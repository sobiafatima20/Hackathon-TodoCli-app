---
id: "001"
title: Create project constitution for Phase-2 Todo web app
stage: constitution
date: 2026-01-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: sobiafatima
command: /sp.constitution
labels: ["constitution","governance","principles"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - phase-II/.specify/memory/constitution.md
tests:
  - None
---

## Prompt

/sp.constitution

Project: Todo Full-Stack Web Application (Hackathon Phase-2)

Core principles:
- Specification-Led Development
  Every feature and behavior must be implemented strictly according to approved specifications.
- Mandatory Agentic Workflow 
  Development must follow this exact lifecycle:  
  Specification → Planning → Task Decomposition → Automated Implementation
  Manual or ad-hoc coding is not permitted.
- Security-by-Default Architecture
  Authentication, authorization, and strict user data isolation are enforced at all layers by default.
- Consistent and Deterministic Behavior
  APIs and user interfaces must behave predictably and consistently across all users and sessions.
- End-to-End System Alignment
  Frontend, backend, authentication, and database layers must remain fully synchronized with no implicit assumptions.


Key standards:
- No implementation may begin without an approved specification and execution plan
- All API contracts and behaviors must be fully documented in specifications
- Authentication must be implemented using **Better Auth with JWT-based tokens**
- Every backend route must validate JWTs and enforce resource ownership
- All database access must be explicitly scoped to the authenticated user
- REST APIs must strictly adhere to HTTP methods, status codes, and semantics
- Error responses must be explicit, deterministic, and documented
- Frontend integration must conform exactly to defined API specifications
- Secrets must never be hard-coded; environment variables are mandatory


Constraints:
- All code must be generated exclusively through Claude Code
  Manual coding is strictly forbidden.
- The technology stack is fixed and cannot be altered:
  - Frontend: Next.js 16+ (App Router)
  - Backend: Python FastAPI
  - ORM: SQLModel
  - Database: Neon Serverless PostgreSQL
  - Authentication: Better Auth (JWT-based)
- All protected endpoints require a valid JWT
- Backend authentication must remain stateless (JWT-only)
- Multi-user capability is required by design
- Persistent data storage across sessions is mandatory

Success criteria:
- Backend, Authentication, and Frontend specifications are fully implemented and integrated
- Users are able to register, authenticate, and manage only their own tasks
- All unauthorized requests consistently return **HTTP 401**
- Task ownership is enforced across all CRUD operations
- The application operates correctly as a complete full-stack system
- Specifications, plans, and implementation steps are traceable and reviewable
- The project satisfies hackathon evaluation criteria for correctness and process discipline

## Response snapshot

Created project constitution at `.specify/memory/constitution.md` with:
- 6 core principles (Spec-Driven Development, Agentic Workflow, Security-First, Deterministic Behavior, Full-Stack Coherence, Traceability)
- Technology Stack section documenting fixed stack (Next.js, FastAPI, SQLModel, Neon PostgreSQL, Better Auth)
- Development Workflow section with 4 phases (Specification, Planning, Task Breakdown, Implementation, Integration)
- Quality Standards covering API, Security, and Testing requirements
- Governance section establishing constitution precedence

## Outcome

- ✅ Impact: Established project constitution v1.0.0 for Phase-2 Todo web application
- 🧪 Tests: None
- 📁 Files: `.specify/memory/constitution.md`
- 🔁 Next prompts: Create feature specs for Backend, Auth, and Frontend
- 🧠 Reflection: Constitution establishes the governance framework for agentic SDD workflow

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (if applicable): N/A
