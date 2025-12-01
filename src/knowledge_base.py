"""
Knowledge Base - Lightweight Storage for Vercel
================================================
Simple JSON-based storage (no heavy dependencies)
"""

import os
import json
import re
from typing import List, Dict, Any, Optional
from datetime import datetime


class KnowledgeBase:
    """Lightweight knowledge storage for Vercel deployment"""
    
    def __init__(self, persist_directory: str = 'data/knowledge_base'):
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        
        self.categories = ['fees', 'exams', 'hostel', 'library', 'general']
        self.simple_store: Dict[str, List[Dict]] = {}
        
        # Load existing data
        self._load_simple_store()
        
        print("✅ Knowledge Base initialized (JSON mode for Vercel)")
        
        # Load simple backup store
        self._load_simple_store()
        
        print(f"📚 Knowledge Base initialized")
        print(f"   Vector DB: {'✅ ChromaDB' if self.client else '❌ Using fallback'}")
        print(f"   Embeddings: {'✅ Enabled' if self.embedding_model else '❌ Disabled'}")
    
    def _init_embeddings(self) -> Optional[Any]:
        """Initialize embedding model"""
        if not EMBEDDINGS_AVAILABLE:
            return None
        
        try:
            model = SentenceTransformer('all-MiniLM-L6-v2')
            return model
        except Exception as e:
            print(f"Embedding model error: {e}")
            return None
    
    def _init_chromadb(self) -> Optional[Any]:
        """Initialize ChromaDB"""
        if not CHROMA_AVAILABLE:
            return None
        
        try:
            client = chromadb.PersistentClient(path=self.persist_directory)
            return client
        except Exception as e:
            print(f"ChromaDB error: {e}")
            return None
    
    def _load_simple_store(self):
        """Load simple backup storage"""
        store_path = os.path.join(self.persist_directory, 'simple_store.json')
        
        if os.path.exists(store_path):
            try:
                with open(store_path, 'r', encoding='utf-8') as f:
                    self.simple_store = json.load(f)
                    return
            except:
                pass
        
        self.simple_store = {cat: [] for cat in self.categories}
    
    def _save_simple_store(self):
        """Save simple backup storage"""
        store_path = os.path.join(self.persist_directory, 'simple_store.json')
        try:
            with open(store_path, 'w', encoding='utf-8') as f:
                json.dump(self.simple_store, f, indent=2)
        except Exception as e:
            print(f"Save error: {e}")
    
    def add_document(self, content: str, category: str, metadata: Optional[Dict] = None) -> str:
        """Add document to knowledge base"""
        if category not in self.categories:
            category = 'general'
        
        doc_id = f"{category}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        
        # Add to vector store if available
        if self.client and self.embedding_model and category in self.collections:
            try:
                embedding = self.embedding_model.encode(content).tolist()
                self.collections[category].add(
                    embeddings=[embedding],
                    documents=[content],
                    metadatas=[metadata or {}],
                    ids=[doc_id]
                )
            except Exception as e:
                print(f"Vector add error: {e}")
        
        # Always add to simple store as backup
        self.simple_store[category].append({
            'id': doc_id,
            'content': content,
            'category': category,
            'metadata': metadata or {},
            'added_at': datetime.now().isoformat()
        })
        self._save_simple_store()
        
        return doc_id
    
    def search(self, query: str, category: Optional[str] = None, top_k: int = 3) -> List[Dict[str, Any]]:
        """Search knowledge base"""
        
        # Try vector search first
        if self.client and self.embedding_model:
            try:
                return self._vector_search(query, category, top_k)
            except Exception as e:
                print(f"Vector search error: {e}")
        
        # Fallback to keyword search
        return self._keyword_search(query, category, top_k)
    
    def _vector_search(self, query: str, category: Optional[str], top_k: int) -> List[Dict[str, Any]]:
        """Vector similarity search"""
        query_embedding = self.embedding_model.encode(query).tolist()
        results = []
        
        categories = [category] if category else self.categories
        
        for cat in categories:
            if cat in self.collections:
                try:
                    cat_results = self.collections[cat].query(
                        query_embeddings=[query_embedding],
                        n_results=top_k
                    )
                    
                    if cat_results['documents'] and cat_results['documents'][0]:
                        for i, doc in enumerate(cat_results['documents'][0]):
                            results.append({
                                'content': doc,
                                'category': cat,
                                'score': 1.0 - (cat_results['distances'][0][i] if cat_results.get('distances') else 0),
                                'metadata': cat_results['metadatas'][0][i] if cat_results.get('metadatas') else {}
                            })
                except Exception as e:
                    print(f"Category {cat} search error: {e}")
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def _keyword_search(self, query: str, category: Optional[str], top_k: int) -> List[Dict[str, Any]]:
        """Simple keyword search fallback"""
        query_words = set(query.lower().split())
        results = []
        
        categories = [category] if category else self.categories
        
        for cat in categories:
            for doc in self.simple_store.get(cat, []):
                content_words = set(doc['content'].lower().split())
                matches = len(query_words & content_words)
                
                if matches > 0:
                    score = matches / len(query_words)
                    results.append({
                        'content': doc['content'],
                        'category': cat,
                        'score': score,
                        'metadata': doc.get('metadata', {})
                    })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get knowledge base stats"""
        stats = {
            'total_documents': 0,
            'by_category': {},
            'vector_enabled': bool(self.client),
            'embeddings_enabled': bool(self.embedding_model)
        }
        
        for cat in self.categories:
            count = len(self.simple_store.get(cat, []))
            stats['by_category'][cat] = count
            stats['total_documents'] += count
        
        return stats
