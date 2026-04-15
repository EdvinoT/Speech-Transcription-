# Advanced Speech Transcription & Synthesis Tool

A comprehensive Python tool for audio transcription, text-to-speech synthesis, and multi-source audio splicing with multi-language support.

## Features

✨ **Speech-to-Text Transcription**: Convert audio files to text using Google's speech recognition
🎤 **Text-to-Speech Synthesis**: Convert text to audio with multiple language support
🔗 **Audio Splicing**: Combine multiple audio files seamlessly
🌍 **Multi-Language Translation**: Translate text between 9 languages
📦 **Multi-Source Processing**: Process and splice multiple text and audio sources together
🎯 **Clean Object-Oriented Design**: Maintainable and extensible codebase

## Installation

### Prerequisites
- Python 3.7+
- `ffmpeg` (required for audio processing)

### Setup on Ubuntu/Debian
```bash
# Install ffmpeg
sudo apt-get install ffmpeg

# Install Python dependencies
pip install -r requirements.txt
```

### Setup on macOS
```bash
# Install ffmpeg
brew install ffmpeg

# Install Python dependencies
pip install -r requirements.txt
```

### Setup on Windows
```bash
# Install ffmpeg (using chocolatey)
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html

# Install Python dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python main.py
```

### Operation Modes

#### 1. **Transcribe Audio File to Text**
- Select mode: `1`
- Enter path to audio file (MP3, WAV, FLAC, etc.)
- Output: Text transcription saved to `transcribed_text.txt`

#### 2. **Text-to-Speech Synthesis**
- Select mode: `2`
- Enter text you want to convert
- Specify target language
- Output: Audio file `output.mp3`

#### 3. **Multi-Source Audio Splicing**
- Select mode: `3`
- Add multiple text segments (auto-synthesized) or audio files
- Choose finish to splice all segments
- Output: Combined audio file `spliced_output.mp3`

#### 4. **Complete Pipeline** (Transcribe → Translate → Synthesize)
- Select mode: `4`
- Provide audio file
- System transcribes → translates → synthesizes in target language

## Supported Languages

- **en**: English
- **es**: Spanish
- **fr**: French
- **de**: German
- **it**: Italian
- **pt**: Portuguese
- **ja**: Japanese
- **ko**: Korean
- **zh**: Chinese

## Project Structure

```
Speech-Transcription-/
├── main.py                    # Main application
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── text.txt                   # User input text (generated)
├── transcribed_text.txt       # Transcription output (generated)
├── output.mp3                 # Synthesis output (generated)
└── spliced_output.mp3         # Spliced audio output (generated)
```

## Key Functions

### `SpeechProcessor` Class

**`transcribe_audio(audio_path)`**
- Converts audio file to text
- Uses Google Speech Recognition API
- Returns: transcribed text string

**`synthesize_speech(text, output_file)`**
- Converts text to audio
- Uses Google Text-to-Speech (gTTS)
- Returns: output file path

**`splice_audio_files(audio_files, output_file)`**
- Combines multiple audio files into one
- Supports MP3, WAV, FLAC, and more
- Returns: combined audio file path

**`translate_text(text, target_lang)`**
- Translates text to target language
- Async operation for performance
- Returns: translated text

**`process_multiple_sources()`**
- Interactive mode for multi-source processing
- Allows mixing text and audio segments
- Automatically splices results

## Examples

### Example 1: Transcribe Audio
```bash
python main.py
# Select mode: 1
# Enter audio file: recording.wav
# Output: Transcription in transcribed_text.txt
```

### Example 2: Text to Speech in Spanish
```bash
python main.py
# Select language: es
# Select mode: 2
# Enter text: "Hola, mundo!"
# Output: Audio file output.mp3
```

### Example 3: Splice Multiple Audio Files
```bash
python main.py
# Select mode: 3
# Add segment 1: audio1.mp3 (text)
# Add segment 2: audio2.wav (file)
# Add segment 3: outro text (text)
# Finish and splice
# Output: spliced_output.mp3
```

## Troubleshooting

### "ffmpeg not found"
- Ensure FFmpeg is installed and in your PATH
- Verify: `ffmpeg -version`

### "Audio file not recognized"
- Ensure audio format is supported (MP3, WAV, FLAC, OGG, etc.)
- Try converting to MP3 first

### "Speech recognition failed"
- Check internet connection (Google Speech API requires internet)
- Try a clearer audio file
- Ensure audio quality is acceptable

### "Translation failed"
- Original text will be used as fallback
- Check internet connection

## Limitations

- Speech recognition works best with clear audio
- API rate limits apply for translation and synthesis
- Requires internet connection for Google APIs

## Future Enhancements

- Offline speech recognition (using Whisper or similar)
- Voice cloning with specific speaker characteristics
- Support for more languages and accents
- Local LLM integration (Gemma, Llama) for text preprocessing
- GUI interface with PyQt/Tkinter
- Advanced audio editing capabilities

## License

MIT License - Feel free to modify and use for your projects!