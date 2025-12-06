---
id: 003
title: Unclear User Input
stage: general
date: 2025-12-06
surface: agent
model: gemini-1.5-flash-latest
feature: none
branch: unknown
user: user
command: Unclear input
labels: ["error-handling", "clarification"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

Ins

Ins

Ins

Ins

Ins

InsC

C

C

C

C

C

C

C

## Response snapshot

I didn't understand that input. Could you please clarify what you'd like to do?

## Outcome

- ✅ Impact: Prompted user for clarification on an unrecognized command.
- 🧪 Tests: N/A
- 📁 Files: None
- 🔁 Next prompts: Awaiting user clarification.
- 🧠 Reflection: The user input was garbled. Asking for clarification is the best approach to avoid incorrect actions and guide the user effectively.

## Evaluation notes (flywheel)

- Failure modes observed: User input was un-parsable.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
