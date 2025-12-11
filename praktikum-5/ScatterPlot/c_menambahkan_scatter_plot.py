import matplotlib.pyplot as plt

suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]

# data tambahan untuk kategori hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160 , 200]

# Scatter plot multiple
plt.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
plt.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
plt.title('Penjualan Es Krim Berdasarkan Hari')
plt.xlabel('Suhu (°C)')
plt.ylabel('Penjualan Es Krim')
plt.legend()
plt.show()