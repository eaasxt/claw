from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/")
async def handle_slack(request: Request):
    payload = await request.json()
    return {"response": "Received Slack event", "event": payload}
