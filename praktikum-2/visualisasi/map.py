import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 12")
st.markdown("""
- Distia Fajar Familiati (0110222163)
- Sabrina Ramadhani (0110222068)
- Muhammad Faris Zacky (0110222227)"""
)
df = pd.DataFrame(
  np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
  columns=["latitude", "longitude"]
)

st.map(df)