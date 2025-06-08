from fastapi import APIRouter
from models.request_models import ParaphraseInput
from services.openai_service import paraphrase

router = APIRouter()


@router.post("/")
async def paraphrase_route(input: ParaphraseInput):
    output = await paraphrase(input.text, input.tone)
    return {"original": input.text, "paraphrased": output}
