from llm import call_llm
from registry import ToolRegistry

class Agent:

    def __init__(self, registry, max_steps=2):
        self.registry = registry
        self.max_steps = max_steps

    def run(self, goal):

        conversation = [
            {
                "role": "user",
                "content": goal
            }
        ]

        for step in range(self.max_steps):

            response = call_llm(
                conversation,
                self.registry.get_schemas()
            )

            # --------------------------------
            # Tool call
            # --------------------------------

            if response["type"] == "tool_call":

                tool_name = response["name"]
                arguments = response["arguments"]
                tool_call_id = response["tool_call_id"]

                # Execute tool
                result = self.registry.execute(
                    tool_name,
                    arguments
                )

                # Add assistant tool call
                conversation.append({
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [
                        {
                            "id": tool_call_id,
                            "type": "function",
                            "function": {
                                "name": tool_name,
                                "arguments": str(arguments)
                            }
                        }
                    ]
                })

                # Add tool result
                conversation.append({
                    "role": "tool",
                    "tool_call_id": tool_call_id,
                    "content": str(result)
                })

            # --------------------------------
            # Final answer
            # --------------------------------

            else:

                return response["content"]

        return "Unable to complete the research."
