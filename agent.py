from llm import call_llm
from registry import ToolRegistry


class Agent:

    def __init__(self, registry, max_steps=10):
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

            print(f"\n--- Step {step + 1} ---")

            # Send conversation + available tools to LLM
            response = call_llm(
                conversation,
                self.registry.get_schemas()
            )

            # --------------------------------
            # Check if LLM wants to use a tool
            # --------------------------------

            if response["type"] == "tool_call":

                tool_name = response["name"]
                arguments = response["arguments"]

                print(f"Tool: {tool_name}")
                print(f"Arguments: {arguments}")

                # Execute the requested tool
                result = self.registry.execute(
                    tool_name,
                    arguments
                )

                print(f"Tool Result: {result}")

                # Send tool request to conversation
                conversation.append({
                    "role": "assistant",
                    "content": response
                })

                # Send tool result back to LLM
                conversation.append({
                    "role": "tool",
                    "content": str(result)
                })

            # --------------------------------
            # LLM has produced final answer
            # --------------------------------

            else:

                print("\nAgent finished.")

                return response["content"]

        # --------------------------------
        # Maximum steps reached
        # --------------------------------

        return "Agent stopped because maximum steps were reached."
    