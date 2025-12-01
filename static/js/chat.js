// Campus Chatbot - Main Chat Interface

// Configuration
const config = JSON.parse(document.getElementById('config-data').textContent);
let sessionId = generateSessionId();

// Socket.IO connection
const socket = io();

// DOM Elements
const messagesContainer = document.getElementById('messages-container');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const charCount = document.getElementById('char-count');
const typingIndicator = document.getElementById('typing-indicator');
const clearChatBtn = document.getElementById('clear-chat');
const quickActions = document.querySelectorAll('.action-btn');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initializeChat();
    setupEventListeners();
});

function generateSessionId() {
    return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

function initializeChat() {
    // Auto-focus input
    messageInput.focus();
    
    // Apply custom colors from config
    applyBranding();
    
    console.log('✅ Chat initialized');
}

function applyBranding() {
    if (config.branding) {
        document.documentElement.style.setProperty('--primary-color', config.branding.primary_color);
        document.documentElement.style.setProperty('--secondary-color', config.branding.secondary_color);
        document.documentElement.style.setProperty('--accent-color', config.branding.accent_color);
    }
}

function setupEventListeners() {
    // Send button
    sendBtn.addEventListener('click', () => sendMessage());
    
    // Enter to send (Shift+Enter for new line)
    messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // Character count
    messageInput.addEventListener('input', () => {
        const length = messageInput.value.length;
        charCount.textContent = `${length}/500`;
        
        // Auto-resize textarea
        messageInput.style.height = 'auto';
        messageInput.style.height = messageInput.scrollHeight + 'px';
    });
    
    // Clear chat
    clearChatBtn.addEventListener('click', () => clearChat());
    
    // Quick actions
    quickActions.forEach(btn => {
        btn.addEventListener('click', () => {
            const query = btn.dataset.query;
            messageInput.value = query;
            sendMessage();
        });
    });
    
    // Socket events
    socket.on('connected', (data) => {
        console.log('🔌 Connected to server');
    });
    
    socket.on('typing', (data) => {
        typingIndicator.style.display = data.status ? 'flex' : 'none';
        scrollToBottom();
    });
    
    socket.on('response', (data) => {
        displayBotMessage(data);
    });
    
    socket.on('error', (data) => {
        showError(data.message);
    });
}

async function sendMessage() {
    const message = messageInput.value.trim();
    
    if (!message || message.length > 500) {
        return;
    }
    
    // Display user message
    displayUserMessage(message);
    
    // Clear input
    messageInput.value = '';
    charCount.textContent = '0/500';
    messageInput.style.height = 'auto';
    
    // Disable input while processing
    messageInput.disabled = true;
    sendBtn.disabled = true;
    
    try {
        // Send via REST API
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayBotMessage(data);
        } else {
            showError(data.error || 'Failed to get response');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showError('Network error. Please try again.');
    } finally {
        messageInput.disabled = false;
        sendBtn.disabled = false;
        messageInput.focus();
    }
}

function displayUserMessage(text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user-message';
    
    messageDiv.innerHTML = `
        <div class="message-avatar">👤</div>
        <div class="message-content">
            <div class="message-text">${escapeHtml(text)}</div>
            <div class="message-time">${formatTime(new Date())}</div>
        </div>
    `;
    
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

function displayBotMessage(data) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    
    let html = `
        <div class="message-avatar">🤖</div>
        <div class="message-content">
            <div class="message-text">${formatBotResponse(data.response)}</div>
    `;
    
    // Add related actions if available
    if (data.related_actions && data.related_actions.length > 0) {
        html += '<div class="related-actions">';
        data.related_actions.forEach(action => {
            html += `<button class="related-action-btn" onclick="handleRelatedAction('${escapeHtml(action.query)}')">${escapeHtml(action.label)}</button>`;
        });
        html += '</div>';
    }
    
    html += `
            <div class="message-time">${formatTime(new Date())}</div>
        </div>
    `;
    
    messageDiv.innerHTML = html;
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

function formatBotResponse(text) {
    // Convert markdown-like formatting to HTML
    text = escapeHtml(text);
    
    // Bold
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Line breaks
    text = text.replace(/\n/g, '<br>');
    
    return text;
}

function handleRelatedAction(query) {
    messageInput.value = query;
    sendMessage();
}

function clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
        // Keep only the welcome message
        const welcomeMessage = messagesContainer.querySelector('.welcome-message');
        messagesContainer.innerHTML = '';
        if (welcomeMessage) {
            messagesContainer.appendChild(welcomeMessage);
        }
        
        // Generate new session
        sessionId = generateSessionId();
    }
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'message bot-message';
    errorDiv.innerHTML = `
        <div class="message-avatar">⚠️</div>
        <div class="message-content" style="background: #fee2e2; border-left: 4px solid #ef4444;">
            <div class="message-text" style="color: #991b1b;">
                <strong>Error:</strong> ${escapeHtml(message)}
            </div>
        </div>
    `;
    
    messagesContainer.appendChild(errorDiv);
    scrollToBottom();
}

function scrollToBottom() {
    requestAnimationFrame(() => {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    });
}

function formatTime(date) {
    return date.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Export functions for related actions
window.handleRelatedAction = handleRelatedAction;
