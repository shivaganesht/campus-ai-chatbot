"""
Campus AI Chatbot - Advanced Serverless Version with Admin Panel
"""
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import requests
import json
from datetime import datetime
import secrets

app = Flask(__name__, static_folder='../public')
CORS(app)

# Security
ADMIN_TOKEN = os.getenv('ADMIN_TOKEN', secrets.token_urlsafe(32))

# Groq API configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')

# In-memory database (for serverless, use external DB in production)
students_db = {
    "STU001": {
        "id": "STU001",
        "name": "Rahul Sharma",
        "email": "rahul.sharma@campus.edu",
        "department": "Computer Science",
        "year": "3rd Year",
        "semester": "6th Semester",
        "phone": "+91-9876543210",
        "hostel": "Block A, Room 201",
        "fee_status": "Paid",
        "fee_amount": "₹85,000",
        "due_date": "2024-12-15",
        "library_books": 3,
        "cgpa": "8.5",
        "attendance": "92%",
        "enrolled_date": "2022-08-15"
    },
    "STU002": {
        "id": "STU002",
        "name": "Priya Patel",
        "email": "priya.patel@campus.edu",
        "department": "Electronics Engineering",
        "year": "2nd Year",
        "semester": "4th Semester",
        "phone": "+91-9876543211",
        "hostel": "Block B, Room 305",
        "fee_status": "Pending",
        "fee_amount": "₹82,000",
        "due_date": "2024-12-01",
        "library_books": 2,
        "cgpa": "9.1",
        "attendance": "95%",
        "enrolled_date": "2023-08-15"
    },
    "STU003": {
        "id": "STU003",
        "name": "Arjun Reddy",
        "email": "arjun.reddy@campus.edu",
        "department": "Mechanical Engineering",
        "year": "4th Year",
        "semester": "8th Semester",
        "phone": "+91-9876543212",
        "hostel": "Block A, Room 410",
        "fee_status": "Paid",
        "fee_amount": "₹88,000",
        "due_date": "2024-12-20",
        "library_books": 5,
        "cgpa": "7.8",
        "attendance": "88%",
        "enrolled_date": "2021-08-15"
    },
    "STU004": {
        "id": "STU004",
        "name": "Sneha Gupta",
        "email": "sneha.gupta@campus.edu",
        "department": "Civil Engineering",
        "year": "1st Year",
        "semester": "2nd Semester",
        "phone": "+91-9876543213",
        "hostel": "Block C, Room 102",
        "fee_status": "Paid",
        "fee_amount": "₹80,000",
        "due_date": "2024-11-30",
        "library_books": 1,
        "cgpa": "8.9",
        "attendance": "97%",
        "enrolled_date": "2024-08-15"
    },
    "STU005": {
        "id": "STU005",
        "name": "Vikram Singh",
        "email": "vikram.singh@campus.edu",
        "department": "Computer Science",
        "year": "2nd Year",
        "semester": "3rd Semester",
        "phone": "+91-9876543214",
        "hostel": "Block A, Room 215",
        "fee_status": "Overdue",
        "fee_amount": "₹85,000",
        "due_date": "2024-11-15",
        "library_books": 0,
        "cgpa": "7.2",
        "attendance": "82%",
        "enrolled_date": "2023-08-15"
    },
    "STU006": {
        "id": "STU006",
        "name": "Ananya Krishnan",
        "email": "ananya.krishnan@campus.edu",
        "department": "Information Technology",
        "year": "3rd Year",
        "semester": "5th Semester",
        "phone": "+91-9876543215",
        "hostel": "Block B, Room 208",
        "fee_status": "Paid",
        "fee_amount": "₹84,000",
        "due_date": "2024-12-10",
        "library_books": 4,
        "cgpa": "9.3",
        "attendance": "96%",
        "enrolled_date": "2022-08-15"
    },
    "STU007": {
        "id": "STU007",
        "name": "Rohan Mehta",
        "email": "rohan.mehta@campus.edu",
        "department": "Electrical Engineering",
        "year": "4th Year",
        "semester": "7th Semester",
        "phone": "+91-9876543216",
        "hostel": "Block A, Room 320",
        "fee_status": "Paid",
        "fee_amount": "₹87,000",
        "due_date": "2024-12-18",
        "library_books": 2,
        "cgpa": "8.1",
        "attendance": "90%",
        "enrolled_date": "2021-08-15"
    },
    "STU008": {
        "id": "STU008",
        "name": "Ishita Verma",
        "email": "ishita.verma@campus.edu",
        "department": "Computer Science",
        "year": "1st Year",
        "semester": "1st Semester",
        "phone": "+91-9876543217",
        "hostel": "Block C, Room 115",
        "fee_status": "Pending",
        "fee_amount": "₹85,000",
        "due_date": "2024-12-05",
        "library_books": 1,
        "cgpa": "8.7",
        "attendance": "94%",
        "enrolled_date": "2024-08-15"
    },
    "STU009": {
        "id": "STU009",
        "name": "Aditya Kumar",
        "email": "aditya.kumar@campus.edu",
        "department": "Mechanical Engineering",
        "year": "2nd Year",
        "semester": "4th Semester",
        "phone": "+91-9876543218",
        "hostel": "Block B, Room 412",
        "fee_status": "Paid",
        "fee_amount": "₹83,000",
        "due_date": "2024-12-12",
        "library_books": 3,
        "cgpa": "7.9",
        "attendance": "89%",
        "enrolled_date": "2023-08-15"
    },
    "STU010": {
        "id": "STU010",
        "name": "Kavya Nair",
        "email": "kavya.nair@campus.edu",
        "department": "Electronics Engineering",
        "year": "3rd Year",
        "semester": "6th Semester",
        "phone": "+91-9876543219",
        "hostel": "Block C, Room 301",
        "fee_status": "Paid",
        "fee_amount": "₹86,000",
        "due_date": "2024-12-22",
        "library_books": 6,
        "cgpa": "9.0",
        "attendance": "93%",
        "enrolled_date": "2022-08-15"
    }
}

