from __future__ import division
from google.cloud import speech
import os
import base64
import io

os.system("cd /tmp/")
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= '/tmp/paramount-371207-4576b089b156.json'

def main(args):
  try:
    client = speech.SpeechClient()
    content=args.get("audio")
    with open("result.wav", "wb") as fh:
      fh.write(base64.b64decode(content))
    with io.open("result.wav", "rb") as audio_file:
      content = audio_file.read()
    lang=args.get("lang")
    audio = speech.RecognitionAudio(content=content)
    config= speech.RecognitionConfig(
    enable_automatic_punctuation=True,
    language_code=lang,
    audio_channel_count=2)
    response = client.recognize(config=config, audio=audio)
    return {"body": str(response)}
  except Exception as E:
    return {"body":str(E)}
