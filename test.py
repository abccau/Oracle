from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b",
    disable_streaming=True,
)

print(llm.invoke("Hello"))