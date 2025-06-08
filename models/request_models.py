from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


class ParaphraseInput(TextInput):
    tone: str = "casual"


class SummaryInput(TextInput):
    length: str = "short"


class ToneInput(TextInput):
    target_tone: str = "professional"
