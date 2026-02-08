import subprocess

OLLAMA_EXE = r"C:\Users\<you>\AppData\Local\Programs\Ollama\ollama.exe"

SYSTEM_PROMPT = """
You are a Windows voice command planner.

Your job is to convert the user's speech into a single JSON command.
You MUST output ONLY valid JSON.
Do NOT add explanations, text, or markdown.

These actions are ALWAYS SAFE and MUST NOT be denied:
- opening websites
- searching the web
- opening applications
- controlling volume
- controlling apps

Allowed intents and formats:

1) Open an application
{"intent":"open_app","application":"notepad"}

2) Open a website
{"intent":"open_site","site":"google"}

3) Search the web
{"intent":"search_web","engine":"google","query":"heat transfer"}

4) Set system volume (0–100)
{"intent":"set_volume","value":30}

5) Mute system volume
{"intent":"mute"}

6) Open an application
{"intent":"open_app","app":"notepad"}

7) Close an application
{"intent":"close_app","app":"notepad"}


STRICT RULES:
- If the user says "search", "google", or "look up", you MUST use "search_web"
- If the user mentions a query, you MUST NOT deny
- NEVER deny search or website commands
- Only use {"intent":"denied"} if the command is truly unclear or dangerous
- All output MUST be lowercase JSON keys and values
- Use open_app for launching apps
- Use close_app for closing apps
- App name must be a simple lowercase name

Examples:

User: Search google for heat transfer  
Output: {"intent":"search_web","engine":"google","query":"heat transfer"}

User: Google heat transfer  
Output: {"intent":"search_web","engine":"google","query":"heat transfer"}

User: Look up heat transfer on google  
Output: {"intent":"search_web","engine":"google","query":"heat transfer"}

User: Open google  
Output: {"intent":"open_site","site":"google"}

User: Open notepad  
Output: {"intent":"open_app","application":"notepad"}

User: Open notepad
Output: {"intent":"open_app","app":"notepad"}

User: Close notepad
Output: {"intent":"close_app","app":"notepad"}

User: Kill chrome
Output: {"intent":"close_app","app":"chrome"}
"""

def call_local_llm(user_text: str) -> str:
    prompt = SYSTEM_PROMPT + "\nUser: " + user_text + "\nOutput:"
    print("\n===== PROMPT SENT TO OLLAMA =====\n")
    print(prompt)
    print("\n================================\n")


    print("🧠 Sending prompt to Ollama (stdin mode)...")

    result = subprocess.run(
    [OLLAMA_EXE, "run", "llama3:8b"],
    input=prompt,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore",   # <-- critical
    timeout=30
    )


    output = result.stdout.strip()

    # Some Ollama versions print to stderr
    if not output:
        output = result.stderr.strip()

    print("🧠 Ollama raw output:", output)
    return output
