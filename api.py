from fastapi import FastAPI
from copykitt import generate_brand_snippet, generate_keywords

app = FastAPI()


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    snippet = generate_brand_snippet(prompt)
    return {"snippet": snippet}

#run server
##uvicorn api:app --reload