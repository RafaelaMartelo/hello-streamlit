# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from model_utils import load_model, predict
from image_utils import save_uploaded_file, display_images
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# Global variables for sample images
SAMPLE_IMAGE_SNOWY = "images/test_5.jpg"
SAMPLE_IMAGE_CLEAN = "images/test_10.jpg"


# Main function to run the app
def main():
    LOGGER.info("App started")
    
    st.title('Object Detection for Autonomous Vehicles in Inclement Weather')
    st.markdown("""
    Welcome to this demonstration, showcasing the application of the YOLOv8 model, an existing state-of-the-art object detection framework, tailored to enhance the perception capabilities of autonomous vehicles in inclement weather.
    """)

    st.sidebar.markdown('''**How to Use This App**  
    1️⃣  Adjust the **Model Confidence** slider to set the detection threshold.  
    2️⃣ Choose **Image Source** to upload your image or select a sample image.  
    3️⃣ Click the **Predict** button to perform object detection.  
    ''', unsafe_allow_html=True)

    # Adding a slider to the sidebar for selecting model confidence
    st.sidebar.markdown('**Select Model Confidence**')  # Using Markdown for bold text
    confidence = st.sidebar.slider("**Model Confidence**", 25, 100, 40, key="conf_slider", label_visibility="collapsed")/100  # Empty label

    sample_image_paths = {
        "Sample Snowy Day ❄️": SAMPLE_IMAGE_SNOWY,
        "Sample Clean Day 🌤️": SAMPLE_IMAGE_CLEAN
    }

    # Option for users to choose an image source
    st.sidebar.markdown('**Select Image Source**') 
    image_source = st.sidebar.radio("**Image Source**", ["Upload Image 🚗", "Sample Snowy Day ❄️", "Sample Clean Day 🌤️"], key="image_source", label_visibility="collapsed")

    image_path = None

    if image_source == "Upload Image 🚗":
        uploaded_file = st.sidebar.file_uploader("Upload an image...", type=['png', 'jpg', 'jpeg'])
        image_path = save_uploaded_file(uploaded_file) if uploaded_file else None
    else:
        image_path = sample_image_paths[image_source]

    if st.button('Predict'):
        if image_path:
            model = load_model()
            predicted_image_path = predict(model, image_path, confidence)
            display_images(image_path, predicted_image_path)
        else:
            st.warning("Please select an image source and click 'Predict' to proceed.")

    # Model Performance Metrics
    st.markdown("""
    ### Model Performance Metrics

    The table below presents the performance metrics of the YOLO model tailored for object detection in inclement weather conditions, crucial for autonomous vehicle navigation. The metrics underscore the model's proficiency in identifying key objects—cars, trucks, and persons—with notable precision and recall rates. 

    | Class   | Images | Instances | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
    |---------|--------|-----------|-----------|--------|---------|--------------|
    | All     | 39     | 290       | 86.2%     | 77.5%   | 84.3%   | 58.9%        |
    | Car     | 39     | 221       | 85.8%     | 76.5%   | 86.1%   | 60.8%        |
    | Person  | 39     | 48        | 78.1%     | 70.8%   | 80.0%   | 45.7%        |
    | Truck   | 39     | 21        | 94.7%     | 85.2%   | 86.9%   | 70.2%        |

    These metrics demonstrate the model's effectiveness in accurately identifying cars, trucks, and persons, which are essential for the safety and operational efficiency of autonomous vehicles under various weather conditions. However, it's important to note that the model's performance, while impressive, is not infallible. Trained on a relatively small dataset, the model may exhibit limitations in certain complex scenarios typical of inclement weather conditions. Continuous improvements and training on a more diverse and extensive dataset are essential for enhancing the model's robustness and reliability in real-world applications.

    ### More About This Project 

    This project explores the application of object detection technologies in enhancing autonomous vehicle navigation, particularly under challenging weather conditions. By focusing on critical object detection, the project aims to contribute to the safety and efficiency of autonomous driving systems. 

    For a deeper understanding of the project's objectives, methodologies, and findings, please visit the [GitHub repository](https://github.com/RafaelaMartelo/Capstone_Object_Tracking_and_Detection_for_AV/tree/main).

    """)

    st.sidebar.markdown("""
    ---
    **🔍 More About This Project**  
    To learn more about this project, its methodologies, datasets used, and the technology behind it, visit the GitHub repository:
    [Rafaela Martelo's Capstone Project on GitHub](https://github.com/RafaelaMartelo/Capstone_Object_Tracking_and_Detection_for_AV/tree/main)
    """)

    st.markdown("---")
    st.caption("Developed by Rafaela Martelo 👩‍💻. This is a demonstration app for object detection using YOLOv8.")

if __name__ == "__main__":
    main()
