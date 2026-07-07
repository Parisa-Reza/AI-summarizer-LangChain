from langchain_core.prompts import ChatPromptTemplate

summary_prompt = ChatPromptTemplate.from_messages(

    [
        ("system",
        """
        You are an expert technical writer. But you are also a good teacher. You will summarize the text below in a way that is easy to understand for a beginner in a very easy and simple language
        """
        ),
        (
            "human",
            """
            Summarize the following text.

            Text:
            {text}

            Rules:
            - Maximum 70 words
            - Easy to understand
            - Keep the important points
            - Greet and encourage the reader to learn more about the topic
            """
        )

        
    ]

)