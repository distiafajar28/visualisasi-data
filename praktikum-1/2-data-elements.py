import streamlit as st
import pandas as pd 
import numpy as  np
import matplotlib.pyplot as plt
import altair as alt

df = pd.DataFrame(
  np.random.randn(30,10),
  columns=('col_no %d' % i for i in range (10))) 
st.dataframe(df)

df = pd.DataFrame(
  np.random.randn(30, 10),
  columns=('col_no %d' % i for i in range(10)))
st.dataframe(df.style.highlight_min(axis=0))

df = pd.DataFrame(
  np.random.randn(30, 10),
  columns=('col_no %d' % i for i in range(10)))
st.table(df)

st.metric(label="Temperature", value="31 c",delta="1.2 c")
c1, c2, c3 = st.columns(3)
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Bilions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

df = pd.DataFrame(np.random.randn(30, 10),columns=('col_no %d' % i for i in range(10)))
st.write('Here is our Data', df, 'Data is in dataframe format. \n', "\nWrite is Super funcition")

df = pd.DataFrame(
  np.random.randn(10, 2),
  columns=['a', 'b'])

chart = alt.Chart(df).mark_bar().encode(
  x='a', y='b', tooltip=['a', 'b'])   
st.write(chart)

"Adding 5 & 4 =", 5+4
a = 5
'a', 
a
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""
df = pd.DataFrame({'col': [1,2]})
'dataframe', df 

s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
"chart", chart