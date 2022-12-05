from fastapi import FastAPI, HTTPException
from copykitt import generate_brand_snippet, generate_keywords

app = FastAPI()

Max_Input_Len = 32

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    snippet = generate_brand_snippet(prompt)
    return {"snippet": snippet}

@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    keywords = generate_keywords(prompt)
    return {"snippet":None, "keywords": keywords}

@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_len(prompt)
    snippet = generate_brand_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet":snippet, "keywords": keywords}

def validate_input_len(prompt: str):
    if len(prompt) > Max_Input_Len:
        raise HTTPException(status_code=400, detail=f"Input length is too long. Must be under {Max_Input_Len}")
    pass

#run server
##uvicorn api:app --reload