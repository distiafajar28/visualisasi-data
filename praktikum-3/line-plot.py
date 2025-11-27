import streamlit as st
import matplotlib as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

st.title("Visualisasi Penjualan Product")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot",
    "Multiple &",
    "Costumizations",
    "Garis Untuk Menunjukkan Tren",
    "subplot"
))

st.caption("Praktikum-3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 12:
- Distia Fajar Familiati 0110222163
- Sabrina Ramadhani 0110222068
- Muhammad Faris Zacky 0110222227
""")

def line_plot(): 
    fig, ax = plt.sub()
    ax.plot(months, product_A_sales, label="Product A",
            color="pink", linestyle='--', marker='o')

    ax.set_title('Penjualan Product per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)


def customize_line_plot():
    fig, ax = plt.subplots()

    # Product A
    ax.plot(months, product_A_sales, label="Product A",
            color="pink", linestyle='--', marker='o')

    # Product B (harus pakai data yang beda)
    ax.plot(months, product_B_sales, label="Product B",
            color="blue", linestyle='-', marker='x')

    ax.set_title('Penjualan Product per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

if option == "Single Line Plot":
    line_plot()
elif option == "Costumizations":
    customize_line_plot()
elif option == "Multiple &":
    customize_line_plot()
elif option == "Garis Untuk Menunjukkan Tren":
    customize_line_plot()