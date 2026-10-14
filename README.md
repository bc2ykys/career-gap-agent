# Career Gap Agent — Education & Career AI

Agentic AI that takes a resume + target role → parses skills → finds gaps → builds a 20-day plan + mock quiz + tracker.

## Quickstart

```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Flow

upload PDF → parse → gap vs role → plan (web/courses) → quiz → tracker

## Responsible AI

- Resume stays local unless user opts in; never commit `.env` or real resumes.
- Plans are suggestions, not job guarantees.
- Log prompts/outputs for originality proof.
