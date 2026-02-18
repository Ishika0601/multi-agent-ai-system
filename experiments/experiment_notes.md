# Multi-Agent System Experiments

## Experiment 1: Retry Strategy

- Retries = 0 → success rate ~78%
- Retries = 1 → success rate ~88%
- Retries = 2 → success rate ~93%

Decision: MAX_RETRIES = 2

---

## Experiment 2: Output Quality

Measured based on summary length and structure.

| Run | Quality |
|----|--------|
| Short queries | Medium |
| Technical queries | High |

---

## Experiment 3: Latency

| Scenario | Avg Latency |
|--------|-------------|
| Simple topic | ~1.1s |
| Complex topic | ~1.6s |
