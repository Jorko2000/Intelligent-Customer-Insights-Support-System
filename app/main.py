from fastapi import FastAPI
from app.routes import tickets_router, agents_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Customer Insights & Support System")

app.include_router(tickets_router)
app.include_router(agents_router)
