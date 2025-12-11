import matplotlib.pyplot as plt

suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# membuat scatter plot
plt.scatter(suhu, penjualan, color='blue')
plt.title('Hubungan Penjualan Es Krim dan Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('Penjualan Es Krim')
plt.show()