import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

def compute_histogram(image):
    # Konversi gambar ke format NumPy array
    img_array = np.array(image)

    # Ambil histogram untuk setiap saluran warna (R, G, B)
    r_hist, _ = np.histogram(img_array[:,:,0], bins=256, range=[0,256])
    g_hist, _ = np.histogram(img_array[:,:,1], bins=256, range=[0,256])
    b_hist, _ = np.histogram(img_array[:,:,2], bins=256, range=[0,256])

    # Susun data histogram dalam DataFrame
    hist_data = pd.DataFrame({
        'Red': r_hist,
        'Green': g_hist,
        'Blue': b_hist
    })

    return hist_data

def main():
    st.title('RGB Color Histogram')

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Baca gambar yang diunggah
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Hitung histogram
        hist_data = compute_histogram(image)

        # Tampilkan histogram menggunakan st.line_chart
        st.subheader('RGB Color Histogram')
        st.line_chart(hist_data)

if __name__ == '__main__':
    main()
    