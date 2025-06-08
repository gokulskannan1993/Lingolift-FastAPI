from fastapi import APIRouter
from models.request_models import SummaryInput
from services.openai_service import summarize

router = APIRouter()


@router.post("/")
async def summarize_route(input: SummaryInput):
    output = await summarize(input.text, input.length)
    return {"original": input.text, "summary": output}
