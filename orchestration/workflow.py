import time
from app.agents.planner import create_plan
from app.agents.researcher import research
from app.agents.summarizer import summarize
from app.agents.memory import AgentMemory
from app.agents.metrics import AgentMetrics
from app.agents.evaluation import evaluate_summary
from app.config import MAX_RETRIES
from app.logging_config import logger

def execute(goal: str):
    memory = AgentMemory()
    metrics = AgentMetrics()
    start = time.time()

    try:
        plan = create_plan(goal)
        metrics.step()
        memory.add("planner", str(plan))

        research_data = None
        for attempt in range(MAX_RETRIES + 1):
            try:
                research_data = research(plan[0])
                metrics.step()
                memory.add("researcher", research_data)
                break
            except Exception:
                metrics.failure()
                logger.warning("Research agent failed, retrying...")

        summary = summarize(research_data)
        metrics.step()
        memory.add("summarizer", summary)

        evaluation = evaluate_summary(summary)
        metrics.mark_success()

        latency = round(time.time() - start, 2)

        return {
            "goal": goal,
            "summary": summary,
            "evaluation": evaluation,
            "execution_trace": memory.get_trace(),
            "metrics": {
                "steps_executed": metrics.steps_executed,
                "failures": metrics.failures,
                "success": metrics.success,
                "latency_seconds": latency
            }
        }

    except Exception as e:
        metrics.failure()
        return {
            "error": str(e),
            "metrics": {
                "steps_executed": metrics.steps_executed,
                "failures": metrics.failures,
                "success": False
            }
        }
