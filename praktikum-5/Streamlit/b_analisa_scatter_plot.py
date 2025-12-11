import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy
data = {
  'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
  'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
  'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
  'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
  'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Judul aplikasi
st.title('Analisis Penjualan Es Krim Berdasarkan Suhu')

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

# Ringkasan hubungan
st.subheader('Ringkasan Hubungan')
st.write(f"Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis_eskrim}**.")