from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.live_agent import router as live_router

app = FastAPI(title="Voxa Kids Backend")

# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # you can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include websocket/chat routes
app.include_router(live_router)


@app.get("/")
def root():
    return {"message": "Voxa Kids Backend Running"}