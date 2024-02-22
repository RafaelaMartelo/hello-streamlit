from ultralytics import YOLO  
import glob  
import os  


# Function to load the YOLO model
def load_model():
    return YOLO('best.pt')


def predict(model, image_path, confidence):
    results = model.predict(source=image_path, conf=confidence, save=True, name='predicted')
    predicted_dirs = sorted(glob.glob('runs/detect/predicted*/'), key=os.path.getmtime, reverse=True)
    if predicted_dirs:
        latest_predicted_dir = predicted_dirs[0]
        predicted_images = glob.glob(f'{latest_predicted_dir}/*.jpg')
        if predicted_images:
            return predicted_images[0]
    return None

