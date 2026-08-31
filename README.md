# Research Agent

**AI-Powered Automated Research System**

---

## 1. Overview

**Research Agent** is a Python-based, LLM-powered agent that automates the process of researching a topic on the web.

Instead of manually opening a search engine, browsing multiple websites, reading through pages, and compiling notes, this project lets a Large Language Model (LLM) do that work in an automated, structured way.

- **What the project is:** A command-line AI agent that takes a research query from the user and returns a synthesized, well-informed answer.
- **What problem it solves:** It removes the repetitive manual effort of searching, opening pages, and summarizing information from multiple sources.
- **What an AI agent does here:** The agent doesn't just answer from memory — it reasons about the query, decides which tool to use (search, fetch, or note-taking), executes that tool, observes the result, and repeats this cycle until it has enough information to answer.
- **Why an LLM is used:** The LLM acts as the "brain" of the system. It interprets the user's query, decides what action is needed next, and eventually synthesizes all gathered information into a final answer.
- **How tools are used:** The agent has access to a small set of tools (web search, page fetching, note-taking) that let it interact with the outside world, since an LLM alone cannot browse the internet.
- **What the final output is:** A synthesized, human-readable research response based on the information the agent gathered during its run.

---

## 2. Problem Statement

- **Traditional research is time-consuming.** Gathering information on a topic usually means running several searches, opening many tabs, and manually reading through each page.
- **Manually searching multiple websites is repetitive.** The same steps — search, open, skim, note down, repeat — are done over and over for every new query.
- **Limitations of a normal chatbot:** A standard chatbot answers only from what it already "knows" (its training data). It cannot browse the live web, verify current information, or actively decide to look something up.
- **Why an agentic workflow is useful:** An agentic approach allows the system to actively decide *when* it needs more information, *what* action to take to get it, and *how* to combine multiple pieces of information into a coherent answer — much closer to how a human researcher works.

---

## 3. Objectives

- Build an AI-powered Research Agent capable of automating web research.
- Integrate a Large Language Model (LLM) to drive reasoning and decision-making.
- Implement tool calling so the LLM can trigger real-world actions.
- Automate the process of gathering information from the web.
- Create a modular, maintainable project architecture.
- Implement a centralized tool registry for managing available tools.
- Add execution tracing for debugging and understanding agent behavior.
- Design the system to be easily extensible with new tools in the future.

---

## 4. Key Features

- **LLM-based reasoning** — the LLM decides what action the agent should take at each step.
- **Automated research workflow** — the agent handles search, retrieval, and synthesis without manual intervention.
- **Web search** — retrieves relevant results for a given query.
- **Webpage fetching** — retrieves the content of a specific webpage.
- **Note-taking** — stores important information found during research.
- **Tool registry** — centralizes and manages all available tools.
- **Agent workflow** — coordinates reasoning, tool execution, and response generation.
- **Execution tracing** — tracks the agent's steps for debugging.
- **Modular architecture** — each responsibility is separated into its own file.

---

## 5. System Architecture

```text
                         USER
                           │
                           ▼
                       main.py
                           │
                           ▼
                       agent.py
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
               llm.py          registry.py
                  │                 │
                  ▼                 ▼
               LLM API           tools.py
                                    │
                       ┌────────────┼────────────┐
                       ▼            ▼            ▼
                  Web Search    Fetch Page    Take Note
                       │            │            │
                       └────────────┼────────────┘
                                    ▼
                                  Agent
                                    │
                                    ▼
                              Final Response
```

**Component overview:**

- **main.py** — The entry point. Accepts the user's research query and displays the final response.
- **agent.py** — The core controller. Coordinates communication with the LLM, decides which tool to run, and processes results.
- **llm.py** — Handles all communication with the LLM (sending prompts, receiving responses).
- **registry.py** — Maintains a lookup of all available tools so the agent can find and call them by name.
- **tools.py** — Contains the actual tool implementations: `web_search()`, `fetch_page()`, and `take_note()`.
- **tracing.py** — Records the agent's execution steps for debugging and analysis.

---

## 6. Project Structure

```text
research_agent/
│
├── agent.py
├── llm.py
├── main.py
├── registry.py
├── tools.py
├── tracing.py
├── requirements.txt
├── .gitignore
└── README.md
```

| File                | Purpose                  |
|---------------------|---------------------------|
| `main.py`           | Application entry point   |
| `agent.py`          | Core agent workflow       |
| `llm.py`            | LLM communication         |
| `tools.py`          | Research tools            |
| `registry.py`       | Tool registration         |
| `tracing.py`        | Execution tracing         |
| `requirements.txt`  | Dependencies               |
| `.gitignore`        | Ignored files              |
| `README.md`         | Documentation               |

---

## 7. Code Flow

1. The user provides a research query.
2. `main.py` receives the query.
3. The query is passed to `agent.py`.
4. The agent communicates with the LLM through `llm.py`.
5. The LLM determines what action is required next.
6. The agent looks up the appropriate tool using `registry.py`.
7. The selected tool from `tools.py` is executed.
8. The tool returns its result to the agent.
9. The agent evaluates the result.
10. The agent may repeat the process to gather more information if needed.
11. All collected information is sent back to the LLM.
12. The LLM generates the final synthesized response.
13. The final response is returned to the user.

**Simplified flow:**

