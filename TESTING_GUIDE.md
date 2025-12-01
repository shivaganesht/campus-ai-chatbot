# Campus AI Chatbot - Sample Data for Testing

## Sample Questions to Test

### Fee Structure Questions
```
1. What is the fee structure for undergraduate programs?
2. How can I pay my tuition fees?
3. What scholarships are available?
4. What is the refund policy?
5. Are there any late payment fines?
```

### Exam Schedule Questions
```
1. When are the semester exams?
2. How do I check my exam results?
3. What is the examination schedule for this semester?
4. Can I apply for revaluation?
5. Where do I find the exam timetable?
```

### Hostel Questions
```
1. What are the hostel rules?
2. How is room allocation done?
3. What are the mess timings?
4. Can visitors stay in the hostel?
5. What is the hostel curfew time?
```

### Library Questions
```
1. What are the library timings?
2. How many books can I borrow?
3. What is the fine for late returns?
4. How do I access e-resources?
5. Can I book a study room?
```

### General Questions
```
1. How do I contact the administration?
2. Where is the academic calendar?
3. What are the office hours?
4. How do I register for courses?
5. Tell me about the campus facilities
```

## Sample PDF Content for Testing

### Fee Structure Sample (fees_sample.txt)
```
UNIVERSITY FEE STRUCTURE 2025

UNDERGRADUATE PROGRAMS
- Tuition Fee: $10,000 per semester
- Library Fee: $200 per semester
- Laboratory Fee: $500 per semester
- Sports Fee: $150 per semester
- Total: $10,850 per semester

PAYMENT METHODS
- Online payment via student portal
- Bank transfer
- Credit/Debit card
- Cash at fee counter

PAYMENT DEADLINES
- Fall Semester: August 15
- Spring Semester: January 15

LATE PAYMENT FINE
- After deadline: $100 per week

SCHOLARSHIPS
- Merit Scholarship: Up to 50% tuition waiver
- Need-based aid: Up to $5,000 per year
- Sports scholarship: Up to 30% tuition waiver

REFUND POLICY
- Before semester starts: 90% refund
- Within first week: 50% refund
- After first week: No refund
```

### Exam Schedule Sample (exam_sample.txt)
```
SEMESTER EXAMINATION SCHEDULE
Fall 2025

IMPORTANT DATES
- Exam Registration: November 1-15
- Exam Period: December 10-24
- Results: January 10

EXAMINATION GUIDELINES
1. Arrive 15 minutes before exam
2. Bring student ID card
3. No electronic devices allowed
4. Use blue or black pen only

REVALUATION
- Application deadline: 7 days after result
- Fee: $50 per paper
- Results: Within 2 weeks

EXAM TIMETABLE
Monday, Dec 10: Mathematics (9 AM - 12 PM)
Tuesday, Dec 11: Physics (9 AM - 12 PM)
Wednesday, Dec 12: Chemistry (2 PM - 5 PM)
Thursday, Dec 13: English (9 AM - 12 PM)
Friday, Dec 14: Computer Science (2 PM - 5 PM)
```

### Hostel Rules Sample (hostel_sample.txt)
```
HOSTEL RULES AND REGULATIONS

CHECK-IN/CHECK-OUT
- Check-in: 9 AM - 6 PM
- Check-out: Before 11 AM
- Late check-out: Additional charge

ROOM ALLOCATION
- Based on availability and seniority
- Room change requests: First week of semester
- Roommate preference: Subject to approval

TIMINGS
- Entry Gate: 6 AM - 10 PM
- Mess Breakfast: 7 AM - 9 AM
- Mess Lunch: 12 PM - 2 PM
- Mess Dinner: 7 PM - 9 PM

VISITORS
- Allowed between 9 AM - 6 PM
- Registration at reception mandatory
- No overnight visitors

GENERAL RULES
1. Maintain cleanliness in rooms
2. No loud music after 10 PM
3. No smoking or alcohol
4. Report maintenance issues promptly
5. No pets allowed

MESS MENU
Monday: Breakfast - Toast, Eggs / Lunch - Rice, Curry / Dinner - Pasta
Tuesday: Breakfast - Pancakes / Lunch - Biryani / Dinner - Soup, Sandwich
Wednesday: Breakfast - Oatmeal / Lunch - Chinese / Dinner - Pizza
Thursday: Breakfast - Cereals / Lunch - Mexican / Dinner - Salad Bowl
Friday: Breakfast - French Toast / Lunch - Indian Thali / Dinner - Burgers
Saturday: Breakfast - Continental / Lunch - BBQ / Dinner - Special Menu
Sunday: Breakfast - Brunch / Lunch - Family Meal / Dinner - Light Dinner
```

