"""
EXAMPLES & ADVANCED USAGE

This file demonstrates how to use the enhanced Speech Transcription tool
with various real-world scenarios.
"""

from main import SpeechProcessor
from gemma_processor import GemmaTextProcessor
import asyncio

# =============================================================================
# EXAMPLE 1: Basic Transcription + Translation + Synthesis
# =============================================================================
def example_1_complete_pipeline():
    """
    Scenario: You have a Spanish audio file and want to hear it in English
    """
    print("\n" + "="*60)
    print("EXAMPLE 1: Complete Pipeline")
    print("="*60)
    
    processor = SpeechProcessor()
    processor.language = 'en'  # Output language
    
    # 1. Transcribe Spanish audio
    text = processor.transcribe_audio("spanish_audio.mp3")
    
    # 2. Translate to English
    translated = asyncio.run(processor.translate_text(text, 'en'))
    
    # 3. Synthesize English speech
    processor.synthesize_speech(translated, "english_output.mp3")
    
    print("✓ Converted Spanish audio to English audio!")


# =============================================================================
# EXAMPLE 2: Multi-Source Podcast Creation
# =============================================================================
def example_2_podcast_creation():
    """
    Scenario: Create a podcast by combining intro, multiple segments, and outro
    """
    print("\n" + "="*60)
    print("EXAMPLE 2: Multi-Source Podcast Creation")
    print("="*60)
    
    processor = SpeechProcessor()
    processor.language = 'en'
    
    segments = []
    
    # Intro text
    print("[*] Creating intro...")
    intro_text = "Welcome to TechTalk Podcast. Today we discuss AI innovations."
    intro = processor.synthesize_speech(intro_text, "intro.mp3")
    segments.append(intro)
    
    # Add existing interview audio
    print("[*] Adding interview segment...")
    segments.append("interview_recording.mp3")  # Existing file
    
    # Add background music
    print("[*] Adding background music...")
    segments.append("background_music.mp3")  # Existing file
    
    # Outro text
    print("[*] Creating outro...")
    outro_text = "Thanks for listening! Subscribe for more episodes."
    outro = processor.synthesize_speech(outro_text, "outro.mp3")
    segments.append(outro)
    
    # Splice everything
    podcast = processor.splice_audio_files(segments, "complete_podcast.mp3")
    print(f"✓ Podcast created: {podcast}")


# =============================================================================
# EXAMPLE 3: Meeting Transcription + Summary
# =============================================================================
def example_3_meeting_transcription():
    """
    Scenario: Transcribe a meeting and summarize with Gemma
    """
    print("\n" + "="*60)
    print("EXAMPLE 3: Meeting Transcription + Summary")
    print("="*60)
    
    processor = SpeechProcessor()
    gemma = GemmaTextProcessor()
    
    # Transcribe meeting recording
    print("[*] Transcribing meeting...")
    meeting_text = processor.transcribe_audio("meeting_recording.mp3")
    
    if meeting_text and gemma.available:
        # Summarize with Gemma
        print("[*] Summarizing with Gemma...")
        summary = gemma.process_text(meeting_text, task="summarize")
        print(f"Summary: {summary}")
        
        # Extract key points
        keywords = gemma.extract_keywords(meeting_text)
        print(f"Key Topics: {', '.join(keywords)}")
        
        # Save results
        with open("meeting_summary.txt", "w") as f:
            f.write(f"Original Transcription:\n{meeting_text}\n\n")
            f.write(f"Summary:\n{summary}\n\n")
            f.write(f"Key Topics:\n{', '.join(keywords)}")
        
        print("✓ Meeting summary saved to meeting_summary.txt")
    else:
        print("⚠ Could not transcribe or Gemma not available")


# =============================================================================
# EXAMPLE 4: Text Enhancement with Gemma
# =============================================================================
def example_4_text_enhancement():
    """
    Scenario: Improve transcribed text quality using Gemma
    """
    print("\n" + "="*60)
    print("EXAMPLE 4: Text Enhancement with Gemma")
    print("="*60)
    
    processor = SpeechProcessor()
    gemma = GemmaTextProcessor()
    processor.language = 'en'
    
    # Poor quality transcription
    poor_text = "um the project is going good we have uh many things to do"
    print(f"Original: {poor_text}")
    
    if gemma.available:
        # Enhance the text
        enhanced = gemma.process_text(poor_text, task="enhance")
        print(f"Enhanced: {enhanced}")
        
        # Now synthesize the enhanced text
        processor.synthesize_speech(enhanced, "enhanced_output.mp3")
        print("✓ Synthesized enhanced text")
    else:
        processor.synthesize_speech(poor_text, "output.mp3")


# =============================================================================
# EXAMPLE 5: Multi-Language Content Creation
# =============================================================================
def example_5_multilingual():
    """
    Scenario: Create content in multiple languages from one script
    """
    print("\n" + "="*60)
    print("EXAMPLE 5: Multi-Language Content Creation")
    print("="*60)
    
    base_text = "Welcome to our product presentation"
    languages = ['en', 'es', 'fr', 'de']
    
    processor = SpeechProcessor()
    
    for lang in languages:
        processor.language = lang
        print(f"[*] Creating {lang} version...")
        
        # Translate
        translated = asyncio.run(processor.translate_text(base_text, lang))
        
        # Synthesize
        output_file = f"presentation_{lang}.mp3"
        processor.synthesize_speech(translated, output_file)
    
    print("✓ Multi-language versions created!")


