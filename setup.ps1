# Campus AI Chatbot - Quick Start Script
# This script helps you set up the chatbot quickly

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  🎓 Campus AI Chatbot - Setup" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Check Python version
Write-Host "✅ Checking Python version..." -ForegroundColor Green
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "   Found: $pythonVersion" -ForegroundColor Gray
} else {
    Write-Host "❌ Python not found! Please install Python 3.9 or higher" -ForegroundColor Red
    exit 1
}

# Check if virtual environment exists
$venvPath = "venv"
if (Test-Path $venvPath) {
    Write-Host "✅ Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "🔄 Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host ""
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
Write-Host "   (This may take a few minutes)" -ForegroundColor Gray
pip install -r requirements.txt --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "⚠️  Some dependencies may have issues, but continuing..." -ForegroundColor Yellow
}

# Check if .env exists
if (Test-Path ".env") {
    Write-Host "✅ Environment file (.env) found" -ForegroundColor Green
} else {
    Write-Host "📝 Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "✅ .env file created - Please configure it!" -ForegroundColor Green
}

# Create necessary directories
Write-Host ""
Write-Host "📁 Creating directories..." -ForegroundColor Yellow
$directories = @("assets", "documents", "data", "config")
foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "   Created: $dir" -ForegroundColor Gray
    }
}
Write-Host "✅ Directories ready" -ForegroundColor Green

# Check for Ollama
Write-Host ""
Write-Host "🤖 Checking for LLM providers..." -ForegroundColor Yellow
$ollamaInstalled = Get-Command ollama -ErrorAction SilentlyContinue
if ($ollamaInstalled) {
    Write-Host "✅ Ollama found! (Best FREE option)" -ForegroundColor Green
    Write-Host "   Run 'ollama serve' in another terminal" -ForegroundColor Gray
    Write-Host "   Then run 'ollama pull llama2' to download model" -ForegroundColor Gray
} else {
    Write-Host "ℹ️  Ollama not found (recommended for FREE local AI)" -ForegroundColor Cyan
    Write-Host "   Download from: https://ollama.ai" -ForegroundColor Gray
}

# Summary
Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  ✨ Setup Complete!" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. Configure .env file with your preferences" -ForegroundColor White
Write-Host "2. (Optional) Install Ollama for FREE local AI" -ForegroundColor White
Write-Host "3. Run the application: python app.py" -ForegroundColor White
Write-Host ""
Write-Host "Quick Start Commands:" -ForegroundColor Yellow
Write-Host "  .\venv\Scripts\Activate.ps1  # Activate virtual environment" -ForegroundColor Gray
Write-Host "  python app.py                 # Start the chatbot" -ForegroundColor Gray
Write-Host ""
Write-Host "Access URLs:" -ForegroundColor Yellow
Write-Host "  Main Chat:  http://localhost:5000" -ForegroundColor Gray
Write-Host "  Admin:      http://localhost:5000/admin" -ForegroundColor Gray
Write-Host ""

# Ask if user wants to start the app
$response = Read-Host "Would you like to start the application now? (y/n)"
if ($response -eq 'y' -or $response -eq 'Y') {
    Write-Host ""
    Write-Host "🚀 Starting Campus AI Chatbot..." -ForegroundColor Green
    Write-Host ""
    python app.py
} else {
    Write-Host ""
    Write-Host "👍 Great! Run 'python app.py' when you're ready" -ForegroundColor Green
    Write-Host ""
}
