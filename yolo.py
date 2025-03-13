from ultralytics import YOLO

model = YOLO("yolov8n.pt")
result = model.predict("image.jpg")
result[0].show()