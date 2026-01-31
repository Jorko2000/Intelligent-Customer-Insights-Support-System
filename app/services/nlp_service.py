from textblob import TextBlob

def analyze_sentiment(text: str):
    """Return sentiment polarity between -1 (negative) and 1 (positive)"""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def categorize_ticket(text: str):
    """Categorize ticket based on keywords"""
    text = text.lower()
    if "billing" in text or "payment" in text:
        return "billing"
    elif "technical" in text or "error" in text or "crash" in text:
        return "technical"
    else:
        return "general"
