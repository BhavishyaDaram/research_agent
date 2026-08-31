from agent import Agent
from registry import ToolRegistry

from tools import (
    web_search_tool,
    fetch_page_tool,
    take_note_tool
)

def main():

    # -----------------------------
    # 1. Create Tool Registry
    # -----------------------------

    registry = ToolRegistry()

    # Register our research tools
    registry.register(web_search_tool)
    registry.register(fetch_page_tool)
    registry.register(take_note_tool)


    # -----------------------------
    # 2. Create Agent
    # -----------------------------

    agent = Agent(
        registry=registry,
        max_steps=3
    )


    # -----------------------------
    # 3. Get question from user
    # -----------------------------

    question = input(
        "\nEnter your research question: "
    )


    # -----------------------------
    # 4. Run the agent
    # -----------------------------

    answer = agent.run(question)


    # -----------------------------
    # 5. Print final answer
    # -----------------------------


    print(answer)


if __name__ == "__main__":
    main()