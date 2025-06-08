from fastapi import APIRouter
from models.request_models import TextInput
from services.openai_service import correct_grammar

router = APIRouter()


@router.post("/")
async def correct_grammar_route(input: TextInput):
    output = await correct_grammar(input.text, input.tone)
    return {"original": input.text, "corrected": output}
