from agent import Agent
from registry import ToolRegistry

from tools import (
    web_search,
    fetch_page,
    take_note
)


def main():

    # -----------------------------
    # 1. Create Tool Registry
    # -----------------------------

    registry = ToolRegistry()

    # Register our research tools
    registry.register(web_search)
    registry.register(fetch_page)
    registry.register(take_note)


    # -----------------------------
    # 2. Create Agent
    # -----------------------------

    agent = Agent(
        registry=registry,
        max_steps=10
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

    print("\n" + "=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)

    print(answer)


if __name__ == "__main__":
    main()