from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs', openapi_url='/api.openapi.json')

def greet_user(name: str)  -> dict:
    """이름을 받아 환영 메시지를 만듭니다."""
    return {"message": f"Nice to meet you, {name}!" }

@app.get("/users/{name}")
def greet_endpoint(name: str) -> dict:
    return greet_user(name)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)