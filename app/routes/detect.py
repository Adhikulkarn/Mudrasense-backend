from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2
from app.services.yolo_service import YoloService

router = APIRouter(prefix="/detect", tags=["Detection"])
yolo_service = YoloService("best.pt")

@router.post("/")
async def detect_gesture(file: UploadFile = File(...)):
    # Read image bytes directly (no need to save temporarily)
    image_bytes = await file.read()
    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Pass numpy array directly to YOLO
    results = yolo_service.predict(img)
    return {"detections": results}