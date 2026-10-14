"""Agent stubs — replace heuristics with LLM calls during build week."""
import re

COMMON = ["python", "sql", "git", "ml basics", "statistics", "excel",
          "data viz", "prompt engineering", "apis"]

def parse_resume_text(text: str) -> list:
    text = (text or "").lower()
    return [s for s in COMMON if s in text]
