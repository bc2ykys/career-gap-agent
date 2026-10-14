def find_gaps(skills: list, required: list) -> list:
    have = set(s.lower() for s in skills)
    return [r for r in required if r.lower() not in have]
