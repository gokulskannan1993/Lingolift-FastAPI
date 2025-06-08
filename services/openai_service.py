import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


async def ask_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message["content"].strip()


async def correct_grammar(text: str):
    return await ask_openai([
        {"role": "system", "content": "You are a grammar corrector."},
        {"role": "user", "content": f"Correct this text: \"{text}\""}
    ])


async def paraphrase(text: str, tone: str):
    return await ask_openai([
        {"role": "system", "content": "You help rephrase content in various tones."},
        {"role": "user", "content": f"Paraphrase this in a {tone} tone: \"{text}\""}
    ])


async def summarize(text: str, length: str):
    return await ask_openai([
        {"role": "system", "content": "You summarize text efficiently."},
        {"role": "user", "content": f"Summarize the following text in a {length} format: \"{text}\""}
    ])


async def change_tone(text: str, target_tone: str):
    return await ask_openai([
        {"role": "system", "content": "You rewrite text in the desired tone."},
        {"role": "user", "content": f"Rewrite this in a {target_tone} tone: \"{text}\""}
    ])
