"""
LLM Provider - FREE Cloud Options for Vercel Deployment
========================================================
Supports FREE cloud-based LLM providers that work on serverless platforms
"""

import os
import requests
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()


class LLMProvider:
    """
    Unified interface for multiple LLM providers (Cloud-based FREE options for Vercel)
    
    FREE Cloud Options (work on Vercel):
    - Groq: FREE, 30 req/min, very fast
    - Hugging Face Inference API: FREE with rate limits
    - Together AI: $25 FREE credit on signup
    
    Local Options (for development):
    - Ollama: FREE but doesn't work on Vercel
    """
    
    def __init__(self):
        self.provider = os.getenv('LLM_PROVIDER', 'groq').lower()
        self.model = None
        self._initialize_provider()
    
    def _initialize_provider(self):
        """Initialize the configured LLM provider"""
        print(f"\n🔧 Initializing LLM Provider: {self.provider.upper()}")
        
        if self.provider == 'groq':
            self._init_groq()
        elif self.provider == 'huggingface_api':
            self._init_huggingface_api()
        elif self.provider == 'together':
            self._init_together()
        elif self.provider == 'ollama':
            self._init_ollama()
        elif self.provider == 'huggingface':
            self._init_huggingface()
        elif self.provider == 'ibm_granite':
            self._init_ibm_granite()
        elif self.provider == 'openai':
            self._init_openai()
        else:
            print(f"⚠️  Unknown provider: {self.provider}, falling back to rule-based")
            self.provider = 'fallback'
    
    def _init_groq(self):
        """Initialize Groq API (100% FREE, 30 requests/min, works on Vercel)"""
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("⚠️  GROQ_API_KEY not found. Get FREE key at: https://console.groq.com")
            self.provider = 'fallback'
            return
        
        try:
            self.model = {
                'api_key': api_key,
                'base_url': 'https://api.groq.com/openai/v1',
                'model': os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')
            }
            
            # Test connection
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            response = requests.post(
                f"{self.model['base_url']}/chat/completions",
                headers=headers,
                json={
                    "model": self.model['model'],
                    "messages": [{"role": "user", "content": "Hi"}],
                    "max_tokens": 10
                },
                timeout=10
            )
            if response.status_code == 200:
                print(f"✅ Groq initialized with model: {self.model['model']}")
                print("   🌐 Works perfectly on Vercel!")
            else:
                raise Exception(f"API test failed: {response.status_code}")
        except Exception as e:
            print(f"⚠️  Groq initialization error: {e}")
            self.provider = 'fallback'
    
    def _init_huggingface_api(self):
        """Initialize Hugging Face Inference API (FREE with rate limits, works on Vercel)"""
        api_key = os.getenv('HUGGINGFACE_API_KEY')
        if not api_key:
            print("⚠️  HUGGINGFACE_API_KEY not found. Get FREE key at: https://huggingface.co/settings/tokens")
            self.provider = 'fallback'
            return
        
        try:
            self.model = {
                'api_key': api_key,
                'model': os.getenv('HUGGINGFACE_MODEL', 'mistralai/Mistral-7B-Instruct-v0.2')
            }
            print(f"✅ Hugging Face Inference API initialized")
            print(f"   Model: {self.model['model']}")
            print("   🌐 Works on Vercel!")
        except Exception as e:
            print(f"⚠️  Hugging Face API error: {e}")
            self.provider = 'fallback'
    
    def _init_together(self):
        """Initialize Together AI ($25 FREE credit, works on Vercel)"""
        api_key = os.getenv('TOGETHER_API_KEY')
        if not api_key:
            print("⚠️  TOGETHER_API_KEY not found. Get $25 FREE at: https://api.together.xyz")
            self.provider = 'fallback'
            return
        
        try:
            self.model = {
                'api_key': api_key,
                'base_url': 'https://api.together.xyz/v1',
                'model': os.getenv('TOGETHER_MODEL', 'mistralai/Mistral-7B-Instruct-v0.2')
            }
            print(f"✅ Together AI initialized with model: {self.model['model']}")
            print("   🌐 Works on Vercel!")
        except Exception as e:
            print(f"⚠️  Together AI error: {e}")
            self.provider = 'fallback'
    
    def _init_ollama(self):
        """Initialize Ollama (100% FREE, runs locally - NOT for Vercel)"""
        print("⚠️  WARNING: Ollama runs locally and won't work on Vercel!")
        print("   For Vercel deployment, use: groq, huggingface_api, or together")
        
        try:
            import ollama
            
            base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
            model_name = os.getenv('OLLAMA_MODEL', 'llama2')
            
            # Test connection
            try:
                response = ollama.chat(
                    model=model_name,
                    messages=[{'role': 'user', 'content': 'Hi'}],
                    options={'num_predict': 10}
                )
                self.model = {'client': ollama, 'model': model_name}
                print(f"✅ Ollama initialized with model: {model_name} (LOCAL ONLY)")
            except Exception as e:
                print(f"⚠️  Ollama not running. Start it with: ollama serve")
                print(f"   Then pull a model: ollama pull llama2")
                print(f"   Error: {e}")
                self.provider = 'fallback'
                
        except ImportError:
            print("⚠️  Ollama not installed. Install with: pip install ollama")
            self.provider = 'fallback'
    
    def _init_huggingface(self):
        """Initialize Hugging Face (FREE with rate limits)"""
        try:
            from transformers import pipeline
            
            model_name = os.getenv('HUGGINGFACE_MODEL', 'HuggingFaceH4/zephyr-7b-beta')
            
            print(f"⏳ Loading Hugging Face model: {model_name}")
            print("   (First time may take a few minutes to download)")
            
            self.model = pipeline(
                "text-generation",
                model=model_name,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7
            )
            print(f"✅ Hugging Face model loaded")
            
        except Exception as e:
            print(f"⚠️  Hugging Face error: {e}")
            self.provider = 'fallback'
    
    def _init_ibm_granite(self):
        """Initialize IBM Granite (PAID)"""
        try:
            from ibm_watsonx_ai.foundation_models import Model
            from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
            
            api_key = os.getenv('IBM_GRANITE_API_KEY')
            project_id = os.getenv('IBM_PROJECT_ID')
            
            if not api_key or not project_id:
                print("⚠️  IBM Granite credentials not found in .env")
                self.provider = 'fallback'
                return
            
            parameters = {
                GenParams.DECODING_METHOD: "greedy",
                GenParams.MAX_NEW_TOKENS: 500,
                GenParams.TEMPERATURE: 0.7,
            }
            
            self.model = Model(
                model_id="ibm/granite-13b-chat-v2",
                params=parameters,
                credentials={"apikey": api_key},
                project_id=project_id
            )
            print("✅ IBM Granite initialized")
            
        except Exception as e:
            print(f"⚠️  IBM Granite error: {e}")
            self.provider = 'fallback'
    
    def _init_openai(self):
        """Initialize OpenAI (PAID)"""
        try:
            import openai
            
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                print("⚠️  OpenAI API key not found in .env")
                self.provider = 'fallback'
                return
            
            openai.api_key = api_key
            self.model = openai
            print("✅ OpenAI initialized")
            
        except Exception as e:
            print(f"⚠️  OpenAI error: {e}")
            self.provider = 'fallback'
    
    def generate(self, prompt: str, max_tokens: int = 300) -> str:
        """Generate response from LLM"""
        
        if self.provider == 'groq':
            return self._generate_groq(prompt, max_tokens)
        elif self.provider == 'huggingface_api':
            return self._generate_huggingface_api(prompt, max_tokens)
        elif self.provider == 'together':
            return self._generate_together(prompt, max_tokens)
        elif self.provider == 'ollama':
            return self._generate_ollama(prompt, max_tokens)
        elif self.provider == 'huggingface':
            return self._generate_huggingface(prompt, max_tokens)
        elif self.provider == 'ibm_granite':
            return self._generate_ibm(prompt)
        elif self.provider == 'openai':
            return self._generate_openai(prompt, max_tokens)
        else:
            return self._generate_fallback(prompt)
    
    def _generate_groq(self, prompt: str, max_tokens: int) -> str:
        """Generate with Groq API"""
        try:
            headers = {
                "Authorization": f"Bearer {self.model['api_key']}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model['model'],
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": 0.7
            }
            
            response = requests.post(
                f"{self.model['base_url']}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Groq generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_huggingface_api(self, prompt: str, max_tokens: int) -> str:
        """Generate with Hugging Face Inference API"""
        try:
            headers = {
                "Authorization": f"Bearer {self.model['api_key']}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": max_tokens,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            
            response = requests.post(
                f"https://api-inference.huggingface.co/models/{self.model['model']}",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "").strip()
            return str(result).strip()
        except Exception as e:
            print(f"Hugging Face API generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_together(self, prompt: str, max_tokens: int) -> str:
        """Generate with Together AI"""
        try:
            headers = {
                "Authorization": f"Bearer {self.model['api_key']}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model['model'],
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": 0.7
            }
            
            response = requests.post(
                f"{self.model['base_url']}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Together AI generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_ollama(self, prompt: str, max_tokens: int) -> str:
        """Generate with Ollama"""
        try:
            response = self.model['client'].chat(
                model=self.model['model'],
                messages=[{'role': 'user', 'content': prompt}],
                options={'num_predict': max_tokens}
            )
            return response['message']['content']
        except Exception as e:
            print(f"Ollama generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_huggingface(self, prompt: str, max_tokens: int) -> str:
        """Generate with Hugging Face"""
        try:
            result = self.model(prompt, max_length=max_tokens)[0]
            return result['generated_text'].replace(prompt, '').strip()
        except Exception as e:
            print(f"Hugging Face generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_ibm(self, prompt: str) -> str:
        """Generate with IBM Granite"""
        try:
            response = self.model.generate_text(prompt=prompt)
            return response.strip()
        except Exception as e:
            print(f"IBM Granite generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_openai(self, prompt: str, max_tokens: int) -> str:
        """Generate with OpenAI"""
        try:
            response = self.model.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI generation error: {e}")
            return self._generate_fallback(prompt)
    
    def _generate_fallback(self, prompt: str) -> str:
        """Rule-based fallback when no LLM is available"""
        return "I can provide information about the campus. Please upload university handbook PDFs in the admin panel for detailed responses."
    
    def is_available(self) -> bool:
        """Check if LLM is available"""
        return self.provider != 'fallback'
