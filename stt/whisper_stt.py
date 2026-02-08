from faster_whisper import WhisperModel

# CPU-only, very stable
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"  # faster + compatible
)

def transcribe(audio_file: str) -> str:
    print("🧠 Transcribing (faster-whisper)...")

    segments, info = model.transcribe(audio_file)

    text = ""
    for segment in segments:
        text += segment.text

    text = text.strip()
    print("📝 Transcript:", text)
    return text