# =============================================================================
# EXAMPLE 6: Smart Interview Processing
# =============================================================================
def example_6_interview_processing():
    """
    Scenario: Process an interview - transcribe, analyze sentiment, enhance, synthesize
    """
    print("\n" + "="*60)
    print("EXAMPLE 6: Smart Interview Processing")
    print("="*60)
    
    processor = SpeechProcessor()
    gemma = GemmaTextProcessor()
    processor.language = 'en'
    
    # Transcribe interview
    interview_text = processor.transcribe_audio("interview.mp3")
    
    if not interview_text:
        print("Could not transcribe interview")
        return
    
    print(f"\nTranscribed ({len(interview_text)} chars)")
    
    if gemma.available:
        # Analyze sentiment
        sentiment = gemma.sentiment_analysis(interview_text)
        print(f"Sentiment: {sentiment}")
        
        # Enhance for clarity
        enhanced = gemma.process_text(interview_text, task="enhance")
        print(f"\nEnhanced excerpt: {enhanced[:100]}...")
        
        # Extract key quotes
        keywords = gemma.extract_keywords(interview_text)
        print(f"Key Topics: {', '.join(keywords)}")
        
        # Create enhanced audio version
        processor.synthesize_speech(enhanced, "interview_enhanced.mp3")
        print("\n✓ Interview processed and enhanced!")


# =============================================================================
# EXAMPLE 7: Batch Transcription
# =============================================================================
def example_7_batch_transcription():
    """
    Scenario: Transcribe multiple audio files at once
    """
    print("\n" + "="*60)
    print("EXAMPLE 7: Batch Transcription")
    print("="*60)
    
    audio_files = [
        "recording_1.mp3",
        "recording_2.wav",
        "recording_3.mp3"
    ]
    
    processor = SpeechProcessor()
    
    transcriptions = {}
    for audio_file in audio_files:
        print(f"[*] Processing {audio_file}...")
        text = processor.transcribe_audio(audio_file)
        if text:
            transcriptions[audio_file] = text
    
    # Save all transcriptions
    with open("batch_transcriptions.txt", "w") as f:
        for filename, text in transcriptions.items():
            f.write(f"\n{'='*50}\n")
            f.write(f"File: {filename}\n")
            f.write(f"{'='*50}\n")
            f.write(f"{text}\n\n")
    
    print(f"✓ Transcribed {len(transcriptions)} files!")


# =============================================================================
# EXAMPLE 8: Voice Cloning Workflow (Advanced)
# =============================================================================
def example_8_voice_workflow():
    """
    Scenario: Extract speaking style from interview and apply to new text
    
    Note: This requires additional libraries like pyttsx3 with voice selection
    """
    print("\n" + "="*60)
    print("EXAMPLE 8: Voice Workflow (Advanced)")
    print("="*60)
    
    processor = SpeechProcessor()
    gemma = GemmaTextProcessor()
    processor.language = 'en'
    
    # Step 1: Transcribe source audio
    source_text = processor.transcribe_audio("speaker_sample.mp3")
    
    # Step 2: Analyze speaking style with Gemma
    if gemma.available:
        analysis = gemma.process_text(
            f"Analyze the communication style of this text for voice synthesis: {source_text}",
            task="enhance"
        )
        print(f"Style Analysis: {analysis}")
    
    # Step 3: Create new content in similar style
    new_script = "Please discuss the future of technology"
    if gemma.available:
        styled_text = gemma.process_text(
            f"Rewrite this in a professional conversational style: {new_script}",
            task="enhance"
        )
    else:
        styled_text = new_script
    
    # Step 4: Synthesize
    processor.synthesize_speech(styled_text, "styled_output.mp3")
    print("✓ Created content in target voice style!")


# =============================================================================
# EXAMPLE 9: Interactive Session
# =============================================================================
def example_9_interactive():
    """
    Scenario: Run an interactive session demonstrating all features
    """
    print("\n" + "="*60)
    print("EXAMPLE 9: Interactive Demo")
    print("="*60)
    
    processor = SpeechProcessor()
    processor.language_selection()
    processor.run()


# =============================================================================
# RUN EXAMPLES
# =============================================================================
if __name__ == "__main__":
    print("\n" + "🎤 " * 20)
    print("SPEECH TRANSCRIPTION - ADVANCED EXAMPLES")
    print("🎤 " * 20)
    
    examples = {
        "1": ("Complete Pipeline", example_1_complete_pipeline),
        "2": ("Podcast Creation", example_2_podcast_creation),
        "3": ("Meeting Transcription", example_3_meeting_transcription),
        "4": ("Text Enhancement", example_4_text_enhancement),
        "5": ("Multi-Language", example_5_multilingual),
        "6": ("Interview Processing", example_6_interview_processing),
        "7": ("Batch Transcription", example_7_batch_transcription),
        "8": ("Voice Workflow", example_8_voice_workflow),
        "9": ("Interactive Demo", example_9_interactive),
    }
    
    print("\nAvailable Examples:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    print("  0. Exit")
    
    choice = input("\nSelect example to run: ").strip()
    
    if choice == "0":
        print("Goodbye!")
    elif choice in examples:
        name, func = examples[choice]
        print(f"\n🚀 Running: {name}")
        try:
            func()
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Tip: Make sure required audio files exist in the current directory")
    else:
        print("Invalid choice")