```text
User
 ↓
main.py
 ↓
agent.py
 ↓
llm.py
 ↓
LLM Decision
 ↓
registry.py
 ↓
tools.py
 ↓
Tool Result
 ↓
agent.py
 ↓
LLM Synthesis
 ↓
Final Answer
```

---

## 8. What Makes This an AI Agent?

It's useful to distinguish between three levels of software:

- **Traditional software** follows a fixed, predefined sequence of steps written by a developer. It cannot adapt its logic based on context.
- **A normal chatbot** responds to a query using only what it already knows from training. It has no ability to take actions or interact with external systems.
- **An AI agent** goes a step further: it reasons about a task, decides what action to take, executes that action using tools, observes the outcome, and continues reasoning until the task is complete.

Research Agent qualifies as an AI agent because it combines:

```text
Reasoning
    +
Tool Selection
    +
Tool Execution
    +
Observation
    +
Further Reasoning
    +
Final Response
```

This project only implements the functionality described above — no additional capabilities are assumed or exaggerated.

---

## 9. Tools

### Web Search
Searches for information relevant to the user's query and returns a set of results the agent can use to decide what to explore further.

### Fetch Page
Retrieves the content of a specific webpage so the agent can read and extract relevant details from it.

### Take Note
Stores important pieces of information discovered during the research process, so they can be used later when the LLM synthesizes the final response.

**Why tools are separated from agent logic:** Keeping tools in their own file (`tools.py`) keeps the agent's decision-making logic (`agent.py`) clean and independent from *how* each action is actually performed. This separation makes it easy to add, remove, or modify tools without touching the core agent logic.

---

## 10. Tool Registry

A **tool registry** is a centralized place where all available tools are registered and made accessible to the agent by name, rather than the agent needing to know about each tool individually.

**Why it's needed:**
- It decouples the agent's decision-making from the tool implementations.
- It allows the agent to look up and call a tool dynamically, based on what the LLM decides.
- It makes the architecture modular — tools can be added or removed without changing the agent's core logic.

**Conceptual example:**

```text
"web_search" → web_search()
"fetch_page" → fetch_page()
"take_note"  → take_note()
```

*Note: This is a conceptual illustration of how the registry maps tool names to functions, not a description of exact internal implementation details.*

---

## 11. Tracing

**Tracing** refers to recording the steps the agent takes while processing a research query — such as which tool was called, in what order, and what the outcome was.

**Why it's useful:**
- It provides visibility into the agent's decision-making process.
- It helps identify where something went wrong if the agent produces an unexpected result.
- It makes the agent's behavior easier to understand, both for development and for demonstration purposes.

Tracing is implemented in `tracing.py` and is used to track the execution flow of the agent.

---

## 12. Technologies Used

- Python
- Large Language Models (LLMs)
- LLM API
- Web Search
- Tool Calling
- Git
- GitHub

*Additional libraries should be listed here based on the actual contents of `requirements.txt`.*

---

## 13. Installation

```bash
git clone <repository-url>
cd research_agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (activation step):**

```bash
venv\Scripts\activate
```

---

## 14. Environment Variables

API keys and other sensitive credentials should be stored in a `.env` file, never hardcoded in the source code.

Example `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

**Important:**
- Never hardcode API keys directly in your source code.
- Never commit your `.env` file to GitHub.
- Make sure `.env` is listed in `.gitignore`.

---

## 15. How to Run

```bash
python3 main.py
```

Once running, enter your research query when prompted, and the agent will process it and return a final response.

---

## 16. Example Workflow

**Example research question:**

> "What are the latest developments in Generative AI?"

**Processing flow:**

```text
Research Question
       ↓
LLM Reasoning
       ↓
Web Search
       ↓
Search Results
       ↓
Fetch Relevant Pages
       ↓
Take Notes
       ↓
LLM Synthesis
       ↓
Final Research Response
```

*This is an example workflow illustrating the general process. It reflects only the functionality actually implemented in the project.*

---

## 17. Advantages

- Reduces manual research effort.
- Automates repetitive search-and-read tasks.
- Modular, maintainable architecture.
- Extensible tool system for future additions.
- LLM-based reasoning for more context-aware decisions.
- Ability to retrieve external, up-to-date information.
- Easier debugging through execution tracing.

---

## 18. Limitations

- No advanced source verification — information is not automatically fact-checked against multiple sources.
- No formal citation handling — sources are not automatically formatted or cited in the final response.
- Basic error handling — edge cases (e.g., failed requests, unreachable pages) may not be handled comprehensively.
- Webpage content extraction may not work well on all types of websites (e.g., heavily JavaScript-rendered pages).
- No persistent memory — the agent does not retain information across separate runs.
- No built-in mechanism to evaluate research quality or completeness.

---

## 19. Future Enhancements

*The following are potential future improvements, not currently implemented features:*

- Better source citation and reference formatting.
- Automated source verification.
- Persistent memory across sessions.
- Support for PDF and document-based research.
- A Streamlit-based user interface.
- More robust error handling.
- Automated research quality evaluation.
- Multi-agent architecture for more complex research tasks.

---

## 20. Learning Outcomes

This project demonstrates:

- Modular Python project architecture.
- Integration of an LLM into an application.
- Core concepts of AI agents.
- Implementation of tool calling.
- API integration with an LLM provider.
- Design and use of agentic workflows.
- Tool registry design patterns.
- Debugging and tracing techniques.
- Practical Git and GitHub usage.

