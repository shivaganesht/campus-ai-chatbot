// Admin Panel JavaScript

// Tab Management
const tabs = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const targetTab = tab.dataset.tab;
        
        // Update tab buttons
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        
        // Update tab contents
        tabContents.forEach(content => {
            content.classList.remove('active');
            if (content.id === `${targetTab}-tab`) {
                content.classList.add('active');
            }
        });
        
        // Load tab-specific data
        if (targetTab === 'documents') {
            loadDocuments();
        } else if (targetTab === 'statistics') {
            loadStatistics();
        } else if (targetTab === 'settings') {
            loadSettings();
        }
    });
});

// Campus Info Form
document.getElementById('campus-info-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        campus_info: {
            name: document.getElementById('campus-name').value,
            short_name: document.getElementById('campus-short-name').value,
            tagline: document.getElementById('campus-tagline').value,
            website: document.getElementById('campus-website').value,
            contact_email: document.getElementById('campus-email').value,
            contact_phone: document.getElementById('campus-phone').value
        }
    };
    
    await updateConfig(data, 'Campus information updated successfully!');
});

// Branding Form
document.getElementById('branding-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        branding: {
            primary_color: document.getElementById('primary-color').value,
            secondary_color: document.getElementById('secondary-color').value,
            accent_color: document.getElementById('accent-color').value
        }
    };
    
    await updateConfig(data, 'Branding colors applied successfully!');
});

// Chatbot Settings Form
document.getElementById('chatbot-settings-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        chatbot_settings: {
            bot_name: document.getElementById('bot-name').value,
            welcome_message: document.getElementById('welcome-message').value,
            fallback_message: document.getElementById('fallback-message').value
        }
    };
    
    await updateConfig(data, 'Chatbot settings saved successfully!');
});

// Update Configuration
async function updateConfig(data, successMessage) {
    try {
        const response = await fetch('/api/config', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showToast(successMessage, 'success');
        } else {
            showToast('Failed to update: ' + result.message, 'error');
        }
    } catch (error) {
        showToast('Network error: ' + error.message, 'error');
    }
}

// Upload Asset
async function uploadAsset(type, inputId) {
    const fileInput = document.getElementById(inputId);
    const file = fileInput.files[0];
    
    if (!file) {
        showToast('Please select a file', 'error');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    formData.append('type', type);
    
    try {
        const response = await fetch('/api/upload-asset', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showToast(`${type} uploaded successfully!`, 'success');
            fileInput.value = '';
        } else {
            showToast('Upload failed: ' + result.error, 'error');
        }
    } catch (error) {
        showToast('Upload error: ' + error.message, 'error');
    }
}

// Document Upload Form
document.getElementById('document-upload-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const fileInput = document.getElementById('pdf-file');
    const category = document.getElementById('doc-category').value;
    const file = fileInput.files[0];
    
    if (!file) {
        showToast('Please select a PDF file', 'error');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    formData.append('category', category);
    
    showToast('Processing document... This may take a moment.', 'info');
    
    try {
        const response = await fetch('/api/upload-document', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showToast(`Document processed! Created ${result.chunks} knowledge chunks.`, 'success');
            fileInput.value = '';
            loadDocuments();
        } else {
            showToast('Processing failed: ' + result.error, 'error');
        }
    } catch (error) {
        showToast('Upload error: ' + error.message, 'error');
    }
});

// Load Documents
async function loadDocuments() {
    const container = document.getElementById('documents-container');
    container.innerHTML = '<p class="loading">Loading documents...</p>';
    
    try {
        const response = await fetch('/api/documents');
        const data = await response.json();
        
        if (data.documents && data.documents.length > 0) {
            let html = '';
            data.documents.forEach(doc => {
                html += `
                    <div class="document-item">
                        <div class="document-info">
                            <h4>📄 ${doc.filename}</h4>
                            <p class="document-meta">
                                <span class="category-badge">${doc.category}</span>
                                ${doc.size_kb} KB • Uploaded: ${formatDate(doc.uploaded_at)}
                            </p>
                        </div>
                        <button class="delete-doc-btn" onclick="deleteDocument('${doc.filename}')">
                            🗑️ Delete
                        </button>
                    </div>
                `;
            });
            container.innerHTML = html;
        } else {
            container.innerHTML = '<p class="loading">No documents uploaded yet. Upload your first handbook PDF above!</p>';
        }
    } catch (error) {
        container.innerHTML = '<p class="loading" style="color: red;">Error loading documents</p>';
    }
}

// Delete Document
async function deleteDocument(filename) {
    if (!confirm(`Are you sure you want to delete ${filename}?`)) {
        return;
    }
    
    try {
        const response = await fetch(`/api/documents/${filename}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showToast('Document deleted successfully', 'success');
            loadDocuments();
        } else {
            showToast('Failed to delete document', 'error');
        }
    } catch (error) {
        showToast('Delete error: ' + error.message, 'error');
    }
}

// Load Statistics
async function loadStatistics() {
    const container = document.getElementById('stats-container');
    container.innerHTML = '<p class="loading">Loading statistics...</p>';
    
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();
        
        let html = '<div class="stats-grid">';
        
        // Chatbot stats
        html += `
            <div class="stat-card">
                <div class="stat-value">${data.chatbot.total_sessions}</div>
                <div class="stat-label">Total Sessions</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${data.chatbot.total_messages}</div>
                <div class="stat-label">Messages Exchanged</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${data.knowledge_base.total_documents}</div>
                <div class="stat-label">Knowledge Chunks</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${data.documents}</div>
                <div class="stat-label">PDF Documents</div>
            </div>
        `;
        
        html += '</div>';
        
        // Knowledge base breakdown
        html += '<div class="section-card"><h3>📚 Knowledge Base by Category</h3><div class="stats-grid">';
        for (const [category, count] of Object.entries(data.knowledge_base.by_category)) {
            html += `
                <div class="stat-card">
                    <div class="stat-value">${count}</div>
                    <div class="stat-label">${category.charAt(0).toUpperCase() + category.slice(1)}</div>
                </div>
            `;
        }
        html += '</div></div>';
        
        // System info
        html += `
            <div class="section-card">
                <h3>⚙️ System Information</h3>
                <p><strong>LLM Provider:</strong> ${data.chatbot.llm_provider}</p>
                <p><strong>LLM Available:</strong> ${data.chatbot.llm_available ? '✅ Yes' : '❌ No (using fallback)'}</p>
                <p><strong>Vector DB:</strong> ${data.knowledge_base.vector_enabled ? '✅ ChromaDB' : '❌ Keyword search'}</p>
                <p><strong>Embeddings:</strong> ${data.knowledge_base.embeddings_enabled ? '✅ Enabled' : '❌ Disabled'}</p>
            </div>
        `;
        
        container.innerHTML = html;
    } catch (error) {
        container.innerHTML = '<p class="loading" style="color: red;">Error loading statistics</p>';
    }
}

// Load Settings
async function loadSettings() {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        
        const providerSpan = document.getElementById('current-provider');
        if (providerSpan) {
            providerSpan.textContent = data.llm_provider.toUpperCase();
        }
    } catch (error) {
        console.error('Error loading settings:', error);
    }
}

// Toast Notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'slideIn 0.3s reverse';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Utility Functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Export functions for global access
window.uploadAsset = uploadAsset;
window.deleteDocument = deleteDocument;

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    loadDocuments();
});
