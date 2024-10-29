import os
from datetime import datetime
from features.transcribe_audio import transcribe_and_format_dialogue

if __name__ == "__main__":
    audio_file = "input/untitled.wav"

    if not os.path.exists(audio_file):
        print(f"File {audio_file} was not found.")
        exit(1)

    try:
        transcription = transcribe_and_format_dialogue(audio_file)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"output/transcription_{timestamp}.txt"

        os.makedirs(os.path.dirname(output_filename), exist_ok=True)

        with open(output_filename, "w") as f:
            f.write(transcription)

        print(f"Transcription saved to {output_filename}")
    except Exception as e:
        print(f"Error: {e}")
