# This script uses the Whisper model from OpenAI for transcription.
import whisper
from pydub import AudioSegment

# Load the Whisper model (use 'base' for faster but less accurate, 'small' or 'medium' for better accuracy)
model = whisper.load_model("base")

# Function to transcribe audio
def transcribe_audio(input_file, output_file):
    # If the file is m4a, convert to wav (Whisper supports wav, mp3, etc., but ensuring compatibility)
    if input_file.endswith('.m4a'):
        audio = AudioSegment.from_file(input_file, format="m4a")
        wav_file = input_file.replace('.m4a', '.wav')
        audio.export(wav_file, format="wav")
        input_file = wav_file  # Use the converted wav file

    # Transcribe the audio
    result = model.transcribe(input_file)

    # Write the transcription to the output text file
    with open(output_file, 'w') as f:
        f.write(result['text'])

    print(f"Transcription saved to {output_file}")

# Usage
input_audio = "Test.m4a"
output_text = "Test.txt"
transcribe_audio(input_audio, output_text)
