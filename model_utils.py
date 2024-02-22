from ultralytics import YOLO

def load_model(model_path='best.pt'):
    model = YOLO(model_path)
    return model

def predict(model, image_path, confidence):
    results = model.predict(source=image_path, conf=confidence)
    return results
