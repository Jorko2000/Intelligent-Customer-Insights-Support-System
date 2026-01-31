import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_ticket():
    ticket_data = {
        "customer_name": "Test User",
        "email": "test@example.com",
        "subject": "Test Ticket",
        "description": "This is a test technical ticket.",
        "priority": "high"
    }
    response = client.post("/tickets/", json=ticket_data)
    assert response.status_code == 200
    assert "assigned_agent" in response.json()