# Enhanced system prompt with context awareness
SYSTEM_PROMPT = """You are CampusAI, an advanced intelligent assistant for university administration. You have access to comprehensive student data and campus information.

YOUR CAPABILITIES:
- Provide detailed, accurate information about fees, payments, and financial matters
- Access real-time student records, attendance, and academic performance
- Share exam schedules, academic calendars, and important dates
- Explain hostel policies, room allocations, and accommodation details
- Inform about library services, book availability, and borrowing policies
- Answer questions about departments, courses, and faculty
- Guide students through administrative processes

YOUR PERSONALITY:
- Professional yet approachable and friendly
- Proactive in offering relevant information
- Detail-oriented and precise
- Empathetic to student concerns
- Use emojis occasionally to maintain engagement (📚, 🎓, 💡, etc.)

IMPORTANT GUIDELINES:
1. Always provide specific, actionable information
2. If discussing a particular student, reference their actual data when available
3. For general queries, give comprehensive answers with examples
4. Suggest next steps or related information proactively
5. If you don't have specific information, guide students to the appropriate department
6. Maintain student privacy - never share personal data of one student with another

CAMPUS INFORMATION:
- Library Hours: Mon-Fri: 8 AM - 10 PM, Sat-Sun: 9 AM - 6 PM
- Hostel Check-in: 6 PM, Check-out: 10 AM
- Fee Payment Methods: Online portal, Bank transfer, Campus office
- Exam Office: Block E, Room 201 | Hours: 9 AM - 5 PM
- Student Helpdesk: +91-1234567890 | help@campus.edu"""

@app.route('/')
def home():
    return jsonify({
        'status': 'working',
        'message': 'Campus AI Chatbot is running!',
        'version': '1.0',
        'endpoints': ['/api/chat', '/api/health']
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'llm': 'groq-connected'})

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        student_id = data.get('studentId', '').strip()
        chat_history = data.get('history', [])
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        if not GROQ_API_KEY:
            return jsonify({'error': 'Groq API key not configured'}), 500
        
        # Build context with student data if available
        context = SYSTEM_PROMPT
        if student_id and student_id in students_db:
            student = students_db[student_id]
            context += f"\n\nCURRENT STUDENT CONTEXT:\n"
            context += f"Name: {student['name']}\n"
            context += f"ID: {student['id']}\n"
            context += f"Department: {student['department']}\n"
            context += f"Year: {student['year']} ({student['semester']})\n"
            context += f"Fee Status: {student['fee_status']} - {student['fee_amount']}\n"
            context += f"Due Date: {student['due_date']}\n"
            context += f"Hostel: {student['hostel']}\n"
            context += f"Library Books Issued: {student['library_books']}\n"
            context += f"CGPA: {student['cgpa']}\n"
            context += f"Attendance: {student['attendance']}\n"
        
        # Build messages for API
        messages = [{'role': 'system', 'content': context}]
        
        # Add chat history (last 5 messages)
        for msg in chat_history[-5:]:
            messages.append({
                'role': 'user' if msg['type'] == 'user' else 'assistant',
                'content': msg['content']
            })
        
        # Add current message
        messages.append({'role': 'user', 'content': user_message})
        
        # Call Groq API
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': GROQ_MODEL,
            'messages': messages,
            'temperature': 0.7,
            'max_tokens': 800,
            'top_p': 0.9
        }
        
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            bot_response = result['choices'][0]['message']['content']
            return jsonify({
                'response': bot_response,
                'model': GROQ_MODEL,
                'status': 'success',
                'timestamp': datetime.utcnow().isoformat()
            })
        else:
            return jsonify({
                'error': 'Failed to get response from LLM',
                'details': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Student lookup endpoint
@app.route('/api/student/<student_id>', methods=['GET'])
def get_student(student_id):
    if student_id in students_db:
        return jsonify(students_db[student_id])
    return jsonify({'error': 'Student not found'}), 404

# Admin endpoints
@app.route('/api/admin/students', methods=['GET'])
def get_all_students():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token != ADMIN_TOKEN:
        return jsonify({'error': 'Unauthorized'}), 401
    
    return jsonify({
        'students': list(students_db.values()),
        'total': len(students_db)
    })

@app.route('/api/admin/student', methods=['POST'])
def add_student():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token != ADMIN_TOKEN:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        data = request.get_json()
        student_id = data.get('id')
        
        if not student_id:
            return jsonify({'error': 'Student ID is required'}), 400
        
        if student_id in students_db:
            return jsonify({'error': 'Student ID already exists'}), 400
        
        students_db[student_id] = data
        return jsonify({
            'message': 'Student added successfully',
            'student': data
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/admin/student/<student_id>', methods=['PUT'])
def update_student(student_id):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token != ADMIN_TOKEN:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        if student_id not in students_db:
            return jsonify({'error': 'Student not found'}), 404
        
        data = request.get_json()
        students_db[student_id].update(data)
        
        return jsonify({
            'message': 'Student updated successfully',
            'student': students_db[student_id]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/admin/student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token != ADMIN_TOKEN:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        if student_id not in students_db:
            return jsonify({'error': 'Student not found'}), 404
        
        deleted_student = students_db.pop(student_id)
        
        return jsonify({
            'message': 'Student deleted successfully',
            'student': deleted_student
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/admin/token', methods=['GET'])
def get_admin_token():
    return jsonify({'token': ADMIN_TOKEN})

if __name__ == '__main__':
    app.run()
