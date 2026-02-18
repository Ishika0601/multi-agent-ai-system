class AgentMemory:
    def __init__(self):
        self.trace = []

    def add(self, agent: str, content: str):
        self.trace.append({
            "agent": agent,
            "content": content
        })

    def get_trace(self):
        return self.trace
