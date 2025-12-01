# 🎨 Campus Customization Guide

Complete guide to customizing the Campus AI Chatbot for your university.

## 📋 Table of Contents
1. [Basic Setup](#basic-setup)
2. [Branding & Visual Identity](#branding--visual-identity)
3. [Content Customization](#content-customization)
4. [Department Configuration](#department-configuration)
5. [Document Upload Strategy](#document-upload-strategy)
6. [Advanced Customization](#advanced-customization)

## 🚀 Basic Setup

### Step 1: Access Admin Panel
1. Start the application: `python app.py`
2. Open browser: http://localhost:5000/admin
3. Navigate to "🎨 Customization" tab

### Step 2: Campus Information
Fill in your university details:

```json
{
  "name": "Stanford University",
  "short_name": "Stanford",
  "tagline": "The Wind of Freedom Blows",
  "website": "https://www.stanford.edu",
  "contact_email": "info@stanford.edu",
  "contact_phone": "+1-650-723-2300",
  "address": "450 Serra Mall, Stanford, CA 94305",
  "established_year": "1885"
}
```

## 🎨 Branding & Visual Identity

### Logo Guidelines
**Recommended Specifications:**
- Format: PNG with transparent background (or JPG)
- Size: 200x50px to 400x100px
- Max file size: 1MB
- Aspect ratio: 2:1 to 4:1 (horizontal logo works best)

**Upload Steps:**
1. Go to Admin Panel → Customization
2. Find "Upload Assets" section
3. Click "Choose File" under Campus Logo
4. Select your logo file
5. Click "Upload Logo"

### Bot Avatar
**Specifications:**
- Format: PNG, JPG, SVG
- Size: 150x150px minimum
- Recommended: Square/circular image
- Friendly, professional appearance

### Color Scheme
Choose colors that match your brand identity:

**Primary Color**: Main brand color (used in header, buttons)
- Example: #1e3a8a (Stanford Cardinal Red)

**Secondary Color**: Accent color (used in UI elements)
- Example: #3b82f6 (Complementary blue)

**Accent Color**: Highlight color (used for user messages, CTAs)
- Example: #f59e0b (Gold/Yellow)

**Color Picker Tips:**
- Use your university's official brand colors
- Ensure sufficient contrast for readability
- Test on different devices and screens

### Favicon
**Specifications:**
- Format: .ico or .png
- Size: 16x16px, 32x32px, or 48x48px
- Represents your university in browser tabs

## 📝 Content Customization

### Chatbot Settings

#### Bot Name
Choose a memorable, friendly name:
- **Examples**: 
  - "Cardinal Bot" (Stanford themed)
  - "Campus Guide"
  - "[University Name] Assistant"
  - "Edu Helper"

#### Welcome Message
Craft an engaging welcome message:

```
Template:
👋 Hello! I'm [Bot Name], your [University Name] AI Assistant.

I can help you with:
💰 Fee Structure & Payments
📝 Exam Schedules & Results
🏠 Hostel Rules & Accommodation
📚 Library Services & Resources

How can I assist you today?
```

**Tips:**
- Keep it friendly and welcoming
- List main capabilities
- Use emojis for visual appeal (optional)
- Keep under 200 characters for mobile

#### Fallback Message
When the bot doesn't understand:

```
Template:
I apologize, but I don't have specific information about that. 

Please try:
✅ Rephrasing your question
✅ Checking our website: [URL]
✅ Contacting [Department]: [Email]

Or ask me about fees, exams, hostel, or library!
```

## 🏢 Department Configuration

### Setting Up Departments

Edit `config/campus_config.json` → `departments` section:

```json
{
  "fees": {
    "name": "Fee & Finance Office",
    "contact": "fees@youruniversity.edu",
    "phone": "+1-XXX-XXX-1001",
    "location": "Administration Building, Room 101",
    "hours": "Mon-Fri: 9:00 AM - 5:00 PM"
  },
  "examinations": {
    "name": "Examination Cell",
    "contact": "exams@youruniversity.edu",
    "phone": "+1-XXX-XXX-1002",
    "location": "Academic Block, Room 205",
    "hours": "Mon-Fri: 9:30 AM - 4:30 PM"
  },
  "hostel": {
    "name": "Hostel Administration",
    "contact": "hostel@youruniversity.edu",
    "phone": "+1-XXX-XXX-1003",
    "location": "Hostel Office, Main Campus",
    "hours": "Mon-Sun: 8:00 AM - 8:00 PM"
  },
  "library": {
    "name": "Central Library",
    "contact": "library@youruniversity.edu",
    "phone": "+1-XXX-XXX-1004",
    "location": "Library Building, Ground Floor",
    "hours": "Mon-Sat: 8:00 AM - 10:00 PM, Sun: 10:00 AM - 6:00 PM"
  }
}
```

### Quick Links Configuration

Add important portals and resources:

```json
{
  "quick_links": [
    {
      "title": "Student Portal",
      "url": "https://portal.youruniversity.edu",
      "icon": "🎓",
      "category": "academic"
    },
    {
      "title": "Fee Payment Gateway",
      "url": "https://payments.youruniversity.edu",
      "icon": "💳",
      "category": "fees"
    },
    {
      "title": "Online Library",
      "url": "https://library.youruniversity.edu",
      "icon": "📚",
      "category": "library"
    },
    {
      "title": "Course Registration",
      "url": "https://courses.youruniversity.edu",
      "icon": "📝",
      "category": "academic"
    }
  ]
}
```

## 📄 Document Upload Strategy

### Document Preparation

**Before Uploading:**
1. ✅ Remove unnecessary pages (covers, blank pages)
2. ✅ Ensure PDF is not password-protected
3. ✅ Check that text is selectable (not scanned image)
4. ✅ Keep file size under 10MB for best performance

### Recommended Documents by Category

#### Fee Structure
- Annual fee schedule
- Payment deadlines
- Scholarship information
- Refund policy
- Fine structure

#### Exam Schedule
- Semester timetable
- Exam calendar
- Assessment schedule
- Result declaration dates
- Revaluation guidelines

#### Hostel Handbook
- Admission procedure
- Rules and regulations
- Room allocation policy
- Mess menu and timings
- Visitor policy
- Disciplinary guidelines

#### Library Manual
- Membership information
- Borrowing rules
- Operating hours
- Fine structure
- E-resource access
- Study room booking

### Upload Process

1. **Navigate**: Admin Panel → Documents tab
2. **Select Category**: Choose appropriate category
3. **Upload**: Drag & drop or browse for PDF
4. **Wait**: System processes (may take 30-60 seconds)
5. **Verify**: Check documents list for successful upload

### Document Organization Tips

**Naming Convention:**
```
[Category]_[Year]_[Description].pdf

Examples:
- Fees_2025_Undergraduate_Structure.pdf
- Exams_Fall2025_Schedule.pdf
- Hostel_2025_Rules_Regulations.pdf
- Library_Guide_2025.pdf
```

## 🔧 Advanced Customization

### Custom Styling

Edit `static/css/styles.css` for advanced styling:

```css
/* Example: Custom header gradient */
.header {
    background: linear-gradient(135deg, #your-color-1, #your-color-2);
}

/* Example: Custom message bubbles */
.bot-message .message-content {
    background: #your-brand-color;
    border-radius: 15px;
}
```

### Custom Responses

Edit `src/chatbot_engine.py` → `_template_response` method for custom responses.

### Multi-language Support

Add language configuration in `config/campus_config.json`:

```json
{
  "customization": {
    "supported_languages": ["en", "hi", "es"],
    "default_language": "en"
  }
}
```

### Social Media Integration

```json
{
  "social_media": {
    "facebook": "https://facebook.com/youruniversity",
    "twitter": "https://twitter.com/youruniversity",
    "instagram": "https://instagram.com/youruniversity",
    "linkedin": "https://linkedin.com/school/youruniversity",
    "youtube": "https://youtube.com/c/youruniversity"
  }
}
```

## ✅ Customization Checklist

### Phase 1: Basic Setup (15 minutes)
- [ ] Update campus name and information
- [ ] Upload campus logo
- [ ] Set brand colors
- [ ] Configure bot name and welcome message

### Phase 2: Contact Information (10 minutes)
- [ ] Add all department contacts
- [ ] Set office hours
- [ ] Add quick links to portals
- [ ] Configure social media links

### Phase 3: Knowledge Base (30 minutes)
- [ ] Upload fee structure PDF
- [ ] Upload exam schedule PDF
- [ ] Upload hostel handbook PDF
- [ ] Upload library manual PDF

### Phase 4: Testing (15 minutes)
- [ ] Test sample queries for each category
- [ ] Verify department contact information displays correctly
- [ ] Check quick actions functionality
- [ ] Test on mobile devices

### Phase 5: Polish (Optional)
- [ ] Upload custom bot avatar
- [ ] Add favicon
- [ ] Customize colors to exact brand guidelines
- [ ] Add campus background image

## 🎯 Best Practices

### DO:
✅ Use official university branding
✅ Keep welcome message concise
✅ Update documents annually
✅ Test chatbot before deployment
✅ Provide accurate contact information
✅ Use high-quality images

### DON'T:
❌ Use copyrighted images without permission
❌ Upload sensitive/confidential documents
❌ Forget to test on mobile devices
❌ Use too many colors (keep it simple)
❌ Make welcome message too long
❌ Forget to update contact information

## 📞 Need Help?

If you encounter issues during customization:

1. Check the main README.md
2. Review configuration file examples
3. Test with sample data first
4. Check browser console for errors
5. Restart the application after major changes

---

**Happy Customizing! 🎨**

Your campus, your brand, your chatbot!
