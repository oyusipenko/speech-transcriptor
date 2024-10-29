# Speech Transcriber

This application transcribes audio files and performs speaker diarization, outputting the result as a dialogue with speaker identification.

## Features

- **Audio Transcription**: Utilizes the WhisperX model for accurate transcription.
- **Speaker Diarization**: Identifies different speakers in the audio.
- **Formatted Output**: Saves the transcription with speaker labels in an organized format.

## Installation

### Prerequisites

- Python 3.7 or later
- Installed `ffmpeg`
- NVIDIA GPU with CUDA support (for acceleration)

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/speech-transcriber.git
   
2. **Navigate to the project directory:**

   ```bash
   cd speech-transcriber
   
3. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   
5. **Install ffmpeg (if not already installed):**

   ```bash
   sudo apt-get install ffmpeg
   
6. **Create a .env file and add your Hugging Face token:**

   ```bash
   HUGGING_FACE_TOKEN=your_token_here