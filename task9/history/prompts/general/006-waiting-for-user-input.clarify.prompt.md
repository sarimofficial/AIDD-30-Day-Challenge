---
id: 006
title: Waiting for User Input
stage: clarify
date: 2025-12-06
surface: agent
model: gemini-1.5-flash-latest
feature: none
branch: unknown
user: user
command: System: Please continue.
labels: ["clarification", "waiting"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

System: Please continue.

## Response snapshot

I am waiting for your input to my previous question. I asked for the list of properties or fields that each "skill" should contain.

Once you provide those details, I can continue with the task.

## Outcome

- ✅ Impact: Clarified that I am blocked and waiting for user input.
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: awaiting user clarification
- 🧠 Reflection: The user asked me to "continue" when I was waiting for them. It was important to clearly and concisely state what information I need to unblock myself.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
