from sarvamai import SarvamAI
import os

# 🔐 API key should be set as environment variable:
# setx SARVAM_API_KEY "sk_..."
client = SarvamAI(api_subscription_key="your key")

def transcribe(audio_file: str) -> str:
    """
    Transcribe speech from audio file.
    - Supports Hindi + English
    - Always returns English text
    - Drop-in replacement for whisper_stt.transcribe
    """

    if not audio_file:
        return ""

    print("🧠 Transcribing (SarvamAI)...")

    # 1️⃣ Speech → Text (Hindi / English)
    with open(audio_file, "rb") as audio:
        stt_result = client.speech_to_text.transcribe(
            file=audio,
            model="saarika:v2.5"
        )

    transcript = (
        stt_result.get("transcript", "")
        if isinstance(stt_result, dict)
        else getattr(stt_result, "transcript", "")
    )

    transcript = transcript.strip()

    if not transcript:
        print("📝 Transcript: <empty>")
        return ""

    # 2️⃣ Translate Hindi → English
    translation_result = client.text.translate(
        input=transcript,
        source_language_code="hi-IN",
        target_language_code="en-IN",
        speaker_gender="Male"
    )

    final_text = (
        translation_result.get("translated_text", "")
        if isinstance(translation_result, dict)
        else getattr(translation_result, "translated_text", "")
    )

    final_text = final_text.strip().lower()

    print("📝 Transcript:", final_text)
    return final_text
