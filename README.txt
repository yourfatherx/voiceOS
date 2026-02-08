VOICEOS — WINDOWS VOICE COMMAND ASSISTANT
===================================

VoiceOS is a command-based Windows voice assistant that lets you control
your system using natural speech. It listens to your voice, understands
your intent, and safely executes OS-level actions such as opening apps,
searching the web, and controlling system volume.

This project is NOT a chatbot and does NOT type into applications.
It follows Windows security boundaries and uses safe command execution.

--------------------------------------------------
FEATURES
--------------------------------------------------

• Open and close applications
  - “Open notepad”
  - “Close calculator”

• Search the web
  - “Search google for BITS Pilani”

• System volume control
  - “Set system volume to 30”
  - “Mute system”

• Multilingual speech input
  - Hindi + English (Hinglish supported)

• Hotkey-based voice trigger
  - Press Ctrl + Space to speak

--------------------------------------------------
HOW IT WORKS
--------------------------------------------------

Voice Input
  ↓
Speech-to-Text (Sarvam AI)
  ↓
Intent Planning (Local LLM via Ollama)
  ↓
Command Router
  ↓
Safe OS Executors

No unsafe keyboard injection
No UI automation
No admin privileges required

--------------------------------------------------
SYSTEM REQUIREMENTS
--------------------------------------------------

• Windows 10 or Windows 11
• Python 3.10 – 3.12
• Working microphone
• Internet connection (for Sarvam STT)
• Ollama installed locally

--------------------------------------------------
INSTALLATION STEPS
--------------------------------------------------

1) Clone the repository
   git clone https://github.com/yourfatherx/voiceOS.git
   cd voiceos

2) Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate

3) Install dependencies
   pip install -r requirements.txt

4) Install Ollama
   Download from: https://ollama.com
   Then run:
   ollama pull llama3:8b-instruct

5) Set environment variables
   Create a file named .env in the project root:

   SARVAM_API_KEY=your_api_key_here

--------------------------------------------------
RUNNING VOICEOS
--------------------------------------------------

Start the application:
   python main.py

You should see:
   VoiceOS running. Press Ctrl+Space to speak.

Usage:
1) Press Ctrl + Space
2) Speak a command
3) Wait for execution

--------------------------------------------------
EXAMPLE COMMANDS
--------------------------------------------------

• Open notepad
• Close calculator
• Search google for heat transfer
• Set system volume to 40
• Mute system
• Notepad kholo
• Google pe IIT Bombay search karo

--------------------------------------------------
PROJECT STRUCTURE (SIMPLIFIED)
--------------------------------------------------

voiceos/
├── audio/        Microphone recording
├── stt/          Speech-to-text modules
├── llm/          Local LLM intent planner
├── planner/      JSON intent parser
├── executors/    OS command executors
├── hotkey/       Global hotkey handler
├── main.py
└── voice_runner.py

--------------------------------------------------
LIMITATIONS (BY DESIGN)
--------------------------------------------------

• Does NOT type into text fields
• Does NOT control mouse or UI
• Executes one command per voice input
• Requires internet for speech recognition

These choices ensure stability and security.

--------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------

Microphone not working:
• Check Windows microphone permissions
• Ensure correct input device is default

Browser not opening:
• Set a default browser in Windows settings
• Test:
  python -c "import webbrowser; webbrowser.open('https://google.com')"

Ollama issues:
• Ensure Ollama is running
• Verify the model is installed

--------------------------------------------------
SECURITY & PRIVACY
--------------------------------------------------

• No background listening
• No keystroke injection
• No cloud LLM execution
• Commands are validated before execution


--------------------------------------------------
FINAL NOTE
--------------------------------------------------

VoiceOS demonstrates real-world voice-driven system control
using safe, deterministic execution.

If you find it useful, consider starring the repository.
