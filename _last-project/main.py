import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Kelompok 12 - Dashboard Energi Industri Baja", layout="wide")

# 2. Load Data Function
@st.cache_data
def load_data():
    # Load dataset
    df = pd.read_csv("data/steel_industry_data_cleaned.csv")
    
    # Check and convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date']) 
    return df

# Load data
try:
    df = load_data()

# Handle file error or file not found error
except FileNotFoundError:
    st.error("File CSV tidak ditemukan! Pastikan nama file sesuai.")
    st.stop()

# 3. Sidebar - Filters
st.sidebar.header("Filter Data")

min_date = df['date'].min()
max_date = df['date'].max()
start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

all_loads = df['load_type'].unique()
selected_load = st.sidebar.multiselect("Pilih Tipe Beban (Load Type)", all_loads, default=all_loads)
colors = ['pink', 'red', 'yellow', 'green', 'purple']

filtered_df = df[
    (df['date'].dt.date >= start_date) & 
    (df['date'].dt.date <= end_date) &
    (df['load_type'].isin(selected_load))
]

# 4. Main Dashboard
st.title("🏭 Dashboard Konsumsi Energi Industri Baja")
st.write("Kelompok 12")
st.markdown("""
- Distia Fajar Familiati 0110222163
- Sabrina Ramadhani 0110222068
- Muhammad Faris Zacky 0110222227
""")
st.markdown("---")

# Key Metrics
st.subheader("Ringkasan Statistik")
col1, col2, col3 = st.columns(3)
total_kwh = filtered_df['usage_kwh'].sum()
avg_co2 = filtered_df['co2_emission'].mean()
max_kwh = filtered_df['usage_kwh'].max()

col1.metric("Total Konsumsi Listrik", f"{total_kwh:,.0f} kWh")
col2.metric("Rata-rata Emisi CO2", f"{avg_co2:.2f} ppm")
col3.metric("Konsumsi Tertinggi", f"{max_kwh:,.0f} kWh")

st.markdown("---")

# ROW 1: Heatmap & Pie Chart
c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("1. Korelasi Antar Variabel (Heatmap)")
    # Choose only numeric columns for correlation
    numeric_df = filtered_df.select_dtypes(include='number')
    corr = numeric_df.corr()
    fig_heat = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
    st.plotly_chart(fig_heat, use_container_width=True)

with c2:
    st.subheader("2. Komposisi Beban (Pie Chart)")
    fig_pie = px.pie(filtered_df, names='load_type', title="Proporsi Tipe Beban", hole=0.4, color_discrete_sequence=colors)
    st.plotly_chart(fig_pie, use_container_width=True)

# ROW 2: Bar Chart & Scatter Plot
c3, c4 = st.columns(2)

with c3:
    st.subheader("3. Rata-rata Konsumsi per Hari (Bar Chart)")
    avg_day = filtered_df.groupby('day_of_week')['usage_kwh'].mean().reset_index()
    # Sort days of the week
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    avg_day['day_of_week'] = pd.Categorical(avg_day['day_of_week'], categories=days_order, ordered=True)
    avg_day = avg_day.sort_values('day_of_week')
    fig_bar = px.bar(avg_day, x='day_of_week', y='usage_kwh', title="Rata-rata Usage per Hari", color_discrete_sequence=colors[1:3])
    st.plotly_chart(fig_bar, use_container_width=True)

with c4:
    st.subheader("4. Korelasi Listrik vs CO2 (Scatter Plot)")
    fig_scatter = px.scatter(filtered_df, x='usage_kwh', y='co2_emission', color='load_type', opacity=0.5, color_discrete_sequence=colors[4:5])
    st.plotly_chart(fig_scatter, use_container_width=True)

# ROW 3: Line Chart
st.subheader("5. Tren Konsumsi Listrik (Line Chart)")
# Grouping by date to get total usage per day
daily_usage = filtered_df.groupby(filtered_df['date'].dt.date)['usage_kwh'].sum().reset_index()
fig_line = px.line(daily_usage, x='date', y='usage_kwh', title="Total Usage per Hari", color_discrete_sequence=colors)
st.plotly_chart(fig_line, use_container_width=True)