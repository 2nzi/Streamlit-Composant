import streamlit as st
from st_image_carousel import image_carousel

st.title("🧪 Test Simple du Composant")

st.write("Test avec un composant minimal:")

# Test avec des données simples
result = image_carousel(
    images=[
        {"name": "Test1", "url": "https://via.placeholder.com/100"},
        {"name": "Test2", "url": "https://via.placeholder.com/100"},
    ],
    key="test_simple"
)

st.write("Résultat du composant:", result) 