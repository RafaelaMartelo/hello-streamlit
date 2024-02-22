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
from streamlit.logger import get_logger
from ultralytics import YOLO
from PIL import Image
import tempfile
import os
import glob

LOGGER = get_logger(__name__)


def run():

  # Initialize the YOLO model
  model = YOLO('best.pt')

  # Streamlit page setup
  st.title('Object Detection for Autonomous Vehicles in Inclement Weather')

  # Introduction and model capabilities
  st.markdown("""

  Welcome to this demonstration, showcasing the application of the YOLOv8 model, an existing state-of-the-art object detection framework, tailored to enhance the perception capabilities of autonomous vehicles in inclement weather. This project focuses on adapting and fine-tuning a pre-trained YOLOv8 model to recognize critical objects such as cars, trucks, and pedestrians with high accuracy, even under challenging weather conditions that typically hinder visibility and sensor performance.

  Discover the app's features to understand the impact of our model's performance under various conditions and learn more about the potential advancements it offers to autonomous vehicle technologies.       

  """)

  # Sidebar: Instructions and Model Confidence
  st.sidebar.markdown('''**How to Use This App**  
  1️⃣  Adjust the **Model Confidence** slider to set the detection threshold.  
  2️⃣ Choose **Image Source** to upload your image or select a sample image.  
  3️⃣ Click the **Predict** button to perform object detection.  
  ''', unsafe_allow_html=True)

  # Adding a slider to the sidebar for selecting model confidence
  st.sidebar.markdown('**Select Model Confidence**')  # Using Markdown for bold text
  confidence = st.sidebar.slider("", 25, 100, 40, key="conf_slider")/100  # Empty label

  # Define paths to your sample images
  sample_image_paths = {
      "Sample Snowy Day ❄️": "C:/Users/rafae/Documents/Capstone/test_5.jpg",
      "Sample Clean Day 🌤️": "C:/Users/rafae/Documents/Capstone/test_10.jpg"
  }

  # Option for users to choose an image source
  st.sidebar.markdown('**Image Source**')  # Using Markdown for bold text
  image_source = st.sidebar.radio("", ["Upload Image 🚗", "Sample Snowy Day ❄️", "Sample Clean Day 🌤️"], key="image_source")

  # Handling image source selection
  uploaded_file = None
  if image_source == "Upload Image 🚗":
      uploaded_file = st.sidebar.file_uploader('Upload an image...', type=['png', 'jpg', 'jpeg'], key="file_uploader")
      if uploaded_file is not None:
          with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
              tmp.write(uploaded_file.getvalue())
              tmp.flush()
              image_path = tmp.name
  else:
      image_path = sample_image_paths[image_source]

  # Display the selected or uploaded image and perform prediction
  if uploaded_file is not None or image_source != "Upload Image":
      if st.button('Predict', key='predict_button'):
          col1, col2 = st.columns(2)
          with col1:
              image = Image.open(image_path)
              st.image(image, caption='Selected Image', use_column_width=True)
          
          model.predict(source=image_path, name='predicted', save=True, conf=confidence)
          
          predicted_dirs = sorted(glob.glob('runs/detect/predicted*/'), key=os.path.getmtime, reverse=True)
          if predicted_dirs:
              latest_predicted_dir = predicted_dirs[0]
              predicted_images = glob.glob(f'{latest_predicted_dir}*.jpg')
              if predicted_images:
                  predicted_image_path = predicted_images[0]
                  predicted_image = Image.open(predicted_image_path)
                  with col2:
                      st.image(predicted_image, caption='Predicted Image', use_column_width=True)
              else:
                  with col2:
                      st.error('No predicted image found in the latest directory.')
          else:
              with col2:
                  st.error('No prediction directories found.')
  else:
      if st.button('Predict', key='predict_button_disabled'):
          st.warning('Please select an image source to use for predictions.')

  # Model Performance Metrics
  st.markdown("""
  ### Model Performance Metrics

  The table below presents the performance metrics of the YOLO model tailored for object detection in inclement weather conditions, crucial for autonomous vehicle navigation. The metrics underscore the model's proficiency in discerning between key objects—cars, trucks, and persons—with notable precision and recall rates. 

  | Class   | Images | Instances | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
  |---------|--------|-----------|-----------|--------|---------|--------------|
  | All     | 39     | 290       | 86.2%     | 77.5%   | 84.3%   | 58.9%        |
  | Car     | 39     | 221       | 85.8%     | 76.5%   | 86.1%   | 60.8%        |
  | Person  | 39     | 48        | 78.1%     | 70.8%   | 80.0%   | 45.7%        |
  | Truck   | 39     | 21        | 94.7%     | 85.2%   | 86.9%   | 70.2%        |

  These metrics demonstrate the model's effectiveness in accurately identifying cars, trucks, and persons, which are pivotal for the safety and operational efficiency of autonomous vehicles under various weather conditions. However, it's important to note that the model's performance, while impressive, is not infallible. Trained on a relatively small dataset, the model may exhibit limitations in certain complex scenarios typical of inclement weather conditions. Continuous improvements and training on a more diverse and extensive dataset are essential for enhancing the model's robustness and reliability in real-world applications.

  ### More About This Project 

  This project explores the application of object detection technologies in enhancing autonomous vehicle navigation, particularly under challenging weather conditions. By focusing on critical object detection, the project aims to contribute to the safety and efficiency of autonomous driving systems. 

  For a deeper understanding of the project's objectives, methodologies, and findings, please visit the [GitHub repository](https://github.com/RafaelaMartelo/Capstone_Object_Tracking_and_Detection_for_AV/tree/main).

  """)

  # Add a section at the bottom of the sidebar for more information about the project
  st.sidebar.markdown("""
  ---
  **🔍 More About This Project**  
  To learn more about this project, its methodologies, datasets used, and the technology behind it, visit the GitHub repository:
  [Rafaela Martelo's Capstone Project on GitHub](https://github.com/RafaelaMartelo/Capstone_Object_Tracking_and_Detection_for_AV/tree/main)
  """)

  # Add some space before the footer
  st.markdown("---")
  st.caption("Developed by Rafaela Martelo 👩‍💻. This is a demonstration app for object detection using YOLOv8.")



if __name__ == "__main__":
    run()
