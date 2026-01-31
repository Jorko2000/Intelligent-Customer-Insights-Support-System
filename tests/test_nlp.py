
from app.services.nlp_service import analyze_sentiment, categorize_ticket

def test_sentiment():
    assert analyze_sentiment("I love this!") > 0
    assert analyze_sentiment("I hate this!") < 0

def test_categorize_ticket():
    assert categorize_ticket("Billing issue with account") == "billing"
    assert categorize_ticket("App crashes frequently") == "technical"
    assert categorize_ticket("General inquiry") == "general"
