from fastapi import APIRouter
from models.request_models import ToneInput
from services.openai_service import change_tone

router = APIRouter()


@router.post("/")
async def change_tone_route(input: ToneInput):
    output = await change_tone(input.text, input.tone)
    return {"original": input.text, "changedTone": output}
