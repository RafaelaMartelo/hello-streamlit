from ultralytics import YOLO  
import glob  
import os  

def load_model():
    """
    Loads the pre-trained YOLOv8 Small model.

    Returns:
        model (YOLO): An instance of the YOLO class with loaded pre-trained weights.
    """
    return YOLO('best.pt')  


def predict(model, image_path, confidence):
    """
    Predicts objects in the given image using the specified YOLO model.

    Args:
        model (YOLO): The loaded YOLO model for object detection.
        image_path (str): Path to the image file on which to perform object detection.
        confidence (float): Confidence threshold for detecting objects.

    Returns:
        str: Path to the image with predictions, or None if no predictions were made.
    """
    # Perform prediction using the model on the specified image with the given confidence threshold
    results = model.predict(source=image_path, conf=confidence, save=True, name='predicted')
    
    # Sorting the directories containing predictions in reverse chronological order (most recent first)
    predicted_dirs = sorted(glob.glob('runs/detect/predicted*/'), key=os.path.getmtime, reverse=True)
    
    if predicted_dirs:  
        latest_predicted_dir = predicted_dirs[0]  
        predicted_images = glob.glob(f'{latest_predicted_dir}/*.jpg')  
        
        if predicted_images:  
            return predicted_images[0] 
    return None  
