from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

class LLM:
    def __init__(self):
        self.llm = ChatOllama(
            model = "qwen3:8b",
            temperature = 0,
            disable_streaing = True,
        )

    def generate(self, context, query):
        prompt = PromptTemplate(
            input_variables=["context", "query"],
            template = """
                You are an assistant that answers questions using only the provided context. You don't
                make answers of your own. 

                Context:
                {context}

                Question:
                {query}

                Answer:

            """
        )

        formatted_prompt = prompt.format(
            context=context,
            query=query
        )
        # print(len(formatted_prompt))


        return self.llm.invoke(formatted_prompt)