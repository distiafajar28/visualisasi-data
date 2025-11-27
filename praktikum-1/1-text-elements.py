import streamlit as st
st.write("Hello")
st.write('World!!!')

st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""This is our Sub-Header""")
st.caption("""This is our Caption""")

st.text("Hi, \nPeople\t!!!!!!!!")
st.text('Welcome to')
st.text(""" Streamlit's World""")

st.markdown("# Hi,\n# ***People*** \t !!!!!!!")
st.markdown('## Welcome to')
st.markdown(""" Streamlit's World""")

st.latex(r'''cos2\theta = 1 - 2sin^\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''
         \frac{\partial u}
         {\partial t}) = h^2\left( 
         /frac{/partial^2 u}{\partial x^2} 
         + \frac{\partial^2 u}{\partial y^2}
         + \frac{\partial^2 u}{\partial z^2} \right)''')

st.subheader("""Python Code""")
code = '''def hello() :
print("Hello, Streamlit!")'''
st.code(code,  language='python')

st.subheader("""Java Code""")
st.code("""
public class GFG {
  Public static void main(String args[])})
    {
      System.out.print1n("Hello World");
    }
}""", language='java')
st.subheader("""JavaScript Code""")
st.code("""
<p id="demo"></p>
<script>
try {
  adddlert("Welcome guest!");
}
catch(err) {
  document.getElementById("demo").innerHTML = err.message;
}
</script> """, 'javascript')