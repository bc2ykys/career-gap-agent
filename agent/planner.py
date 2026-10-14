def build_plan(gaps: list) -> list:
    plan = []
    for i, g in enumerate(gaps, 1):
        plan.append({"Day": f"{(i-1)*4+1}-{i*4}", "Focus": g,
                     "Task": f"Learn {g}: 1 tutorial + 1 mini-project + notes"})
    return plan or [{"Day": "1-4", "Focus": "stretch", "Task": "Build portfolio project"}]
