import cv2
import numpy as np
import streamlit as st

def detect_faces(image):
    # Memuat detektor wajah yang telah dilatih sebelumnya
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Mengonversi gambar ke skala keabuan
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah dalam gambar
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Menggambar persegi panjang di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image

def main():
    st.title("Face Detection")
    st.write("Unggah gambar dan deteksi wajah")

    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Membaca gambar yang diunggah
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        st.image(image, caption="Gambar yang Diunggah", use_column_width=True)

        # Mendeteksi wajah dalam gambar
        detected_image = detect_faces(image)

        # Menampilkan gambar dengan wajah yang terdeteksi
        st.image(detected_image, caption="Wajah yang Terdeteksi", use_column_width=True)

if __name__ == "__main__":
    main()