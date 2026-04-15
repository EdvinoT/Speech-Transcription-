# Installation & Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install FFmpeg
Required for audio processing. Choose for your OS:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS (with Homebrew):**
```bash
brew install ffmpeg
```

**Windows:**
- Download from: https://ffmpeg.org/download.html
- Or use Chocolatey: `choco install ffmpeg`

Verify installation:
```bash
ffmpeg -version
```

### 3. Run the Application
```bash
python main.py
```

---

## Optional: Gemma 3B Local LLM Integration

For advanced text processing with a local Gemma model:

### Prerequisites
- Ollama: https://ollama.ai (Free download)
- 4-8GB RAM (for 7B model) or 2-4GB (for 2B model)

### Setup Gemma

1. **Install Ollama:**
   - Download from https://ollama.ai
   - Follow installation instructions for your OS

2. **Start Ollama Service:**
   ```bash
   # Ollama runs as a background service automatically on most OS
   # Verify it's running on localhost:11434
   ```

3. **Pull Gemma Model:**
   ```bash
   # For 7B model (better quality, needs more RAM)
   ollama pull gemma:7b
   
   # Or for 2B model (faster, lighter)
   ollama pull gemma:2b
   ```

4. **Verify Model Installation:**
   ```bash
   ollama list
   ```

### Using Gemma in Your Code

Optional integration is provided in `gemma_processor.py`:

```python
from gemma_processor import GemmaTextProcessor

# Initialize processor
gemma = GemmaTextProcessor()

# Enhance transcribed text
enhanced = gemma.process_text("your text here", task="enhance")

# Summarize
summary = gemma.process_text("long text", task="summarize")

# Fix grammar
corrected = gemma.process_text("text with errors", task="correct")

# Analyze sentiment
sentiment = gemma.sentiment_analysis("This is amazing!")

# Extract keywords
keywords = gemma.extract_keywords("some text content")
```

### Available Gemma Tasks
- **enhance**: Make text clearer and more engaging
- **summarize**: Condense text to key points
- **correct**: Fix grammar and spelling
- **expand**: Make text longer and more detailed

---

## Improvements Made to Your Code

### From Original:
- ❌ Limited to text-to-speech only
- ❌ No transcription capability
- ❌ No audio splicing
- ❌ Unused Gemma import
- ❌ Poor error handling
- ❌ No multi-source support

### To Enhanced Version:
✅ **Full Speech-to-Text**: Transcribe audio files to text
✅ **Text-to-Speech**: Synthesize any text to audio
✅ **Audio Splicing**: Combine multiple audio sources
✅ **Multi-Language**: Support for 9+ languages
✅ **Better Architecture**: Object-oriented with `SpeechProcessor` class
✅ **Error Handling**: Comprehensive exception handling
✅ **Multi-Source Mode**: Process text and audio together
✅ **Optional Gemma Integration**: Enhance text with local LLM
✅ **Clean UI**: Better user prompts and feedback

---

## Troubleshooting

### Issue: "No module named 'speech_recognition'"
```bash
pip install SpeechRecognition
```

### Issue: "ffmpeg not found"
```bash
# Linux
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from ffmpeg.org or use: choco install ffmpeg
```

### Issue: "ModuleNotFoundError: No module named 'pydub'"
```bash
pip install pydub
```

### Issue: Speech Recognition Returns Empty
- Check microphone input
- Try clearer audio with less background noise
- Ensure internet connection (uses Google API)
- Check audio file format is supported (MP3, WAV, FLAC, etc.)

### Issue: Gemma Not Connecting
- Check Ollama is running: `curl http://localhost:11434/api/tags`
- Restart Ollama service
- Ensure model is downloaded: `ollama list`
- Try: `ollama run gemma:7b`

### Issue: Audio Synthesis Fails
- Verify internet connection (gTTS requires internet)
- Check text is not empty
- Try shorter text first to test

---

## Performance Tips

1. **For Faster Audio Processing:**
   - Use MP3 format (faster than WAV)
   - Keep audio files under 30 seconds for quicker transcription

2. **For Faster Gemma Processing:**
   - Use 2B model instead of 7B (`ollama pull gemma:2b`)
   - Shorter text input processes faster

3. **For Better Speech Recognition:**
   - Use clear audio with minimal background noise
   - Keep file format in MP3 or WAV

4. **For Best Synthesis Quality:**
   - Use English language (fastest)
   - Set `slow=False` in gTTS for normal speed

---

## Resources

- **SpeechRecognition**: https://pypi.org/project/SpeechRecognition/
- **pydub**: https://pypi.org/project/pydub/
- **gTTS**: https://pypi.org/project/gTTS/
- **Ollama**: https://ollama.ai
- **Gemma Models**: https://ai.google.dev/gemma
- **FFmpeg**: https://ffmpeg.org

---

## Next Steps

1. Try the basic modes first (2 & 4)
2. Experiment with different languages
3. Test audio splicing with your files
4. Optionally integrate Gemma for text enhancement
5. Extend with your own features as needed

Enjoy! 🎉
