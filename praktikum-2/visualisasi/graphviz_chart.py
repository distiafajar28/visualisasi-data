import streamlit as st
import graphviz as graphviz

st.title("Grapviz Chart")
st.write("Kelompok: 12")
st.markdown("""
- Distia Fajar Familiati (0110222163)
- Sabrina Ramadhani (0110222068)
- Muhammad Faris Zacky (0110222227)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
                  
      }
""")

graph =graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')

st.graphviz_chart(graph)