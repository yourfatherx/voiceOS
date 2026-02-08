import time
import executors.app_control as app_control
from executors.browser import open_site, search_web
import executors.system_control as system_control


def execute_step(step: dict):
    intent = step.get("intent")

    if intent == "open_app":
        app_control.open_app(step.get("app"))

    elif intent == "close_app":
        app_control.close_app(step.get("app"))

    elif intent == "open_site":
        open_site(step.get("site"))

    elif intent == "search_web":
        search_web(step.get("engine"), step.get("query"))

    elif intent == "set_volume":
        system_control.set_volume(step.get("value"))

    elif intent == "mute":
        system_control.mute()


def run_workflow(steps: list):
    print(f"🔁 Running workflow with {len(steps)} steps")

    for i, step in enumerate(steps, start=1):
        print(f"➡️ Step {i}: {step}")
        execute_step(step)
        time.sleep(0.7)  # small delay for stability
