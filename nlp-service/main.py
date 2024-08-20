from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Text(BaseModel):
    text: str

@app.post("/api/check")
async def check_text(text: Text):
    return {"corrected_text": text.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
