import os
import json

from dotenv import load_dotenv
from openai import OpenAI


# --------------------------------
# Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# OpenRouter client
# --------------------------------

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# --------------------------------
# Model
# --------------------------------

MODEL = "openai/gpt-oss-20b"


# --------------------------------
# Convert conversation
# --------------------------------

def convert_conversation(conversation):

    messages = []

    for message in conversation:

        role = message["role"]

        # -------------------------
        # User
        # -------------------------

        if role == "user":

            messages.append({
                "role": "user",
                "content": message["content"]
            })

        # -------------------------
        # Assistant
        # -------------------------

        elif role == "assistant":

            content = message.get("content")

            if isinstance(content, dict):
                content = json.dumps(content)

            messages.append({
                "role": "assistant",
                "content": content
            })

        # -------------------------
        # Tool result
        # -------------------------

        elif role == "tool":

            messages.append({
                "role": "tool",
                "tool_call_id": message.get("tool_call_id"),
                "content": message["content"]
            })

    return messages


# --------------------------------
# Convert tools
# --------------------------------

def convert_tools(tool_schemas):

    tools = []

    for tool in tool_schemas:

        function = tool["function"]

        tools.append({
            "type": "function",
            "function": {
                "name": function["name"],
                "description": function["description"],
                "parameters": function["parameters"]
            }
        })

    return tools


# --------------------------------
# Call OpenRouter
# --------------------------------

def call_llm(conversation, tool_schemas):

    messages = convert_conversation(
        conversation
    )

    tools = convert_tools(
        tool_schemas
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # --------------------------------
    # Check tool call
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
    # Final answer
    # --------------------------------

    return {
        "type": "final",
        "content": message.content.strip()
        if message.content
        else ""
    }