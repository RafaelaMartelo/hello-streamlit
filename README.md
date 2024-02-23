# Object Detection for Autonomous Vehicles in Inclement Weather

## Project Overview

This project showcases the application of the YOLOv8 model for object detection, tailored for enhancing the perception capabilities of autonomous vehicles under inclement weather conditions. Our solution focuses on accurately recognizing critical objects such as cars, trucks, and pedestrians, ensuring safety and efficiency in autonomous vehicle navigation despite challenging visibility and sensor performance hurdles posed by adverse weather.

## Demo Video

![Demo](streamlit-demo-video.gif)

## Try it Yourself!

Experience the app firsthand:

[![Try the Object Detection App](URL_TO_IMAGE_IF_AVAILABLE)](https://object-detection-demoo.streamlit.app/)

## Deployment Instructions

To deploy this Streamlit app using our repository, follow these steps:

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Git**: For cloning and managing versions of the repository.
- **Python**: The project is tested with Python 3.9. Adjust according to your project's compatibility. It's recommended to use a virtual environment.
- **pip**: To install Python packages listed in `requirements.txt`.

Please refer to `requirements.txt` for the Python packages and their versions needed to run this application.


### Steps

1. **Clone the Repository**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/RafaelaMartelo/object-detection-demo.git
   cd your-repo-name

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate  # On Windows

3. **Install Dependencies**

   Install the project's dependencies by running:

   ```bash
   pip install -r requirements.txt

4. **Run the App Locally**

   With the dependencies installed, you can run the app locally by executing:

   streamlit run object_detection_demo.py

   Your default web browser should automatically open a new tab pointing to localhost:8501, where you can interact with your Streamlit app.

5. **Deploying on Streamlit Sharing**

   - Ensure you have a `requirements.txt` file and a `packages.txt` file (if necessary for system-level packages) in your repository.
   - Log in to your Streamlit Sharing account or sign up if you don't have one.
   - Once logged in, go to your apps dashboard and click on 'New app'.
   - Select the GitHub repository where you've pushed your app, choose the branch where the app is located, and then enter the path to your app's file (`object_detection_demo.py`).
   - Click 'Deploy', and Streamlit Sharing will start the process of deploying your app. After a few moments, you should be provided with a URL to access your deployed app.

**Note**: The deployment process on Streamlit Sharing automatically installs Python dependencies listed in your `requirements.txt` file. If your app requires system-level packages, make sure to include a `packages.txt` file in your repository root with the required system packages listed there. Streamlit Sharing will install these system-level packages before running your app.

## Future Directions for Testing and Logging

To ensure the robustness and reliability of our object detection application as we move towards production, focusing on detailed testing and straightforward logging is crucial. Below are strategies to consider in future work:

### Unit Testing

Unit testing should cover fundamental functionality and edge cases, ensuring the system behaves as expected under a variety of inputs and conditions.

- **Functionality Tests:** Verify core functionalities such as image upload, model prediction, and result display operate correctly.
- **Edge Cases for Image Inputs:**
  - **Unsupported File Formats:** Test the application's ability to handle and notify users about unsupported image formats (e.g., TIFF, BMP).
  - **Corrupted Image Files:** Ensure the system gracefully handles corrupted images without crashing, providing a user-friendly error message.
  - **Large File Sizes:** Simulate uploads of excessively large images to test the system's capability to limit input sizes or efficiently process large files.

### Integration Testing

Integration testing should confirm that different parts of the application work together harmoniously.

- **Workflow Integration:** Confirm that the end-to-end process from image upload to prediction and visualization is seamless and bug-free.
- **User Interface and Experience:** Test the application's response to user interactions, such as adjusting confidence thresholds or selecting different image sources.

### Logging

Simple yet effective logging strategies are essential for monitoring the application's health and user activities.

- **Access Logs:** Record timestamps, IP addresses, and endpoints accessed to monitor application usage and detect unusual patterns that may indicate issues.
- **Error Logs:** Capture detailed error messages and stack traces for backend failures, such as model loading errors or prediction exceptions, to facilitate debugging.
- **Operational Metrics:** Log key operational metrics such as request processing time, memory usage, and CPU load to ensure the application's performance is within expected thresholds.

By addressing these edge cases through rigorous testing and implementing straightforward logging practices, we aim to build a resilient and user-friendly application ready for production deployment.

## More About this Project

For more details on the project's techniques, methods, or dataset, please see the following related repository:

- [Capstone_Object_Tracking_and_Detection_for_AV](https://github.com/RafaelaMartelo/Capstone_Object_Tracking_and_Detection_for_AV)

This repository includes additional documentation, dataset, and code used on the prototype development that complement the current project.

## Contributors

- Rafaela Martelo - [rafaelasofialm98@gmail.com](mailto:rafaelasofialm98@gmail.com)

## License

This project is licensed under the MIT License.

## Acknowledgments

This demo App was developed upon the [hello-streamlit](https://github.com/streamlit/hello-streamlit) sample provided by Streamlit. 
