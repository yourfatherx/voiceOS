from ui.notif import notify
from audio.recorder import record_audio
from stt.sarvam_stt import transcribe
from llm.router import get_intent
from planner.parser import parse_llm_response
from executors.volume import set_volume, mute
from executors.apps import open_app
from executors.native_keyboard import type_text, press_key
from executors.browser import open_site, search_web
import executors.app_control as app_control
import executors.system_control as system_control



def run_voice():
    print("🚀 run_voice entered")
    with open("VOICE_TRIGGERED.txt", "w") as f:
        f.write("run_voice was called\n")
        
    notify("VoiceOS", "🎤 Listening...")

    audio_file = record_audio("input.wav")
    print("📁 Audio file:", audio_file)
    text = transcribe(audio_file)
    print("📝 Transcript:", text)

    if not text.strip():
        notify("VoiceOS", "❌ Didn't catch that")
        return

    notify("VoiceOS", f"🗣️ {text}")

    llm_output = get_intent(text)
    command = parse_llm_response(llm_output)
    print("🧪 Parsed command dict:", command)
    print("🧪 Intent value:", command.get("intent"), type(command.get("intent")))


    print("🧭 ENTERED ROUTER")

    intent = command.get("intent")
    app_name = command.get("app")

    print("🧭 Intent:", intent)
    print("🧭 App name:", repr(app_name))

    if intent == "open_app":
        print("🧭 CALLING app_control.open_app")
        app_control.open_app(app_name)
        print("🧭 RETURNED FROM open_app")

    elif intent == "close_app":
        print("🧭 CALLING app_control.close_app")
        app_control.close_app(app_name)
        print("🧭 RETURNED FROM close_app")

    elif intent == "set_volume":
        value = command.get("value")
        print("🧭 Setting volume to:", value)
        system_control.set_volume(value)

    elif intent == "mute":
        system_control.mute()


    else:
        print("🚫 Intent not handled:", intent)

