import matplotlib.pyplot as plt

suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

plt.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
plt.title('Hubungan Penjualan Es Krim dan Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('Penjualan Es Krim')
plt.grid(True)
plt.show()