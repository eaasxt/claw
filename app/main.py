from fastapi import FastAPI
from app.routes.slack import router as slack_router

app = FastAPI()
app.include_router(slack_router, prefix="/slack")
