import streamlit as st
from skimage.exposure import match_histograms 
import numpy as np
from PIL import Image
import io
import os

def histogram_matching(source: Image.Image, target: Image.Image):
    image1 = np.array(source).astype(np.uint8)
    image2 = np.array(target).astype(np.uint8)
    
    matched = match_histograms(image1, image2).astype(np.uint8)

    return Image.fromarray(matched)

def main():

    st.title("Histogram Matching")
    st.write("Upload foto yang ingin diubah ke mode warna yang sesuai.")

    cols = st.columns(2)
    with cols[0]:
        st.subheader("Original Image")
        input_image = st.file_uploader("Upload Input Image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
        if input_image is not None:
            input_image = Image.open(input_image)
            st.image(input_image)
    with cols[1]:
        st.subheader("Reference Image")
        reference_image = st.file_uploader("Upload Reference Image", type=["png", "png", "jpeg"], accept_multiple_files=False)
        if reference_image is not None:
            reference_image = Image.open(reference_image)
            st.image(reference_image)


    if input_image is not None and reference_image is not None:

        # Perform histogram matching
        colorized_img = histogram_matching(input_image, reference_image)

        # Convert image to CMYK
        colorized_img = colorized_img.convert("CMYK")

        # Convert CMYK to RGB for display
        colorized_img = colorized_img.convert("RGB")

        # Display images side by side for comparison
        st.subheader("Output Image")
        st.write("Berikut hasil dari proses histogram matching.")
        st.image(colorized_img, use_column_width=True)

        # Download colorized image
        download_button = st.button("Download Output Image")
        if download_button:
            # Convert the colorized image to bytes
            image_bytes = io.BytesIO()
            colorized_img.save(image_bytes, format='JPEG')
            image_bytes = image_bytes.getvalue()

            # Create 'downloaded' folder if it doesn't exist
            if not os.path.exists("downloaded"):
                os.makedirs("downloaded")

            # Save the image to 'downloaded' folder
            with open("downloaded/Colorized_Image.jpg", "wb") as f:
                f.write(image_bytes)

            # Offer the file download
            st.download_button(
                label="Download",
                data=image_bytes,
                file_name="Colorized_Image.jpg",
                mime="image/jpeg"
            )

if __name__ == "__main__":
    main()