from summarizer.ai.chains import summary_chain

article = """
LangChain is a powerful, open-source developer framework designed to simplify the creation of applications powered by Large Language Models. Rather than being an AI model itself, it acts as the "nervous system" that seamlessly connects LLMs to external data sources, memory systems, and computational tools.At its core, it provides modular abstractions that let developers build sophisticated workflows without manually hardcoding prompt structures or API calls. Key building blocks include Prompt Templates for dynamic instruction management, Chains for stringing together multi-step logical operations, and Agents that use reasoning to decide which external APIs or functions to utilize. Additionally, it streamlines Retrieval-Augmented Generation (RAG) by integrating document loaders and vector stores, allowing models to accurately reference private or up-to-date datasets. By supporting both Python and JavaScript/TypeScript, LangChain gives developers the flexibility to swap out models and tools seamlessly as the AI landscape evolves. Coupled with tools like LangSmith for debugging and evaluating performance, it transforms standalone AI models into reliable, production-ready enterprise systems.
"""

result = summary_chain.invoke(
    {
        "text": article
    }
)

print(result)