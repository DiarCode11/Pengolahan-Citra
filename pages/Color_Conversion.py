import streamlit as st
from PIL import Image
import os
import base64
import io

# to process image based on mode
def process_image(image, mode):
    if mode == "Gambar Asli": 
        return image
    elif mode == "Merah":
        if image.mode == 'RGB':
            r, g, b = image.split()
            r = r.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna merah
            g = g.point(lambda i: 0)       # Meniadakan intensitas warna hijau
            b = b.point(lambda i: 0)       # Meniadakan intensitas warna biru
            return Image.merge("RGB", (r, g, b))
        else:
            st.error("Mode warna merah hanya berlaku untuk gambar RGB.")
            return image
    elif mode == "Biru":
        if image.mode == 'RGB':
            r, g, b = image.split()
            r = r.point(lambda i: 0)       # Meniadakan intensitas warna merah
            g = g.point(lambda i: 0)       # Meniadakan intensitas warna hijau
            b = b.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna biru
            return Image.merge("RGB", (r, g, b))
        else:
            st.error("Mode warna biru hanya berlaku untuk gambar RGB.")
            return image
    elif mode == "Hijau":
        if image.mode == 'RGB':
            r, g, b = image.split()
            r = r.point(lambda i: 0)       # Meniadakan intensitas warna merah
            g = g.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna hijau
            b = b.point(lambda i: 0)       # Meniadakan intensitas warna biru
            return Image.merge("RGB", (r, g, b))
        else:
            st.error("Mode warna hijau hanya berlaku untuk gambar RGB.")
            return image
    elif mode == "Cyan":
        if image.mode == 'RGB':
            r, g, b = image.split()
            r = r.point(lambda i: 0)       # Meniadakan intensitas warna merah
            g = g.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna hijau
            b = b.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna biru
            return Image.merge("RGB", (r, g, b))
        else:
            st.error("Mode cyan hanya berlaku untuk gambar RGB.")
            return image
    elif mode == "Magenta":
        if image.mode == 'RGB':
            r, g, b = image.split()
            r = r.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna merah
            g = g.point(lambda i: 0)       # Meniadakan intensitas warna hijau
            b = b.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna biru
            return Image.merge("RGB", (r, g, b))
        else:
            st.error("Mode magenta hanya berlaku untuk gambar RGB.")
            return image
    elif mode == "Kuning":
        if image.mode == 'RGB':
            r, g, b = image.split()
            r = r.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna merah
            g = g.point(lambda i: i * 1.5)  # Meningkatkan intensitas warna hijau
            b = b.point(lambda i: 0)       # Meniadakan intensitas warna biru
            return Image.merge("RGB", (r, g, b))
        else:
            st.error("Mode kuning hanya berlaku untuk gambar RGB.")
            return image
    elif mode == "Grayscale":
        return image.convert("L")
    elif mode == "Binary":
        return image.convert("1")
    
def main():
    st.title("Color Conversion")
    st.write("Pilih foto berwarna yang dapat diubah ke mode warna yang sesuai. Untuk mengubah mode RGB, memungkinkan memakai foto dengan based warna RGB juga.")

    # Upload image
    uploaded_file = st.file_uploader("Upload Foto", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    # Process image if uploaded
    if uploaded_file:
        # Load uploaded image
        img = Image.open(uploaded_file)

        # Display processing options
        mode = st.selectbox("Pilih Mode Pengolahan", ["Gambar Asli","Merah", "Kuning", "Hijau", "Biru", "Cyan", "Magenta", "Grayscale", "Binary"])

        # Process image based on selected mode
        processed_img = process_image(img, mode)

        # Display processed image
        st.image(processed_img, caption=f"Foto dengan mode {mode}", use_column_width=True)

        rgb_image = processed_img.convert("RGB")
        
        # Convert the colorized image to bytes
        image_bytes = io.BytesIO()
        rgb_image.save(image_bytes, format='JPEG')
        image_bytes = image_bytes.getvalue()

        # Offer the file download
        st.download_button(
            label="Download",
            data=image_bytes,
            file_name="Conversion_Image.jpg",
            mime="image/jpeg"
        )

# Function to create a download link for files
# def get_binary_file_downloader_html(file_path, file_label='File'):
#     with open(file_path, 'rb') as f:
#         data = f.read()
#     b64 = base64.b64encode(data).decode()
#     return f'<a href="data:file/jpg;base64,{b64}" download="{os.path.basename(file_path)}">{file_label}</a>'

if __name__ == "__main__":
    main()
