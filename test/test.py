import pytest
import streamlit as st
from meteo.main import text_input, button, metric  # Importez vos fonctions ici

# Test de la fonction text_input
def test_text_input():
    with st.empty():
        result = text_input("")
        assert result == "", "Le résultat attendu était 'Hello', mais le résultat obtenu était différent."

# Test de la fonction button
def test_button():
    with st.empty():
        result = button("search")
        assert result == False, "Le résultat attendu était 'True', mais le résultat obtenu était différent."

# Exécutez les tests avec pytest
if __name__ == "__main__":
    pytest.main()
