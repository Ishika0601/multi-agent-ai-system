from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def summarize(content: str):
    prompt = f"""
Summarize the following content clearly and concisely:

{content}
"""
    return llm.predict(prompt)
