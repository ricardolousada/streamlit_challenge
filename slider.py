# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:28:36 2024

@author: ricar
"""

import streamlit as st
from datetime import time, datetime

st.header("st.slider")


# Exemplo 1

st.subheader("Slider")

age = st.slider("Quantos anos tens?",0,130,25)
st.write("Eu tenho", age, "anos")

# Exemplo 2

st.subheader("Slider de intervalo")

values = st.slider(
    'Escolha um intervalo de valores',\
        0.0,100.0, (25.0,75.0))

st.write(values)

# Exemplo 3

st.subheader("Slider de intervalo de tempo")

appointment = st.slider(
    "Agende um compromisso:",\
        value = (time(11,30), time(12,45)))

st.write("O compromisso foi agendado para:", appointment)

# Exemplo 4

st.header("Slider de data e hora")

start_time = st.slider(
    "Quando vais começar?",
    value = datetime(2020,1,1,9,30),
    format = "MM/DD/YY - hh:mm")

st.write("Inicio:", start_time)

# more about this- https://docs.streamlit.io/library/api-reference/widgets/st.select_slider