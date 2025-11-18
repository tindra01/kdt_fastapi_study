from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

class TranscriptInput(BaseModel):
    text: str = "홍길동"
    language: str = "KO"

def process_transcript(payload: TranscriptInput) -> dict:
    """텍스트 길이 정보를 담아 응답합니다."""
    return {"length": len(payload.text), "language": payload.language}

@app.post("/transcript")
def transcript_endpoint(payload: TranscriptInput) -> dict:
    return process_transcript(payload)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)