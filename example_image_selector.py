import streamlit as st
from streamlit_custom_component import image_selector

st.set_page_config(page_title="Exemple Image Selector", page_icon="🎨")

st.title("🎨 Exemple d'utilisation du composant Image Selector")

# Données d'exemple
images = [
    {"name": "Lionel Messi", "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg"},
    {"name": "Cristiano Ronaldo", "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg"},
    {"name": "Kylian Mbappé", "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Kylian_Mbapp%C3%A9_2019.jpg"},
    {"name": "Erling Haaland", "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Erling_Haaland_2023.jpg"},
    {"name": "Neymar Jr", "url": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Neymar_Jr_2019.jpg"},
    {"name": "Kevin De Bruyne", "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Kevin_De_Bruyne_2019.jpg"},
    {"name": "Mohamed Salah", "url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Mohamed_Salah_2018.jpg"},
    {"name": "Robert Lewandowski", "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Robert_Lewandowski_2018.jpg"},
]

# Exemple 1: Configuration basique
st.header("1️⃣ Configuration basique")
result1 = image_selector(
    images=images,
    key="basic_example"
)

if result1:
    st.success(f"Joueur sélectionné : {result1['selected_image']}")

# Exemple 2: Configuration avec 7 joueurs visibles
st.header("2️⃣ Configuration avec 7 joueurs visibles")
result2 = image_selector(
    images=images,
    max_visible=7,
    key="seven_players"
)

if result2:
    st.success(f"Joueur sélectionné : {result2['selected_image']}")

# Exemple 3: Configuration avec couleurs personnalisées
st.header("3️⃣ Configuration avec couleurs personnalisées")
result3 = image_selector(
    images=images,
    max_visible=5,
    background_color="#0f0f23",
    active_border_color="#00ff88",
    active_glow_color="rgba(0, 255, 136, 0.6)",
    fallback_background="#1a1a2e",
    fallback_gradient_end="#0a0a1a",
    text_color="#ffffff",
    arrow_color="#00ff88",
    key="custom_colors"
)

if result3:
    st.success(f"Joueur sélectionné : {result3['selected_image']}")

# Exemple 4: Configuration thème clair
st.header("4️⃣ Configuration thème clair")
result4 = image_selector(
    images=images,
    max_visible=5,
    background_color="#f8fafc",
    active_border_color="#3b82f6",
    active_glow_color="rgba(59, 130, 246, 0.5)",
    fallback_background="#e2e8f0",
    fallback_gradient_end="#cbd5e1",
    text_color="#1e293b",
    arrow_color="#3b82f6",
    key="light_theme"
)

if result4:
    st.success(f"Joueur sélectionné : {result4['selected_image']}")

# Exemple 5: Configuration avec image présélectionnée
st.header("5️⃣ Configuration avec image présélectionnée")
result5 = image_selector(
    images=images,
    selected_image="Lionel Messi",
    max_visible=5,
    background_color="#1e3a8a",
    active_border_color="#fbbf24",
    active_glow_color="rgba(251, 191, 36, 0.7)",
    fallback_background="#3b82f6",
    fallback_gradient_end="#1e40af",
    text_color="#ffffff",
    arrow_color="#fbbf24",
    key="preselected"
)

if result5:
    st.success(f"Joueur sélectionné : {result5['selected_image']}")

# Affichage des résultats
st.header("📊 Résultats des sélections")

results = [result1, result2, result3, result4, result5]
names = ["Basique", "7 joueurs", "Couleurs perso", "Thème clair", "Présélectionné"]

for i, (result, name) in enumerate(zip(results, names)):
    if result:
        st.write(f"**{name}** : {result['selected_image']} (position {result['current_index'] + 1})")
    else:
        st.write(f"**{name}** : Aucune sélection")
