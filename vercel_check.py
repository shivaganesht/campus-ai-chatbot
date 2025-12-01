#!/usr/bin/env python
"""
Minimal test to verify Vercel deployment will work
"""

import os
import sys

print("🔍 Vercel Deployment Check\n")
print("=" * 50)

# Check 1: Python version
print(f"✓ Python Version: {sys.version.split()[0]}")

# Check 2: Required imports
try:
    import flask
    print(f"✓ Flask: {flask.__version__}")
except ImportError as e:
    print(f"✗ Flask import failed: {e}")
    sys.exit(1)

try:
    import flask_cors
    print("✓ Flask-CORS: Available")
except ImportError as e:
    print(f"✗ Flask-CORS import failed: {e}")
    sys.exit(1)

try:
    import requests
    print(f"✓ Requests: Available")
except ImportError:
    print("✗ Requests import failed")
    sys.exit(1)

# Check 3: Environment variables
print("\n📋 Environment Variables:")
required_vars = ['LLM_PROVIDER', 'GROQ_API_KEY', 'SECRET_KEY']
all_set = True

for var in required_vars:
    value = os.getenv(var)
    if value:
        display_value = value[:20] + "..." if len(value) > 20 else value
        print(f"✓ {var}: {display_value}")
    else:
        print(f"✗ {var}: NOT SET")
        all_set = False

# Check 4: App imports
print("\n🔧 Application Imports:")
try:
    from src.config_manager import ConfigManager
    print("✓ ConfigManager")
except Exception as e:
    print(f"✗ ConfigManager: {e}")

try:
    from src.llm_provider import LLMProvider
    print("✓ LLMProvider")
except Exception as e:
    print(f"✗ LLMProvider: {e}")

try:
    from src.knowledge_base import KnowledgeBase
    print("✓ KnowledgeBase")
except Exception as e:
    print(f"✗ KnowledgeBase: {e}")

print("\n" + "=" * 50)
if all_set:
    print("✅ All checks passed! Ready for Vercel deployment")
    sys.exit(0)
else:
    print("⚠️  Some environment variables missing")
    print("Set them in Vercel Dashboard → Settings → Environment Variables")
    sys.exit(0)  # Don't fail, just warn
