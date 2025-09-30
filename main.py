from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Meu novo novo novo novo novo novo novo novo novo:: Hello from Hello-App! V9"}
