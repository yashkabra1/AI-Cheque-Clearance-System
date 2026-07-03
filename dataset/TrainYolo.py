from ultralytics import YOLO
import os
print("Current Working Directory:", os.getcwd())
model = YOLO("yolov8n.pt")
results = model.train(
    data="Dataset/data.yaml",  
    epochs=50,                           
    imgsz=640,                            
    batch=8,                              
    device=0,                         
    workers=0,                           
    verbose=True
)
print("\nTraining complete ")
print("Best model should be saved inside runs/detect/train*/weights/best.pt")