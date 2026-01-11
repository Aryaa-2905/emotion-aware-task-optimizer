import sounddevice as sd
import numpy as np
import librosa
from src.task_engine import emotion_based_action

SAMPLE_RATE = 22050
DURATION = 3  # seconds

def detect_audio_emotion(audio):
    rms = np.mean(librosa.feature.rms(y=audio))

    if rms < 0.01:
        return "sad"
    elif rms < 0.03:
        return "neutral"
    else:
        return "happy"

print("🎙️ Listening for audio emotion... Speak now!")

while True:
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    audio = audio.flatten()

    emotion = detect_audio_emotion(audio)
    action = emotion_based_action(emotion)

    print(f"Audio Emotion: {emotion} → Action: {action}")
