import json

ALLOWED_INTENTS = {
    "open_app",
    "open_site",
    "search_web",
    "set_volume",
    "mute",
    "open_app",
    "close_app",
    "open_site",
    "search_web",
    "set_volume",
    "mute",
}

def parse_llm_response(raw: str) -> dict:
    """
    Parse raw JSON output from LLM.
    Return {'intent':'denied'} ONLY if JSON is invalid
    or intent is not allowed.
    """

    if not raw or not raw.strip():
        return {"intent": "denied"}

    try:
        data = json.loads(raw.strip())
    except Exception as e:
        print("❌ JSON parse error:", e)
        return {"intent": "denied"}
    
     # 🔹 WORKFLOW CASE
    if "workflow" in data and isinstance(data["workflow"], list):
        validated_steps = []

        for step in data["workflow"]:
            intent = step.get("intent")
            if intent in ALLOWED_INTENTS:
                validated_steps.append(step)

        if validated_steps:
            return {"workflow": validated_steps}
        else:
            return {"intent": "denied"}

     # 🔹 single intent CASE
    intent = data.get("intent")

    if intent not in ALLOWED_INTENTS:
        print("❌ Intent not allowed:", intent)
        return {"intent": "denied"}

    return data
