"""
Chatbot Engine - Core Logic
============================
Intelligent campus assistant with FREE LLM support
"""

import os
import uuid
import json
from datetime import datetime
from typing import Dict, Any, List, Optional

from src.config_manager import ConfigManager
from src.knowledge_base import KnowledgeBase
from src.llm_provider import LLMProvider


class CampusChatbot:
    """Smart campus chatbot with document-based RAG"""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.knowledge_base = KnowledgeBase()
        self.llm = LLMProvider()
        
        self.sessions: Dict[str, Dict] = {}
        self.feedback_log: List[Dict] = []
        
        # Intent classification keywords
        self.intent_keywords = {
            'fees': ['fee', 'fees', 'payment', 'tuition', 'cost', 'scholarship', 'financial', 'charges', 'dues', 'refund'],
            'exams': ['exam', 'examination', 'test', 'assessment', 'schedule', 'timetable', 'result', 'grade', 'marks', 'semester'],
            'hostel': ['hostel', 'accommodation', 'room', 'mess', 'warden', 'dormitory', 'residential', 'lodging', 'food'],
            'library': ['library', 'book', 'journal', 'borrow', 'return', 'fine', 'reading', 'catalogue', 'e-resource'],
            'general': ['contact', 'office', 'timing', 'holiday', 'calendar', 'event', 'admission', 'course']
        }
        
        self.system_prompt = self._create_system_prompt()
        
        print(f"🤖 Chatbot '{self.config.get_value('chatbot_settings', 'bot_name')}' ready!")
    
    def _create_system_prompt(self) -> str:
        """Create system prompt for LLM"""
        campus_name = self.config.get_value('campus_info', 'name', default='University')
        bot_name = self.config.get_value('chatbot_settings', 'bot_name', default='CampusBot')
        
        return f"""You are {bot_name}, an AI assistant for {campus_name}.

Your role: Help students, faculty, and visitors with campus queries.

You can help with:
- Fee structure and payment details
- Exam schedules and academic calendar
- Hostel rules and accommodation
- Library services and timings
- General campus information

Guidelines:
1. Be friendly, professional, and helpful
2. Provide accurate information based on university documents
3. If unsure, suggest contacting the relevant department
4. Keep responses concise (2-4 sentences)
5. Format responses clearly with bullet points when needed
6. Always provide contact info when relevant

When you lack specific information, clearly state that and suggest alternatives."""
    
    def _get_session(self, session_id: str) -> Dict:
        """Get or create session"""
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                'id': session_id,
                'created_at': datetime.now().isoformat(),
                'history': [],
                'context': {}
            }
        return self.sessions[session_id]
    
    def _classify_intent(self, message: str) -> str:
        """Classify user intent"""
        message_lower = message.lower()
        
        scores = {}
        for intent, keywords in self.intent_keywords.items():
            score = sum(1 for kw in keywords if kw in message_lower)
            scores[intent] = score
        
        if scores:
            best_intent = max(scores, key=scores.get)
            if scores[best_intent] > 0:
                return best_intent
        
        return 'general'
    
    def _get_context_from_kb(self, query: str, intent: str) -> str:
        """Retrieve relevant context from knowledge base"""
        results = self.knowledge_base.search(query, category=intent, top_k=3)
        
        if results:
            context_parts = []
            for i, result in enumerate(results, 1):
                context_parts.append(f"[Source {i}]:\n{result['content'][:500]}")
            
            return "\n\n".join(context_parts)
        
        return ""
    
    def _generate_response(self, query: str, context: str, session: Dict, intent: str) -> str:
        """Generate response using LLM or fallback"""
        
        # Build conversation history
        history_text = ""
        for msg in session['history'][-3:]:  # Last 3 exchanges
            history_text += f"User: {msg['user']}\nAssistant: {msg['bot']}\n\n"
        
        # Create prompt
        if context:
            prompt = f"""{self.system_prompt}

Relevant Information from University Documents:
{context}

Recent Conversation:
{history_text}

User Question: {query}

Assistant Response (be helpful and concise):"""
        else:
            prompt = f"""{self.system_prompt}

Recent Conversation:
{history_text}

User Question: {query}

Assistant Response:"""
        
        # Try LLM generation
        if self.llm.is_available():
            try:
                response = self.llm.generate(prompt, max_tokens=300)
                if response and len(response.strip()) > 20:
                    return response.strip()
            except Exception as e:
                print(f"LLM generation error: {e}")
        
        # Fallback to template responses
        return self._template_response(query, context, intent)
    
    def _template_response(self, query: str, context: str, intent: str) -> str:
        """Template-based fallback response"""
        department = self.config.get_department_info(intent)
        
        if context:
            # Extract key information from context
            context_preview = context[:400] + "..." if len(context) > 400 else context
            response = f"Based on our university documents:\n\n{context_preview}\n\n"
            
            if department:
                response += f"For more details, contact:\n📧 {department.get('contact')}\n📞 {department.get('phone')}"
            
            return response
        
        # No context - provide department info
        templates = {
            'fees': f"💰 **Fee Information**\n\nFor detailed fee structure and payment information:\n\n📧 Email: {department.get('contact') if department else 'fees@university.edu'}\n📞 Phone: {department.get('phone') if department else 'See admin office'}\n📍 Location: {department.get('location') if department else 'Admin Block'}\n\n💡 Tip: Upload fee structure PDFs in the admin panel for detailed answers!",
            
            'exams': f"📝 **Examination Information**\n\nFor exam schedules and related queries:\n\n📧 Email: {department.get('contact') if department else 'exams@university.edu'}\n📞 Phone: {department.get('phone') if department else 'See exam cell'}\n📍 Location: {department.get('location') if department else 'Academic Block'}\n\n💡 Tip: Upload exam schedule PDFs in the admin panel!",
            
            'hostel': f"🏠 **Hostel Information**\n\nFor hostel rules and accommodation:\n\n📧 Email: {department.get('contact') if department else 'hostel@university.edu'}\n📞 Phone: {department.get('phone') if department else 'See hostel office'}\n📍 Location: {department.get('location') if department else 'Hostel Office'}\n\n💡 Tip: Upload hostel handbook PDFs for detailed information!",
            
            'library': f"📚 **Library Information**\n\nFor library services and timings:\n\n📧 Email: {department.get('contact') if department else 'library@university.edu'}\n📞 Phone: {department.get('phone') if department else 'See library desk'}\n📍 Location: {department.get('location') if department else 'Central Library'}\n⏰ Hours: {department.get('hours') if department else 'Mon-Sat: 8 AM - 10 PM'}\n\n💡 Tip: Upload library handbook PDFs for complete details!",
            
            'general': f"I'd be happy to help! I can assist with:\n\n💰 Fee Structure\n📝 Exam Schedules\n🏠 Hostel Information\n📚 Library Services\n\nPlease ask a specific question, or contact the administration office:\n📧 {self.config.get_value('campus_info', 'contact_email')}\n📞 {self.config.get_value('campus_info', 'contact_phone')}"
        }
        
        return templates.get(intent, templates['general'])
    
    def get_response(self, message: str, session_id: str = 'default') -> Dict[str, Any]:
        """Main method to get chatbot response"""
        session = self._get_session(session_id)
        message_id = str(uuid.uuid4())
        
        # Classify intent
        intent = self._classify_intent(message)
        
        # Get context from knowledge base
        context = self._get_context_from_kb(message, intent)
        
        # Generate response
        response_text = self._generate_response(message, context, session, intent)
        
        # Get related actions
        related_actions = self._get_related_actions(intent)
        
        # Get department info
        department_info = self.config.get_department_info(intent)
        
        # Update session
        session['history'].append({
            'user': message,
            'bot': response_text,
            'timestamp': datetime.now().isoformat(),
            'intent': intent
        })
        
        return {
            'message_id': message_id,
            'response': response_text,
            'intent': intent,
            'has_context': bool(context),
            'related_actions': related_actions,
            'department_info': department_info,
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_related_actions(self, intent: str) -> List[Dict[str, str]]:
        """Get suggested follow-up actions"""
        actions = {
            'fees': [
                {"label": "💳 Payment Methods", "query": "What payment methods are available?"},
                {"label": "🎓 Scholarships", "query": "Tell me about scholarships"},
                {"label": "📋 Fee Breakdown", "query": "Show detailed fee breakdown"}
            ],
            'exams': [
                {"label": "📅 Full Schedule", "query": "Show complete exam schedule"},
                {"label": "📊 Results", "query": "How to check results?"},
                {"label": "📝 Revaluation", "query": "Revaluation process"}
            ],
            'hostel': [
                {"label": "🍽️ Mess Info", "query": "Tell me about mess facilities"},
                {"label": "🚪 Room Allocation", "query": "How is room allocation done?"},
                {"label": "📋 Rules", "query": "What are the hostel rules?"}
            ],
            'library': [
                {"label": "⏰ Timings", "query": "Library timings?"},
                {"label": "📖 Borrowing", "query": "How to borrow books?"},
                {"label": "💻 E-Resources", "query": "Available e-resources?"}
            ],
            'general': [
                {"label": "📞 Contacts", "query": "How to contact departments?"},
                {"label": "📅 Calendar", "query": "Academic calendar"},
                {"label": "🗺️ Campus Info", "query": "Tell me about the campus"}
            ]
        }
        
        return actions.get(intent, actions['general'])
    
    def record_feedback(self, message_id: str, rating: int, comment: str = ""):
        """Record user feedback"""
        feedback = {
            'message_id': message_id,
            'rating': rating,
            'comment': comment,
            'timestamp': datetime.now().isoformat()
        }
        
        self.feedback_log.append(feedback)
        
        # Save to file
        try:
            os.makedirs('data', exist_ok=True)
            with open('data/feedback.jsonl', 'a', encoding='utf-8') as f:
                f.write(json.dumps(feedback) + '\n')
        except Exception as e:
            print(f"Feedback save error: {e}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get chatbot statistics"""
        total_messages = sum(len(s['history']) for s in self.sessions.values())
        
        return {
            'total_sessions': len(self.sessions),
            'total_messages': total_messages,
            'total_feedback': len(self.feedback_log),
            'llm_provider': self.llm.provider,
            'llm_available': self.llm.is_available()
        }
