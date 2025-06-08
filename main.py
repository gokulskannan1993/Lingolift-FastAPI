from fastapi import FastAPI
from routers import grammar, paraphrase, summarize, tone
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(grammar.router, prefix="/grammar-correct")
app.include_router(paraphrase.router, prefix="/paraphrase")
app.include_router(summarize.router, prefix="/summarize")
app.include_router(tone.router, prefix="/change-tone")
