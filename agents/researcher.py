from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def research(task: str):
    prompt = f"""
You are a research agent.
Task: {task}

Return factual, structured, and concise information.
"""
    return llm.predict(prompt)
