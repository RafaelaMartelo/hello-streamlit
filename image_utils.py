import tempfile  
from PIL import Image  
import streamlit as st  


def save_uploaded_file(uploaded_file):
    """
    Saves the uploaded file to a temporary file.

    Args:
        uploaded_file: The file uploaded by the user.

    Returns:
        str: The path to the temporary file where the uploaded file is saved.
    """
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
            tmp.write(uploaded_file.getvalue()) 
            return tmp.name 
    return None  


def display_images(original_image_path, predicted_image_path):
    """
    Displays the original and predicted images side by side.

    Args:
        original_image_path (str): Path to the original image file.
        predicted_image_path (str): Path to the predicted image file.
    """
    col1, col2 = st.columns(2)  
    
    with col1:  
        st.image(original_image_path, caption='Selected Image', use_column_width=True)  
    
    if predicted_image_path:  
        predicted_image = Image.open(predicted_image_path)  
        with col2:  
            st.image(predicted_image, caption='Predicted Image', use_column_width=True)  
    else:  
        with col2:
            st.error('Prediction failed or no predictions made.')  
