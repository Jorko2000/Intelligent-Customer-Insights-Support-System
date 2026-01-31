from fastapi import APIRouter

router = APIRouter()

agents = [
    {"id": 1, "name": "Alice", "tickets_assigned": 5},
    {"id": 2, "name": "Bob", "tickets_assigned": 3},
    {"id": 3, "name": "Charlie", "tickets_assigned": 2},
    {"id": 4, "name": "Diana", "tickets_assigned": 4},
]

@router.get("/agents/")
def get_agents():
    return agents

@router.get("/agents/{agent_id}")
def get_agent(agent_id: int):
    for agent in agents:
        if agent["id"] == agent_id:
            return agent
    return {"error": "Agent not found"}
