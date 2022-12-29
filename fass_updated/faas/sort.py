
from __future__ import division

import re
import sys
import os
import time

from google.cloud import speech
from google.cloud import translate

import pyaudio
from six.moves import queue
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'paramount-371207-4576b089b156.json'
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io

    client = speech.SpeechClient()

    print("starting")

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    print("started...............")
    audio = speech.RecognitionAudio(content=content)
    config= speech.RecognitionConfig(
    #sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US',
    audio_channel_count=2
)
    start=time.time()
    response = client.recognize(config=config, audio=audio)
    end=time.time()
    print(end-start)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print("Transcript: {}".format(result.alternatives[0].transcript))


transcribe_file("speech2.wav")