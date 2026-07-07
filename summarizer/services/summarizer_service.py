from summarizer.ai.chains import summary_chain


def summarize_text(article: str) -> str:
    summary = summary_chain.invoke(
        {
            "text": article
        }
    )

    return summary