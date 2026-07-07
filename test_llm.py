from summarizer.ai.llm import model

response = model.invoke("Say hello in one sentence.")

print(response.content)