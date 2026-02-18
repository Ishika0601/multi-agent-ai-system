def evaluate_summary(summary: str) -> dict:
    return {
        "length_ok": len(summary) > 100,
        "structured": "." in summary,
        "quality": "high" if len(summary) > 200 else "medium"
    }
