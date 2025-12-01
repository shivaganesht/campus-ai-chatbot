"""
Document Processor - PDF Handler
=================================
Process university handbook PDFs and extract knowledge
"""

import os
import re
from typing import Dict, Any, List
from datetime import datetime

try:
    import pdfplumber
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

try:
    from PyPDF2 import PdfReader
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

from src.config_manager import ConfigManager
from src.knowledge_base import KnowledgeBase


class DocumentProcessor:
    """Process PDF handbooks and extract structured information"""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.knowledge_base = KnowledgeBase()
        self.documents_dir = 'documents'
        os.makedirs(self.documents_dir, exist_ok=True)
        
        print(f"📄 Document Processor initialized")
        print(f"   PDF Support: {'✅ pdfplumber' if PDF_AVAILABLE else '✅ PyPDF2' if PYPDF_AVAILABLE else '❌ No PDF library'}")
    
    def process_document(self, file, category: str = 'general') -> Dict[str, Any]:
        """Process uploaded PDF document"""
        
        if not PDF_AVAILABLE and not PYPDF_AVAILABLE:
            return {
                'status': 'error',
                'message': 'PDF libraries not installed. Run: pip install pdfplumber PyPDF2'
            }
        
        try:
            # Save file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_filename = re.sub(r'[^a-zA-Z0-9._-]', '_', file.filename)
            filename = f"{category}_{timestamp}_{safe_filename}"
            filepath = os.path.join(self.documents_dir, filename)
            
            file.save(filepath)
            
            # Extract text
            text = self._extract_text(filepath)
            
            if not text or len(text.strip()) < 50:
                return {
                    'status': 'error',
                    'message': 'Could not extract meaningful text from PDF'
                }
            
            # Auto-detect category
            if category == 'general':
                category = self._detect_category(text)
            
            # Split into chunks
            chunks = self._create_chunks(text)
            
            # Add to knowledge base
            doc_ids = []
            for i, chunk in enumerate(chunks):
                doc_id = self.knowledge_base.add_document(
                    content=chunk,
                    category=category,
                    metadata={
                        'source': filename,
                        'chunk': i + 1,
                        'total_chunks': len(chunks),
                        'processed_at': datetime.now().isoformat()
                    }
                )
                doc_ids.append(doc_id)
            
            return {
                'status': 'success',
                'message': f'Successfully processed {len(chunks)} chunks from PDF',
                'filename': filename,
                'category': category,
                'chunks': len(chunks),
                'document_ids': doc_ids[:5]  # Return first 5 IDs
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Processing error: {str(e)}'
            }
    
    def _extract_text(self, filepath: str) -> str:
        """Extract text from PDF"""
        text = ""
        
        # Try pdfplumber first (better for tables)
        if PDF_AVAILABLE:
            try:
                with pdfplumber.open(filepath) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n\n"
                        
                        # Extract tables
                        tables = page.extract_tables()
                        for table in tables:
                            text += self._format_table(table) + "\n\n"
                
                if text.strip():
                    return text
            except Exception as e:
                print(f"pdfplumber error: {e}")
        
        # Fallback to PyPDF2
        if PYPDF_AVAILABLE:
            try:
                reader = PdfReader(filepath)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n\n"
            except Exception as e:
                print(f"PyPDF2 error: {e}")
        
        return text
    
    def _format_table(self, table: List[List]) -> str:
        """Format table as text"""
        if not table:
            return ""
        
        formatted = []
        for row in table:
            if row:
                row_text = " | ".join(str(cell) if cell else "" for cell in row)
                formatted.append(row_text)
        
        return "\n".join(formatted)
    
    def _detect_category(self, text: str) -> str:
        """Auto-detect document category"""
        text_lower = text.lower()
        
        category_keywords = {
            'fees': ['fee', 'tuition', 'payment', 'scholarship', 'charges', 'dues'],
            'exams': ['exam', 'examination', 'test', 'schedule', 'timetable', 'assessment'],
            'hostel': ['hostel', 'accommodation', 'dormitory', 'mess', 'warden', 'residential'],
            'library': ['library', 'book', 'journal', 'borrow', 'circulation', 'catalogue']
        }
        
        scores = {}
        for category, keywords in category_keywords.items():
            score = sum(text_lower.count(kw) for kw in keywords)
            scores[category] = score
        
        if scores:
            best_category = max(scores, key=scores.get)
            if scores[best_category] >= 5:
                return best_category
        
        return 'general'
    
    def _create_chunks(self, text: str, chunk_size: int = 800, overlap: int = 150) -> List[str]:
        """Split text into overlapping chunks"""
        # Clean text
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        
        # Split by paragraphs
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        chunks = []
        current_chunk = ""
        
        for para in paragraphs:
            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                
                # Add overlap from previous chunk
                if chunks and overlap > 0:
                    prev_words = current_chunk.split()[-30:]  # Last 30 words
                    current_chunk = " ".join(prev_words) + "\n\n" + para + "\n\n"
                else:
                    current_chunk = para + "\n\n"
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def get_processed_documents(self) -> List[Dict[str, Any]]:
        """List all processed documents"""
        documents = []
        
        try:
            for filename in os.listdir(self.documents_dir):
                if filename.endswith('.pdf'):
                    filepath = os.path.join(self.documents_dir, filename)
                    stat = os.stat(filepath)
                    
                    # Parse category from filename
                    parts = filename.split('_')
                    category = parts[0] if parts else 'general'
                    
                    documents.append({
                        'filename': filename,
                        'category': category,
                        'size_kb': round(stat.st_size / 1024, 2),
                        'uploaded_at': datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
        except Exception as e:
            print(f"List documents error: {e}")
        
        return sorted(documents, key=lambda x: x['uploaded_at'], reverse=True)
    
    def delete_document(self, filename: str) -> bool:
        """Delete a processed document"""
        filepath = os.path.join(self.documents_dir, filename)
        
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except Exception as e:
            print(f"Delete error: {e}")
        
        return False
