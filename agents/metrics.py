class AgentMetrics:
    def __init__(self):
        self.steps_executed = 0
        self.failures = 0
        self.success = False

    def step(self):
        self.steps_executed += 1

    def failure(self):
        self.failures += 1

    def mark_success(self):
        self.success = True
