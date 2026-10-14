def build_quiz(gaps: list) -> list:
    return [f"Explain {g} with one real example." for g in gaps[:5]] or \
           ["Explain your best project end-to-end."]
