import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Judul aplikasi
st.title("Praktikum 5 - Matplotlib Scatter Plot")

# Identitas kelompok 
st.write("Kelompok 12 : ")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227 
""")

#Menu di sidebar
option = st.sidebar.selectbox(   
    "Pilih Visualisasi Scatter Plot:",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scater Plot",
        "3D Scatter Plot Analisis",
    )
)

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]
data = {
  'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
  'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
  'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
  'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
  'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# Scatter plot menggunaakn matplotlib
def basic_scatter():
    st.set_page_config(page_title="Basic Scatter Plot Penjualan Es Krim", layout="centered")
    st.subheader("Basic Scatter Plot")

    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='blue')
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')

    # Tampilkan di streamlit
    st.pyplot(fig)

def custom_scatter():
    st.set_page_config(page_title="Kustomisasi Scatter Plot Penjualan Es Krim", layout="centered")
    st.subheader("Kustomisasi Scatter Plot")
    
    # Kustomisasi scatter plot
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)

    # Tampilkan di streamlit
    st.pyplot(fig)

def multiple_scatter():
    # Data tambahan untuk kategori hari
    penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
    penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160 , 200]

    st.set_page_config(page_title="Multiple Scatter Plot Penjualan Es Krim", layout="centered")
    st.subheader("Multiple Scatter Plot")

    # Multiple scatter plot
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
    ax.set_title('Penjualan Es Krim Berdasarkan Hari')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.legend() 

    # Tampilkan di streamlit
    st.pyplot(fig)

def scatter_3_variabel():
  # Konversi data ke DataFrame
  df = pd.DataFrame(data)

  # Judul aplikasi
  st.set_page_config(page_title="Analisis Penjualan Es Krim", layout="centered")
  st.subheader('Analisis Penjualan Es Krim Berdasarkan Suhu')

  # Pilih jenis es krim
  jenis_eskrim = st.selectbox('Pilih Jenis Es Krim: ', ['Cokelat', 'Vanila', 'Stroberi'])

  # Menentukan kolom penjualan berdasarkan pilihan
  if jenis_eskrim == 'Cokelat':
      penjualan = df['Penjualan_Cokelat']
  elif jenis_eskrim == 'Vanila':
      penjualan = df['Penjualan_Vanila']
  else:
      penjualan = df['Penjualan_Stroberi']

  # Tampilkan tabel data
  st.subheader('Data penjualan dan Suhu')
  st.dataframe(df)

  # Membuat Scatter Plot
  fig, ax = plt.subplots()
  scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)
  ax.set_title(f'Hasil Penjualan Es Krim {jenis_eskrim} vs Suhu dan Kelembapan')
  ax.set_xlabel('Suhu (°C)')
  ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
  fig.colorbar(scatter, label='Kelembapan (%)')

  # Tampilkan scatter plot di Streamlit
  st.pyplot(fig)

def scatter_3d_analysis():
    st.set_page_config(page_title="3D Analisis Penjualan Es Krim", layout="centered")

    df = pd.DataFrame(data)
    # Judul dan pilihan jenis es krim
    st.subheader("Analisis 3D Penjualan Es Krim Berdasarkan Suhu dan Kelembapan")
    jenis_eskrim = st.selectbox("Pilih Jenis Es Krim:", ["Cokelat", "Vanila", "Stroberi"])

    if jenis_eskrim == "Cokelat":
      penjualan = df["Penjualan_Cokelat"]
    elif jenis_eskrim == "Vanila":
      penjualan = df["Penjualan_Vanila"]
    else:
      penjualan = df["Penjualan_Stroberi"]

    # Tampilkan tabel data
    st.subheader("Data Penjualan, Suhu, dan Kelembapan")
    st.dataframe(df)

    # Pengaturan gaya sederhana
    col1, col2 = st.columns(2)
    with col1:
      ukuran_titik = st.slider("Ukuran titik", 20, 300, 120, 10)
    with col2:
      opasitas = st.slider("Opasitas", 0.2, 1.0, 0.8, 0.05)
      
    # Scatter Plot 3D menggunakan mpl_toolkits.mplot3d
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    # Sumbu: X=Suhu, Y=Kelembapan, Z=Penjualan
    scatter = ax.scatter(
      df["Suhu"],
      df["Kelembapan"],
      penjualan,
      c=df["Kelembapan"],
      s=ukuran_titik,
      cmap="coolwarm",
      alpha=opasitas,
    )

    ax.set_title(f"Penjualan {jenis_eskrim} vs Suhu dan Kelembapan (3D)")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Kelembapan (%)")
    ax.set_zlabel(f"Penjualan {jenis_eskrim}")

    fig.colorbar(scatter, ax=ax, shrink=0.6, pad=0.1, label="Kelembapan (%)")

    st.pyplot(fig)
    
# Routing berdasarkan menu sidebar
if option == 'Basic Scatter Plot':
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scater Plot":
    scatter_3_variabel()
elif option == "3D Scatter Plot Analisis":
    scatter_3d_analysis()