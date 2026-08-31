import json
from datetime import datetime


class Tracer:

    def __init__(self, filename="trace.jsonl"):
        self.filename = filename

    def log(self, event_type, data):
        event = {
            "timestamp": datetime.now().isoformat(),
            "event": event_type,
            "data": data
        }

        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(
                json.dumps(event) + "\n"
            )

    def log_agent_start(self, goal):
        self.log(
            "agent_start",
            {
                "goal": goal
            }
        )

    def log_llm_call(self, step):
        self.log(
            "llm_call",
            {
                "step": step
            }
        )

    def log_tool_call(self, step, tool_name, arguments):
        self.log(
            "tool_call",
            {
                "step": step,
                "tool": tool_name,
                "arguments": arguments
            }
        )

    def log_tool_result(self, step, tool_name, result):
        self.log(
            "tool_result",
            {
                "step": step,
                "tool": tool_name,
                "result": str(result)
            }
        )

    def log_final_answer(self, answer):
        self.log(
            "final_answer",
            {
                "answer": answer
            }
        )

    def log_error(self, error):
        self.log(
            "error",
            {
                "error": str(error)
            }
        )
    