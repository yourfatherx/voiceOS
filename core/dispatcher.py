import queue

command_queue = queue.Queue()

def request_voice_run():
    command_queue.put("RUN_VOICE")
