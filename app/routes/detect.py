from fastapi import APIRouter, UploadFile, File
import shutil
import uuid
from app.services.yolo_service import YoloService

router = APIRouter(prefix="/detect", tags=["Detection"])
yolo_service = YoloService("best.pt")

@router.post("/")
async def detect_gesture(file: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4()}.jpg"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = yolo_service.predict(temp_filename)
    return {"detections": results}
