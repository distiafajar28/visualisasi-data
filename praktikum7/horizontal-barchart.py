import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Praktikum 07 Visualisasi Data")
st.subheader("Horizontal Bar Chart  Stacked Horizontal Bar Chart")
st.write("Kelompok 12")
st.markdown("""
  - Distia Fajar Familiati 0110222163
  - Sabrina Ramadhani 0110222068
  - Muhammad Faris Zacky 0110222227
""")

brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 200]
sales_2024 = [380, 450, 320, 300]

y = np.arange(len(brands))
bar_width = 0.4

kategori = st.selectbox(
  "Pilih Kategori Visualisasi",
  ['Basic Barchart', 'Kustomisasi Grafik', 'Multiple Chart']
)

if kategori == "Basic Barchart":
  st.subheader("Horizontal Bar Chart Sederhana")
  fig1, ax1, = plt.subplots()

  ax1.set_yticks(y)
  ax1.set_yticklabels(brands)
  ax1.set_title('Horizontal Bar Chart - 2023')
  ax1.set_xlabel('Jumlah Penjualan')
  ax1.set_ylabel('Merk')
  ax1.barh(y, sales_2023, color='pink')
  st.pyplot(fig1)

  st.subheader("Horizontal Bar Chart Sederhana")
  fig2, ax2, = plt.subplots()
  ax2.set_yticks(y)
  ax2.set_yticklabels(brands)
  ax2.set_title('Stacked Horizontal Bar Chart - 2023')
  ax2.set_xlabel('Jumlah Penjualan')
  ax2.set_ylabel('Merk')
  ax2.barh(y, sales_2023, color='pink')
  ax2.barh(y, sales_2024, color='purple', label='2024', left=sales_2023)
  ax2.legend()
  st.pyplot(fig2)

elif kategori == "Kustomisasi Grafik":
  st.subheader("Kustomisasi Bar Chart Sederhana")
  fig3, ax3, = plt.subplots()
  ax3.set_yticks(y)
  ax3.set_yticklabels(brands)
  ax3.set_title('Stacked Kustomisasi Bar Chart - 2023')
  ax3.set_xlabel('Jumlah Penjualan')
  ax3.set_ylabel('Merk')
  ax3.barh(y, sales_2023, color='pink', edgecolor='black')
  ax3.grid(axis='x', linestyle='--', alpha=0.6)

  for i, v in enumerate(sales_2023):
    ax3.text(v+5,  i, str(v), va='center')
  st.pyplot(fig3)

  st.subheader("Kustomisasi Bar Chart Sederhana")
  fig4, ax4, = plt.subplots()
  ax4.set_yticks(y)
  ax4.set_yticklabels(brands)
  ax4.set_title('Stacked Horizontal Bar Chart - 2023')
  ax4.set_xlabel('Jumlah Penjualan')
  ax4.set_ylabel('Merk')
  ax4.barh(y, sales_2023, label='2023', color='skyblue', edgecolor='black')
  ax4.barh(y, sales_2024, label='2024', left=sales_2023, color='orange', edgecolor='black')
  ax4.grid(axis='x', linestyle='--', alpha=0.6)
  st.pyplot(fig4)

elif kategori == "Multiple Chart":
  st.subheader("Multiple Bar Chart Sederhana")
  fig5, ax5, = plt.subplots()
  ax5.set_yticks(y)
  ax5.set_yticklabels(brands)
  ax5.set_title('Multiple Horizontal Bar Chart - 2023')
  ax5.set_xlabel('Jumlah Penjualan')
  ax5.set_ylabel('Merk')
  ax5.barh(y - bar_width/2, sales_2023, label='2023', height=bar_width)
  ax5.barh(y + bar_width/2, sales_2024, label='2024', height=bar_width)
  ax5.grid(axis='x', linestyle='--', alpha=0.6)
  st.pyplot(fig5)

  st.subheader("Multiple Bar Chart Sederhana")
  fig6, ax6, = plt.subplots()
  ax6.set_yticks(y)
  ax6.set_yticklabels(brands)
  ax6.set_title('Multiple Horizontal Bar Chart - 2023')
  ax6.set_xlabel('Jumlah Penjualan')
  ax6.set_ylabel('Merk')
  ax6.barh(y, sales_2023, label='2023')
  ax6.barh(y, sales_2024, label='2024', left=sales_2023)
  ax6.legend()
  st.pyplot(fig6)