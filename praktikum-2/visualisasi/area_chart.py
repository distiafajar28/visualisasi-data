import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("Kelompok: 12")
st.markdown("""
- Distia Fajar Familiati (0110222163)
- Sabrina Ramadhani (0110222068)
- Muhammad Faris Zacky (0110222227)"""
)
df = pd.DataFrame(
  np.random.randn(40, 4),
  columns=("c1", "c2", "c3", "c4")
)

st.area_chart(df)