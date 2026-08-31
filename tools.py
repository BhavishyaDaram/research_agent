import requests
from bs4 import BeautifulSoup
from ddgs import DDGS

from registry import Tool


# -------------------------
# Notes Storage
# -------------------------

notes = []


# -------------------------
# Web Search
# -------------------------

def web_search(query):

    try:

        results = DDGS().text(
            query,
            max_results=5
        )

        output = []

        for result in results:

            output.append({
                "title": result.get("title"),
                "url": result.get("href"),
                "snippet": result.get("body")
            })

        if not output:
            return "No search results found."

        return output

    except Exception as e:

        return f"Search error: {str(e)}"


# -------------------------
# Fetch Page
# -------------------------

def fetch_page(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for element in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header"
        ]):

            element.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:6000]

    except Exception as e:

        return f"Fetch error: {str(e)}"


# -------------------------
# Take Note
# -------------------------

def take_note(text, source_url):

    try:

        note = {
            "text": text,
            "source_url": source_url
        }

        notes.append(note)

        return "Note saved successfully."

    except Exception as e:

        return f"Note error: {str(e)}"


# =================================================
# TOOL DEFINITIONS
# =================================================

web_search_tool = Tool(

    name="web_search",

    description="Search the web for relevant information.",

    function=web_search,

    schema={
        "type": "object",

        "properties": {
            "query": {
                "type": "string",
                "description": "The search query."
            }
        },

        "required": ["query"]
    }
)


fetch_page_tool = Tool(

    name="fetch_page",

    description="Fetch and extract readable text from a webpage.",

    function=fetch_page,

    schema={
        "type": "object",

        "properties": {
            "url": {
                "type": "string",
                "description": "The URL of the webpage."
            }
        },

        "required": ["url"]
    }
)


take_note_tool = Tool(

    name="take_note",

    description="Save an important research finding together with its source URL.",

    function=take_note,

    schema={
        "type": "object",

        "properties": {
            "text": {
                "type": "string",
                "description": "The important information to save."
            },

            "source_url": {
                "type": "string",
                "description": "The URL where the information came from."
            }
        },

        "required": ["text", "source_url"]
    }
)