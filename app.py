import streamlit as st
import random

elements = {
    "H": "Hidrógeno",
    "He": "Helio",
    "Li": "Litio",
    "Be": "Berilio",
    "B": "Boro",
    "C": "Carbono",
    "N": "Nitrógeno",
    "O": "Oxígeno",
    "F": "Flúor",
    "Ne": "Neón"
}

st.title("Juego de Elementos Químicos")

symbol, name = random.choice(list(elements.items()))
st.write(f"¿Cuál es el nombre del elemento químico con símbolo: **{symbol}**?")

user_input = st.text_input("Tu respuesta:", "")

if st.button("Verificar"):
    if user_input.strip().lower() == name.lower():
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta es: {name}")
