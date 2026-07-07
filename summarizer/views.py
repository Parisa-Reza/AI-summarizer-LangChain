from django.shortcuts import render
from summarizer.ai.chains import summary_chain
from summarizer.services.summarizer_service import summarize_text

def index(request):
    summary = None
    if request.method == "POST":
        article = request.POST.get("article", "").strip()

        if article:
            summary = summarize_text(article)
    
    return render(request, "index.html", {"summary": summary})
        