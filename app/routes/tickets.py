from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket_model import Ticket, TicketStatus
from app.services.nlp_service import analyze_sentiment, categorize_ticket
from app.services.ticket_assignment import assign_agent

router = APIRouter()

@router.post("/tickets/")
def create_ticket(ticket: dict, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(ticket["description"])
    category = categorize_ticket(ticket["description"])
    assigned_agent = assign_agent(category)

    db_ticket = Ticket(
        customer_name=ticket["customer_name"],
        email=ticket["email"],
        subject=ticket["subject"],
        description=ticket["description"],
        category=category,
        priority=ticket.get("priority", "medium"),
        status=TicketStatus.OPEN
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return {**ticket, "sentiment": sentiment, "assigned_agent": assigned_agent}

@router.get("/tickets/")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()