### Library Manual Sample (library_sample.txt)
```
LIBRARY SERVICES GUIDE

OPERATING HOURS
- Monday to Friday: 8 AM - 10 PM
- Saturday: 9 AM - 8 PM
- Sunday: 10 AM - 6 PM
- Holidays: Closed

BORROWING RULES
Undergraduate Students:
- Maximum books: 5
- Loan period: 14 days
- Renewal: Once (online or in-person)

Graduate Students:
- Maximum books: 10
- Loan period: 30 days
- Renewal: Twice

FINES
- Late return: $1 per day per book
- Lost book: Replacement cost + $20 processing fee
- Damaged book: Assessed per damage

E-RESOURCES
- 10,000+ e-journals
- 50,000+ e-books
- Research databases: JSTOR, IEEE, ACM
- Access: Via student portal credentials

STUDY ROOMS
- Available for group study
- Booking: 24 hours in advance
- Maximum duration: 3 hours
- Book online or at circulation desk

REFERENCE SECTION
- Cannot be borrowed
- Photocopy facilities available
- Scan and email service

LIBRARY CARDS
- Issued to all enrolled students
- Report loss immediately
- Replacement fee: $10
```

## Testing Checklist

### Before Testing
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Configure .env file
- [ ] Create sample PDFs from above content
- [ ] Start the application: `python app.py`

### Admin Panel Testing
- [ ] Access http://localhost:5000/admin
- [ ] Update campus information
- [ ] Upload campus logo (any sample image)
- [ ] Change brand colors
- [ ] Upload all 4 sample PDFs (one for each category)
- [ ] Verify documents appear in list

### Chatbot Testing
- [ ] Access http://localhost:5000
- [ ] Test quick action buttons
- [ ] Ask sample questions from each category
- [ ] Verify bot responds with relevant information
- [ ] Check related action buttons appear
- [ ] Test department contact information display

### Functionality Testing
- [ ] Clear chat history
- [ ] Test character limit (500 chars)
- [ ] Test Enter key to send
- [ ] Test Shift+Enter for new line
- [ ] Check responsive design on mobile
- [ ] Verify typing indicator appears
- [ ] Test WebSocket connection

### Performance Testing
- [ ] Response time < 3 seconds
- [ ] PDF processing < 60 seconds
- [ ] Memory usage acceptable
- [ ] No console errors

## Expected Behavior

### With LLM (Ollama/Hugging Face)
- Natural, conversational responses
- Context-aware answers
- Follows system prompt personality
- Cites sources when available

### Without LLM (Fallback Mode)
- Template-based responses
- Shows relevant document excerpts
- Provides department contact info
- Suggests alternative queries

## Troubleshooting

### Bot gives generic responses
- Upload relevant PDF documents
- Check PDF text is extractable (not scanned)
- Verify LLM is configured and running

### PDF upload fails
- Check file size < 16MB
- Ensure PDF is not password-protected
- Verify pdfplumber or PyPDF2 installed

### No search results from knowledge base
- Confirm documents were processed successfully
- Check ChromaDB initialization
- Verify sentence-transformers installed

---

**Ready to Test?**
1. Create sample PDFs from content above
2. Upload via admin panel
3. Start asking questions!
4. Customize for your campus!
