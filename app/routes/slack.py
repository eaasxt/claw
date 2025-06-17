from fastapi import APIRouter, Request
from app.services.prompt_runner import run_prompt

router = APIRouter()

@router.post("", include_in_schema=False)
@router.post("/")
async def handle_slack(request: Request):
    payload = await request.json()
    prompt = payload.get("text", "")
    llm_response = run_prompt(prompt)
    return {"response": llm_response}
