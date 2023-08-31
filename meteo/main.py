import streamlit as st

st.title("METEO +")
st.markdown("---")

# Fonction qui crée un widget de pour renseigner le nom d'une ville
def text_input(text):
    return st.text_input(text)

#Crée un bouton de qui va requeter le nom de la ville a notre api
def button(butt):
    return st.button(butt)

#utilise les metric de notre api pour afficher la temperature et le type de ciel
def metric(label, value):
    return st.metric(label, value)



col1, col2 = st.columns(2)

with col1:
    text_input("City")

with col2:
    st.text("")
    st.text("")
    button("Search")

st.map()

col1, col2 = st.columns(2)

with col1:
    metric("Temp", "25 °C")
with col2:
    metric("Ciel", "Nuageux")
