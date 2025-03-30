from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Initialize OllamaLLM with the desired model
llm = OllamaLLM(model="mistral")

# Create a prompt template
template = "Question: {question}\n\nAnswer:"
prompt = PromptTemplate(template=template, input_variables=["question"])

# Combine the prompt and LLM into a chain
chain = prompt | llm

# Example usage
question = input("Enter your question: ")
answer = chain.invoke({"question": question})
# print(answer)