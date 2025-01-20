import os
import wave
import numpy as np
from google.cloud import speech_v1
from google.cloud import storage

def process_audio(audio_file_path):
    """
    Process the audio file and return the transcription.
    """
    try:
        # Initialize the Speech-to-Text client
        client = speech_v1.SpeechClient()

        # Read the audio file
        with open(audio_file_path, 'rb') as audio_file:
            content = audio_file.read()

        # Configure the recognition settings
        audio = speech_v1.RecognitionAudio(content=content)
        config = speech_v1.RecognitionConfig(
            encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
            enable_automatic_punctuation=True,
        )

        # Perform the transcription
        response = client.recognize(config=config, audio=audio)

        # Extract the transcribed text
        transcription = ""
        for result in response.results:
            transcription += result.alternatives[0].transcript + " "

        return transcription.strip()

    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return None
