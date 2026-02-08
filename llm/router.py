from llm.local_llm import call_local_llm

def get_intent(user_text: str) -> str:
    return call_local_llm(user_text)
