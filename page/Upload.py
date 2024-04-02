import streamlit as st
import cv2
from PIL import Image
import numpy as np

# Fungsi untuk melakukan rotasi citra
def rotate_image(image, angle):
    rotated_image = cv2.rotate(image, angle)
    return rotated_image

# Fungsi untuk mengubah ruang warna citra
def convert_color(image, color_space):
    if color_space == 'Grayscale':
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return converted_image

# Fungsi untuk equalisasi histogram citra
def equalize_histogram(image):
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

# Fungsi untuk menampilkan histogram citra
def show_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist

# Fungsi utama aplikasi
def main():
    st.title("Aplikasi Operasi Citra Sederhana")

    st.sidebar.header("Pengaturan")
    image_file = st.sidebar.file_uploader("Upload file gambar", type=['jpg', 'png', 'jpeg'])

    if image_file is not None:
        image = Image.open(image_file)
        st.sidebar.image(image, caption='Gambar Asli', use_column_width=True)
        image_np = np.array(image)

        # Pilih operasi citra
        operation = st.sidebar.selectbox("Pilih operasi citra:", ["Rotasi", "Konversi Warna", "Equalisasi Histogram"])

        if operation == "Rotasi":
            angle = st.sidebar.slider("Sudut Rotasi", -180, 180, 0)
            rotated_image = rotate_image(image_np, angle)
            st.image(rotated_image, caption='Hasil Rotasi', use_column_width=True)

        elif operation == "Konversi Warna":
            color_space = st.sidebar.selectbox("Pilih ruang warna:", ["RGB", "Grayscale"])
            converted_image = convert_color(image_np, color_space)
            st.image(converted_image, caption='Hasil Konversi Warna', use_column_width=True)

        elif operation == "Equalisasi Histogram":
            equalized_image = equalize_histogram(image_np)
            st.image(equalized_image, caption='Hasil Equalisasi Histogram', use_column_width=True)

        # Tampilkan histogram jika dipilih
        show_hist = st.sidebar.checkbox("Tampilkan Histogram")
        if show_hist:
            histogram = show_histogram(image_np)
            st.bar_chart(histogram)

if __name__ == '__main__':
    main()
