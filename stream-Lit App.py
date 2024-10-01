# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:35:06 2024

@author: KRITHICK BALAJI
"""

import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import cv2

# Load the trained model
model = load_model('/content/drive/MyDrive/nested_unet_model.h5')  # Change to your desired model

def preprocess_image(image):
    img = cv2.resize(image, (256, 256))  # Resize to model input size
    img = img / 255.0  # Normalize
    return np.expand_dims(img, axis=0)  # Add batch dimension

# Streamlit UI
st.title("Brain MRI Segmentation")
uploaded_file = st.file_uploader("Choose an image...", type=["tif", "jpg", "png"])

if uploaded_file is not None:
    image = cv2.imread(uploaded_file.name)  # Read image file
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    if st.button("Predict"):
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)  # Perform prediction
        prediction = (prediction.squeeze() > 0.5).astype(np.uint8) * 255  # Thresholding
        
        st.image(prediction, caption='Predicted Mask', use_column_width=True)
