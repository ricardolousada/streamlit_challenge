import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")

#Exemplo 1

st.write("Hello, *World!* :sunglasses:")

# Exemplo 2

st.write(1234)

# Exemplo 3

df = pd.DataFrame({
    'first collumn': [1,2,3,4],
    'second collumn': [10,20,30,40]
})

st.write(df)

# Exemplo 4

st.write("Below is a DataFrame:", df, "Above is a datafram.")

# Exemplo 5

df2 = pd.DataFrame(
np.random.rand(200,3),
    columns = ['a','b','c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y = 'b', size = 'c', color = 'c', tooltip=['a','b','c'])

st.write(c)


"""
Além do st.write, você pode explorar outras maneiras de exibir texto:

st.markdown
st.header
st.subheader
st.caption
st.text
st.latex
st.code
"""