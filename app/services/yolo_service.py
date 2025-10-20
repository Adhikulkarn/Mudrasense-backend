from ultralytics import YOLO
import cv2
import numpy as np

class YoloService:
    def __init__(self, model_path="best.pt"):
        self.model = YOLO(model_path)

    def predict(self, image):
        # If path is given, read the image
        if isinstance(image, str):
            img = cv2.imread(image)
        else:
            img = image  # assume it's already a numpy array

        results = self.model.predict(img)
        detections = []
        for r in results:
            for box in r.boxes:
                detections.append({
                    "class": r.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy[0].tolist()
                })
        return detections
