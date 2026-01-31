
---

##  Integrated Backend – ML Support (`app/routes/tickets.py`) 

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket_model import Ticket, TicketStatus
from app.services.nlp_service import analyze_sentiment, categorize_ticket
import joblib
import pandas as pd

router = APIRouter()

# Load ML models and encoders
priority_model = joblib.load("ml_models/ticket_priority_model.pkl")
agent_model = joblib.load("ml_models/agent_assignment_model.pkl")
le_category = joblib.load("ml_models/le_category.pkl")
le_priority = joblib.load("ml_models/le_priority.pkl")
le_agent = joblib.load("ml_models/le_agent.pkl")

@router.post("/tickets/")
def create_ticket(ticket: dict, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(ticket["description"])
    category = categorize_ticket(ticket["description"])
    
    # Predict ticket priority
    ticket_text = ticket["description"] + " " + category
    predicted_priority = priority_model.predict([ticket_text])[0]
    
    # Predict best agent
    X_new = pd.DataFrame({
        "category": [le_category.transform([category])[0]],
        "priority": [le_priority.transform([predicted_priority])[0]]
    })
    agent_index = agent_model.predict(X_new)[0]
    assigned_agent = le_agent.inverse_transform([agent_index])[0]
    
    db_ticket = Ticket(
        customer_name=ticket["customer_name"],
        email=ticket["email"],
        subject=ticket["subject"],
        description=ticket["description"],
        category=category,
        priority=predicted_priority,
        status=TicketStatus.OPEN
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    
    return {
        "customer_name": ticket["customer_name"],
        "email": ticket["email"],
        "subject": ticket["subject"],
        "description": ticket["description"],
        "category": category,
        "priority": predicted_priority,
        "sentiment": sentiment,
        "assigned_agent": assigned_agent
    }

@router.get("/tickets/")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()
