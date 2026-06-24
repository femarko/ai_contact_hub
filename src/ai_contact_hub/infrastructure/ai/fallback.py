

def fallback_sentiment(text: str) -> dict[str, str]:
    negative_words = [
        "плохо",
        "ужас",
        "проблема",
        "ошибка",
        "ненавижу"
    ]
    positive_words = [
        "спасибо",
        "отлично",
        "хорошо",
        "люблю"
    ]
    text = text.lower()
    if any(word in text for word in negative_words):
        sentiment = "negative"
    elif any(word in text for word in positive_words):
        sentiment = "positive"
    else:
        sentiment = "neutral"
    return {
        "sentiment": sentiment,
        "source": "fallback"
    }
