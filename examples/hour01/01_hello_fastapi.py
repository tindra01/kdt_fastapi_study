from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.jason')

@app.get("/hello")
def say_hello() -> dict:
    """간단한 JSON 메시지를 반환합니다"""
    return {"message": "Hello, fastapi learner!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)