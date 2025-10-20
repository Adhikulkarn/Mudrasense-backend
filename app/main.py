from fastapi import FastAPI
from app.routes import detect

app = FastAPI()

app.include_router(detect.router)

@app.get("/")
def root():from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import detect

app = FastAPI(
    title="MudraSense API",
    description="YOLOv8-based hand mudra detection backend.",
    version="1.0.0"
)

# ✅ Allow frontend (React/Vue/Next.js, etc.) to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this later to your frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes
app.include_router(detect.router)

@app.get("/")
def root():
    return {"message": "MudraSense API is running!"}

    return {"message": "MudraSense API is running!"}
