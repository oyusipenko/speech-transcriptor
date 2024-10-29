import os
import subprocess
import whisperx
import torch
from dotenv import load_dotenv


load_dotenv()
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")


torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.allow_tf32 = False


def convert_audio_to_mono(audio_file, output_file="temp_mono.wav"):
    try:
        subprocess.run([
            "ffmpeg", "-i", audio_file,
            "-ac", "1",
            "-ar", "16000",
            output_file,
            "-y"
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error during converting: {e}")
        raise


def transcribe_and_format_dialogue(audio_file):
    try:
        model = whisperx.load_model("large", device="cuda")

        mono_audio_file = convert_audio_to_mono(audio_file)

        transcription_result = model.transcribe(mono_audio_file)

        diarize_model = whisperx.DiarizationPipeline(use_auth_token=HUGGING_FACE_TOKEN)
        diarization_segments = diarize_model(mono_audio_file)

        formatted_text = []

        for d in diarization_segments.itertuples():
            speaker_text = [segment["text"] for segment in transcription_result["segments"]
                            if d.start <= segment["start"] < d.end]
            if speaker_text:
                speaker = f"Speaker {d.speaker}"
                text = " ".join(speaker_text)
                formatted_text.append(f"{speaker}: {text}")

        os.remove(mono_audio_file)

        return "\n".join(formatted_text)

    except Exception as e:
        print(f"Error: {e}")
        raise
