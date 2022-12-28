from __future__ import division
from google.cloud import speech
from google.cloud import translate

def main(args):
    client = speech.SpeechClient()
    content=args.get("audio")
    lang=args.get("lang")
    audio = speech.RecognitionAudio(content=content)
    config= speech.RecognitionConfig(
    enable_automatic_punctuation=True,
    language_code=lang,
    audio_channel_count=2
)
    response = client.recognize(config=config, audio=audio)
    return response
