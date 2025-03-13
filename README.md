🔍 Real Time Object Detection using YOLOv8 and Streamlit
This repository contains a simple implementation of real-time object detection using YOLOv8 and Streamlit. It leverages the webcam to detect common objects in the environment and display the results live in a web interface.

🚀 Demo
Live Demo: Add your hosted link here if available

📦 Features
✅ Real-time object detection via webcam
✅ Fast and lightweight YOLOv8 (nano version) for better performance
✅ Interactive and easy-to-use Streamlit web app
✅ Object annotations displayed on video feed
🧰 Tech Stack
Python
Ultralytics YOLOv8 (for object detection)
Streamlit (for web interface)
OpenCV (for webcam feed handling)
📥 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/yolo-object-detection.git
cd yolo-object-detection
2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
Sample requirements.txt:

nginx
Copy
Edit
ultralytics
streamlit
opencv-python
numpy
▶️ How to Run
bash
Copy
Edit
streamlit run yolo_app.py
Make sure your webcam is connected and accessible.

📊 Model Info
Model Used: YOLOv8 Nano (yolov8n.pt)
Objects Detected: People, cars, animals, and other common objects (based on COCO dataset)
