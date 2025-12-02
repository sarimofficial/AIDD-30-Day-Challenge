---

description: "Task list for implementing the calculator feature"
---

# Tasks: calculator-expr

**Input**: Design documents from `/specs/001-calculator-expr/`
**Prerequisites**: spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create the initial project file `calculator.py`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [X] T002 Define the main `evaluate` function signature in `calculator.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Evaluate valid expression (Priority: P1) 🎯 MVP

**Goal**: The calculator can correctly evaluate a valid mathematical expression string and return a numerical result.

**Independent Test**: The `evaluate` function can be called with an expression like "1 + 1" and correctly returns `2`.

### Implementation for User Story 1

- [X] T003 [US1] Implement logic in the `evaluate` function to parse a valid mathematical expression string in `calculator.py`.
- [X] T004 [US1] Implement logic in the `evaluate` function to compute the result of the parsed expression in `calculator.py`.
- [X] T005 [US1] Ensure the `evaluate` function returns the correct numerical result in `calculator.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Handle invalid input and expressions (Priority: P2)

**Goal**: The calculator gracefully handles invalid input types and malformed mathematical expressions.

**Independent Test**: The `evaluate` function, when called with "1 + *" or non-string input, returns a specific error message or raises an exception instead of crashing.

### Implementation for User Story 2

- [X] T006 [US2] Add validation to the `evaluate` function to handle non-string inputs in `calculator.py`.
- [X] T007 [US2] Implement error handling for malformed expressions (e.g., "1 + * 2") within the `evaluate` function in `calculator.py`.
- [X] T008 [US2] Return a clear error message or raise an appropriate exception for invalid cases in `calculator.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T009 Add comprehensive docstrings to the `evaluate` function in `calculator.py`.
- [X] T010 Add inline comments for any complex parsing or evaluation logic in `calculator.py`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Must be completed first.
- **Foundational (Phase 2)**: Depends on Setup completion.
- **User Stories (Phase 3+)**: Depend on Foundational phase completion.
- **Polish (Final Phase)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2).
- **User Story 2 (P2)**: Can start after Foundational (Phase 2).

### Within Each User Story

- Tasks should be completed in the order listed.

### Parallel Opportunities

- No parallel opportunities identified as all work is in a single file.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently.

### Incremental Delivery

1. Complete Setup + Foundational.
2. Add User Story 1 → Test independently.
3. Add User Story 2 → Test independently.
