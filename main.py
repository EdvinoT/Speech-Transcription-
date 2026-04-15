from gtts import gTTS
from googletrans import Translator
import speech_recognition as sr
from pydub import AudioSegment
import os
import asyncio
from pathlib import Path

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese'
}

class SpeechProcessor:
    def __init__(self):
        self.language = 'en'
        self.audio_segments = []
        
    def language_selection(self):
        """Select target language for synthesis"""
        print("=" * 50)
        print("Welcome to Advanced Speech Transcription & Synthesis!")
        print("=" * 50)
        print("\nAvailable languages:")
        for code, name in SUPPORTED_LANGUAGES.items():
            print(f"  {code}: {name}")
        
        lang_input = input("\nEnter language code (e.g., 'en' for English): ").strip().lower()
        if lang_input in SUPPORTED_LANGUAGES:
            self.language = lang_input
            print(f"✓ Selected: {SUPPORTED_LANGUAGES[lang_input]}")
        else:
            print("Invalid selection. Defaulting to English.")
            self.language = 'en'
    
    def transcribe_audio(self, audio_path):
        """Transcribe audio file to text using speech recognition"""
        print(f"\n[*] Transcribing audio: {audio_path}")
        try:
            with sr.AudioFile(audio_path) as source:
                audio = recognizer.record(source)
            
            text = recognizer.recognize_google(audio)
            print(f"✓ Transcribed text: {text}")
            return text
        except sr.UnknownValueError:
            print("✗ Could not understand audio. Please try another file.")
            return None
        except sr.RequestError as e:
            print(f"✗ Error with speech recognition service: {e}")
            return None
    
    def text_input(self):
        """Get text input from user"""
        print("\n[*] Text Input Mode")
        print("Enter the text you want to convert to speech:")
        text = input("> ").strip()
        
        # Save to file
        with open("text.txt", "w") as f:
            f.write(text)
        
        return text
    
    async def translate_text(self, text, target_lang):
        """Translate text asynchronously"""
        print(f"\n[*] Translating to {SUPPORTED_LANGUAGES[target_lang]}...")
        try:
            result = translator.translate(text, dest_lang=target_lang)
            translated = result['text'] if isinstance(result, dict) else result
            print(f"✓ Translated: {translated}")
            return translated
        except Exception as e:
            print(f"✗ Translation error: {e}. Using original text.")
            return text
    
    def synthesize_speech(self, text, output_file="output.mp3"):
        """Convert text to speech"""
        print(f"\n[*] Synthesizing speech...")
        try:
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save(output_file)
            print(f"✓ Audio saved: {output_file}")
            return output_file
        except Exception as e:
            print(f"✗ Error in synthesis: {e}")
            return None
    
    def splice_audio_files(self, audio_files, output_file="spliced_output.mp3"):
        """Combine multiple audio files"""
        print(f"\n[*] Splicing {len(audio_files)} audio files...")
        try:
            combined = AudioSegment.empty()
            
            for i, audio_file in enumerate(audio_files, 1):
                if not Path(audio_file).exists():
                    print(f"⚠ File not found: {audio_file}")
                    continue
                
                # Detect format and load
                ext = Path(audio_file).suffix.lower()
                audio = AudioSegment.from_file(audio_file, format=ext[1:])
                combined += audio
                print(f"  ✓ Added segment {i}: {audio_file}")
            
            # Export combined audio
            combined.export(output_file, format="mp3")
            print(f"✓ Spliced audio saved: {output_file}")
            return output_file
        except Exception as e:
            print(f"✗ Error splicing audio: {e}")
            return None
    
    def process_multiple_sources(self):
        """Process multiple audio/text sources and splice together"""
        print("\n" + "=" * 50)
        print("Multi-Source Processing Mode")
        print("=" * 50)
        
        segments = []
        
        while True:
            print("\nWhat do you want to add?")
            print("1. Text (will be synthesized)")
            print("2. Audio file (existing)")
            print("3. Finish and splice")
            
            choice = input("Enter choice (1-3): ").strip()
            
            if choice == '1':
                text = input("Enter text: ").strip()
                if text:
                    output_file = f"segment_{len(segments)}.mp3"
                    self.synthesize_speech(text, output_file)
                    segments.append(output_file)
            
            elif choice == '2':
                audio_file = input("Enter audio file path: ").strip()
                if Path(audio_file).exists():
                    segments.append(audio_file)
                    print(f"✓ Added: {audio_file}")
                else:
                    print("✗ File not found.")
            
            elif choice == '3':
                if segments:
                    return self.splice_audio_files(segments)
                else:
                    print("✗ No segments added.")
            
            else:
                print("Invalid choice.")
    
    def run(self):
        """Main execution flow"""
        self.language_selection()
        
        print("\n" + "=" * 50)
        print("Select Mode:")
        print("=" * 50)
        print("1. Transcribe audio file to text")
        print("2. Text to speech (manual input)")
        print("3. Process multiple sources (splice audio)")
        print("4. Combined: Transcribe + Translate + Synthesize")
        
        mode = input("Enter mode (1-4): ").strip()
        
        if mode == '1':
            # Transcription mode
            audio_path = input("Enter audio file path: ").strip()
            text = self.transcribe_audio(audio_path)
            if text:
                with open("transcribed_text.txt", "w") as f:
                    f.write(text)
                print("✓ Transcription saved to transcribed_text.txt")
        
        elif mode == '2':
            # Text to speech
            text = self.text_input()
            translated = asyncio.run(self.translate_text(text, self.language))
            self.synthesize_speech(translated)
        
        elif mode == '3':
            # Multi-source splicing
            self.process_multiple_sources()
        
        elif mode == '4':
            # Complete pipeline
            audio_path = input("Enter audio file to transcribe: ").strip()
            text = self.transcribe_audio(audio_path)
            
            if text:
                translated = asyncio.run(self.translate_text(text, self.language))
                self.synthesize_speech(translated)
        
        else:
            print("Invalid mode.")

# Clear screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Run the application
if __name__ == "__main__":
    processor = SpeechProcessor()
    processor.run()