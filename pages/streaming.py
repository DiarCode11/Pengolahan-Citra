import cv2
import numpy as np
import streamlit as st

def horizontal_flip (frame): 
    flipped_frame = cv2.flip(frame, 1)
    return flipped_frame

def vertical_flip (frame): 
    flipped_frame = cv2.flip(frame, 0)
    return flipped_frame

def grayscale_effect (frame): 
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(grayscale_frame, cv2.COLOR_GRAY2RGB)
    return frame

def negative_effect (frame): 
    return 255 - frame
    
def blackWhite_effect (frame): 
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)[1]# Melakukan invert pada gambar biner
    negative_binary_frame = cv2.bitwise_not(binary_frame)
    frame = cv2.cvtColor(negative_binary_frame, cv2.COLOR_GRAY2RGB)
    return frame

def sketch_effect (frame): 
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Konversi gambar ke dalam format grayscale
    inverted_frame = cv2.bitwise_not(gray_frame)# Inversi gambar (membuat efek negatif)
    blurred_frame = cv2.GaussianBlur(inverted_frame, (85, 85), 0) # Aplikasikan efek blur pada gambar
    sketched_frame = cv2.divide(gray_frame, 255 - blurred_frame, scale=256)# Menghasilkan efek sketsa dengan menggunakan operasi subtraksi
    frame = cv2.cvtColor(sketched_frame, cv2.COLOR_GRAY2RGB)
    return frame

def blur_effect(frame): 
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    return frame
    
def edge_effect(frame): 
    # Konversi gambar ke dalam format grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Terapkan operator Sobel pada gambar untuk mendeteksi tepi
    sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=5)
    # Gabungkan hasil dari operator Sobel
    edge_frame = cv2.sqrt(cv2.addWeighted(cv2.pow(sobel_x, 2.0), 1.0, cv2.pow(sobel_y, 2.0), 1.0, 0.0))
    # Konversi gambar kembali ke dalam skala 8-bit
    edge_frame = cv2.normalize(edge_frame, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    frame = cv2.cvtColor(edge_frame, cv2.COLOR_GRAY2RGB)
    return frame
    
def emboss_effect(frame): 
    # Kernel filter emboss
    kernel = np.array([[0, -1, -1],
                    [1,  0, -1],
                    [1,  1,  0]])
    # Terapkan filter emboss pada gambar
    frame = cv2.filter2D(frame, -1, kernel)
    return frame

def sepia_effect(frame): 
    # Matriks transformasi warna untuk efek sepia
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])
    # Terapkan transformasi warna untuk efek sepia
    sepia_frame = cv2.transform(frame, sepia_matrix)
    # Penanganan nilai piksel yang melebihi 255
    sepia_frame = np.where(sepia_frame > 255, 255, sepia_frame)
    frame = sepia_frame.astype(np.uint8)
    return frame
    
def heatmap_effect(frame): 
    # Terapkan filter Gaussian untuk memperhalus gambar
    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    
    # Tingkatkan kontras untuk menyoroti area yang lebih terang
    alpha = 3.0
    beta = -150
    frame = cv2.convertScaleAbs(blurred_frame, alpha=alpha, beta=beta)
    return frame
    
def main():
    st.title("Tampilan Langsung dari Kamera dengan OpenCV")
    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)

    # Periksa apakah kamera berhasil diinisialisasi
    if not cap.isOpened():
        st.error("Tidak dapat membuka kamera.")
        return

    # Menyiapkan wadah kosong untuk menampilkan frame
    frame_container = st.empty()
    
    st.sidebar.write("#### Pencerminan:")
    h_flip = st.sidebar.checkbox('Flip Horizontal')
    v_flip = st.sidebar.checkbox('Flip Vertikal')
    
    filter_type = st.sidebar.radio("Efek:", ["Gambar Asli", "Grayscale", "Negative", "Black and White", "Sketch", "Blur", "Edge", "Emboss", "Sepia", "Heatmap", ])
    
    # Loop untuk menampilkan frame dari kamera
    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()

        # Periksa apakah bacaan frame berhasil
        if not ret:
            st.error("Tidak dapat menerima frame.")
            break
        
        if h_flip: 
            frame = horizontal_flip(frame)
            
        if v_flip: 
            frame = vertical_flip(frame)
        
        # Gambar Asli
        if filter_type == 'Gambar Asli': 
            pass
        
        # Grayscale
        elif filter_type == 'Grayscale': 
            frame = grayscale_effect(frame)
            
        # Negative
        elif filter_type == 'Negative': 
            frame = negative_effect(frame)
            
        # Black and White
        elif filter_type == 'Black and White': 
            frame = blackWhite_effect(frame)
            
        elif filter_type == 'Sketch': 
            frame = sketch_effect(frame)
            
        elif filter_type == 'Blur': 
            frame = blur_effect(frame)
           
        elif filter_type == 'Edge': 
            frame = edge_effect(frame)
            
        elif filter_type == 'Emboss': 
            frame = emboss_effect(frame)
            
        elif filter_type == 'Sepia': 
            frame = sepia_effect(frame)
            
        elif filter_type == 'Heatmap': 
            frame = heatmap_effect(frame)
        
        # Tempat kosong untuk menampilkan frame 
        frame_container.image(frame, channels="BGR")
        
if __name__ == "__main__":
    main()
