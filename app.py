import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np

# Streamlit App
st.title("Real-time Object Detection with YOLOv8 by Kaustubh Jadhav")
run = st.checkbox('Run Camera')
FRAME_WINDOW = st.image([])

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Use lightweight version for faster performance

# Access Webcam
cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to grab frame.")
        break

    # Object Detection
    results = model.predict(frame)
    annotated_frame = results[0].plot()

    # Convert BGR (OpenCV format) to RGB (Streamlit expects)
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    # Display in Streamlit
    FRAME_WINDOW.image(annotated_frame)

cap.release()
