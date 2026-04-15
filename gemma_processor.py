"""
Optional Gemma 3B Integration Module
Use this for local text processing and enhancement with Gemma 3B LLM

Installation:
1. Install ollama: https://ollama.ai
2. Run: ollama run gemma:7b (or gemma:2b for smaller)
3. Ensure ollama service is running on localhost:11434
"""

import requests
import json

class GemmaTextProcessor:
    """Optional: Process and enhance text using local Gemma 3B model"""
    
    def __init__(self, model_name="gemma:7b", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self.available = self.check_connection()
    
    def check_connection(self):
        """Check if Gemma model is available locally"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def process_text(self, text, task="enhance"):
        """
        Process text with Gemma 3B
        Tasks: 'enhance', 'summarize', 'correct', 'expand'
        """
        if not self.available:
            print("⚠ Gemma model not available. Ensure ollama is running.")
            return text
        
        prompts = {
            "enhance": f"Make this text clearer and more engaging: {text}",
            "summarize": f"Summarize this in 1-2 sentences: {text}",
            "correct": f"Fix grammar and spelling: {text}",
            "expand": f"Expand this into a full paragraph: {text}"
        }
        
        prompt = prompts.get(task, prompts["enhance"])
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", text).strip()
            else:
                print(f"✗ Error: {response.status_code}")
                return text
        except Exception as e:
            print(f"✗ Gemma processing error: {e}")
            return text
    
    def sentiment_analysis(self, text):
        """Analyze sentiment of text"""
        if not self.available:
            return None
        
        prompt = f"Analyze the sentiment of this text and respond with only: positive, negative, or neutral. Text: {text}"
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "").strip().lower()
            return None
        except Exception as e:
            print(f"✗ Sentiment analysis error: {e}")
            return None
    
    def extract_keywords(self, text):
        """Extract important keywords from text"""
        if not self.available:
            return []
        
        prompt = f"Extract 5 important keywords from this text. Return only comma-separated words: {text}"
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                keywords = result.get("response", "").strip()
                return [k.strip() for k in keywords.split(",")]
            return []
        except Exception as e:
            print(f"✗ Keyword extraction error: {e}")
            return []


# Example usage in main.py:
"""
from gemma_processor import GemmaTextProcessor

# In SpeechProcessor class, add:
def __init__(self):
    ...
    self.gemma = GemmaTextProcessor()
    
# Then use it:
def enhance_transcription(self, text):
    if self.gemma.available:
        enhanced = self.gemma.process_text(text, task="enhance")
        print(f"Enhanced text: {enhanced}")
        return enhanced
    return text
"""
