import streamlit as st
from skimage.exposure import match_histograms 
import numpy as np
from PIL import Image
import io

def histogram_matching(source: Image.Image, target: Image.Image):
    image1 = np.array(source).astype(np.uint8)
    image2 = np.array(target).astype(np.uint8)
    
    matched = match_histograms(image1, image2, channel_axis=-1).astype(np.uint8)

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
        reference_image = st.file_uploader("Upload Reference Image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
        if reference_image is not None:
            reference_image = Image.open(reference_image)
            st.image(reference_image)


    if input_image is not None and reference_image is not None:
        # Convert both images to the same mode
        input_image = input_image.convert(reference_image.mode)

        # Perform histogram matching
        colorized_img = histogram_matching(input_image, reference_image)

        # Display the output image
        st.subheader("Output Image")
        st.write("Berikut hasil dari proses histogram matching.")
        st.image(colorized_img, use_column_width=True)

        
        rgb_image = colorized_img.convert("RGB")
        
        # Convert the colorized image to bytes
        image_bytes = io.BytesIO()
        rgb_image.save(image_bytes, format='JPEG')
        image_bytes = image_bytes.getvalue()

        # Offer the file download
        st.download_button(
            label="Download",
            data=image_bytes,
            file_name="Colorized_Image.jpg",
            mime="image/jpeg"
        )

if __name__ == "__main__":
    main()