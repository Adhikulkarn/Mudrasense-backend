from ultralytics import YOLO

class YoloService:
    def __init__(self, model_path="best.pt"):
        self.model = YOLO("/home/spidy/Desktop/Projects/Mudrasense-backend/best.pt")

    def predict(self, image_path: str):
        results = self.model.predict(image_path)
        detections = []
        for r in results:
            for box in r.boxes:
                detections.append({
                    "class": r.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy[0].tolist()
                })
        return detections
