import streamlit as st
import cv2
from PIL import Image
import numpy as np

def rotate_image(image, angle):
    image_cv = np.array(image)
    (h, w) = image_cv.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image_cv, M, (w, h))
    return rotated_image

st.title("Simple Image Processing App")

# Suruh user memasukkan sebuah gambar atau image yang akan di rotate
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None: 
    image = Image.open(uploaded_file)
    
    st.image(image, caption="Original Image", use_column_width=True)
    
    rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
    
    if st.button("Rotate"):
        # Rotate the image
        rotated_image = rotate_image(image, rotation_angle)
        # Display the rotated image
        st.image(rotated_image, caption="Rotated Image", use_column_width=True)
