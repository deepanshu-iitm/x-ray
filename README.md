# X-Ray Decision Debugger

A lightweight X-Ray library and dashboard for debugging multi-step, non-deterministic decision systems by capturing why decisions were made, not just what happened.

## What This Does

- Records step-by-step decision context (inputs, rules, evaluations, outputs, reasoning)

- Makes complex pipelines explainable and debuggable

- Visualizes the full decision trail in a simple dashboard

## Components

- **X-Ray Library**:
General-purpose SDK to capture decision reasoning at each step.

- **Dashboard UI**:
Visual timeline showing what went in, what came out, and why.

- **Demo Pipeline**:
3-step mock workflow:

 1. Keyword generation (simulated LLM)

 2. Candidate search (mock API)

 3. Apply filters (price, rating, reviews)

## Project Structure
```bash
backend/
  ├── xray/        # X-Ray SDK
  ├── demo/        # Demo decision pipeline
  └── main.py      # FastAPI server

frontend/
  └── index.html   # Dashboard UI

```
## Setup
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
**Open dashboard**:

frontend/index.html

or serve via python -m http.server
