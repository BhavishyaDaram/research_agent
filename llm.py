import os
import json

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()


# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# Model
MODEL = "gpt-4.1-mini"


def call_llm(conversation, tool_schemas):

    # Convert our simple tool schemas
    # into OpenAI's tool format

    tools = []

    for tool in tool_schemas:

        tools.append({
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"]
            }
        })


    # Call the LLM
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
        tools=tools,
        tool_choice="auto"
    )


    message = response.choices[0].message


    # --------------------------------
    # Case 1: LLM wants to call a tool
    # --------------------------------

    if message.tool_calls:

        tool_call = message.tool_calls[0]

        return {
            "type": "tool_call",

            "name": tool_call.function.name,

            "arguments": json.loads(
                tool_call.function.arguments
            ),

            "tool_call_id": tool_call.id
        }


    # --------------------------------
    # Case 2: LLM gives final answer
    # --------------------------------

    return {
        "type": "final",

        "content": message.content
    }