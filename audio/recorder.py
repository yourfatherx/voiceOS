import sounddevice as sd
import numpy as np
import wave
import time

SAMPLE_RATE = 16000
DURATION = 5  # seconds
CHANNELS = 1

#sd.default.device = 9
sd.default.samplerate = SAMPLE_RATE
sd.default.channels = CHANNELS

def record_audio(filename="input.wav"):
    print("🎤 Listening(5 seconds)...")

    frames = []

    def callback(indata, frames_count, time_info, status):
        if status:
            print("⚠️ Audio status:", status)
        frames.append(indata.copy())

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        callback=callback,
    ):
        time.sleep(DURATION)

    audio = np.concatenate(frames, axis=0)

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())

    print("✅ Audio recorded")
    return filename
