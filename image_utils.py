import tempfile  # For creating temporary files
from PIL import Image  # For image processing
import streamlit as st  # For using Streamlit's functionalities

# Function to save uploaded file
def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
            tmp.write(uploaded_file.getvalue())
            return tmp.name
    return None

# Function to display images
def display_images(original_image_path, predicted_image_path):
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
