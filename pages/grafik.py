import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

#Grafik Garis

# Data
data = {
    'Merk Smartphone': ['Xiaomi', 'Realme', 'iPhone', 'ifinix'],
    'Harga Rata-Rata': [100, 120, 90, 70]
}

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Membuat grafik garis
plt.figure(figsize=(10, 6))
plt.plot(df['Merk Smartphone'], df['Harga Rata-Rata'], marker='o', color='b')
plt.title('Harga Smartphone')
plt.xlabel('Merk Smartphone')
plt.ylabel('Harga Rata-Rata')
plt.xticks(rotation=45)
plt.grid(True)

# Menampilkan grafik menggunakan Streamlit
st.pyplot(plt)


