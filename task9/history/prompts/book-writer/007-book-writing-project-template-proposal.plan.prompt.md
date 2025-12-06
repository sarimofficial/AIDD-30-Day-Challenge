---
id: 007
title: Book Writing Project Template Proposal
stage: plan
date: 2025-12-06
surface: agent
model: gemini-1.5-flash-latest
feature: book-writer
branch: unknown
user: user
command: “Give me a ready-to-use project template where Skills handle reusable instructions and Sub-Agents handle specialized tasks in separate contexts, all working together to write a complete book.”
labels: ["new-project", "agentic-design", "planning"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

Ever

Ever

Ever

Ever

“Give me a ready-to-use project template where Skills handle reusable instructions and Sub-Agents handle specialized tasks in separate contexts, all working together to write a complete book.”

## Response snapshot

Of course. I will create a project template for a multi-agent system designed to write a book. The system will feature an orchestrator agent that manages specialized sub-agents (e.g., for research, outlining, writing, and editing). Reusable instructions, or "Skills," will be stored as simple text files that these agents can leverage.

Here is the plan:

*   **Application Type:** A Python-based command-line application that you can run to generate a book based on a predefined outline.
*   **Technology:** Python 3.
*   **Core Components:**
    1.  **Orchestrator Agent:** The main agent that reads the book's outline and manages the sub-agents to complete the writing process, chapter by chapter.
    2.  **Sub-Agents:** A collection of specialized agents for different tasks:
        *   **Research Agent:** Gathers information on a given topic (placeholder).
        *   **Outlining Agent:** Creates a detailed outline for a chapter.
        *   **Writing Agent:** Writes the chapter content based on the outline.
        *   **Editing Agent:** Edits the written content for grammar and style.
    3.  **Skills:** A library of reusable prompts (as `.txt` files) that can be loaded and used by any agent. For example, a skill could define a specific writing style.
    4.  **Book Outline:** A simple configuration file (`book_outline.yaml`) where you will define the chapters and topics of your book.
*   **Project Structure:** I will create the following file and directory structure:

    ```
    book_writer/
    ├── main.py                # Main entry point to run the system
    ├── book_outline.yaml      # Define your book's structure here
    ├── agents/
    │   ├── base_agent.py      # A base class for all agents
    │   ├── orchestrator.py    # The main conductor
    │   └── sub_agents/
    │       ├── research.py
    │       ├── outlining.py
    │       ├── writing.py
    │       └── editing.py
    ├── skills/
    │   ├── writing_styles/
    │   │   ├── academic.txt
    │   │   └── narrative.txt
    │   └── editing/
    │       └── proofread.txt
    └── output/                # Your generated book will appear here
    ```

Does this plan meet your requirements? Once you approve, I will proceed with creating this project structure and implementing the foundational code.

## Outcome

- ✅ Impact: Proposed a detailed plan for a new Python project as requested by the user.
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: Awaiting user approval of the plan.
- 🧠 Reflection: The user gave a complex request. I broke it down into a concrete plan with a clear project structure and explained the purpose of each component. This ensures alignment before I start building.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
