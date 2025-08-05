import streamlit as st
from st_image_carousel import image_carousel

st.set_page_config(
    page_title="Carrousel de Joueurs Infini",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Carrousel de Joueurs Infini")

st.markdown("""
Ce composant permet de naviguer dans un carrousel infini de joueurs.
Cliquez sur une image pour la centrer, ou utilisez les flèches pour naviguer !
""")

import base64
from PIL import Image
import io

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode()}"

# Exemple d'images de joueurs
joueurs_images = [
    {
        "name": "Antoine Dupont",
        "url": image_to_base64(r"C:\Users\antoi\Documents\Work_Learn\Rugby\data\player_images\AD.jpg")
    },
    {
        "name": "Lionel Messi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg"
    },
    {
        "name": "Cristiano Ronaldo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg"
    },
    {
        "name": "Kylian Mbappé",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Kylian_Mbapp%C3%A9_2019.jpg"
    },
    {
        "name": "Erling Haaland",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Erling_Haaland_2023.jpg"
    },
    {
        "name": "Neymar Jr",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Neymar_Jr_2019.jpg"
    },
    {
        "name": "Kevin De Bruyne",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Kevin_De_Bruyne_2019.jpg"
    },
    {
        "name": "Mohamed Salah",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Mohamed_Salah_2018.jpg"
    },
    {
        "name": "Robert Lewandowski",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Robert_Lewandowski_2018.jpg"
    },
    {
        "name": "Karim Benzema",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Karim_Benzema_2018.jpg"
    },
    {
        "name": "Harry Kane",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/2018-07-07_Sweden_v_England_FIFA_World_Cup_2018_%28cropped%29.jpg"
    },
    {
        "name": "Vinícius Jr",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/76/Vin%C3%ADcius_J%C3%BAnior_2023.jpg"
    },
    {
        "name": "Jude Bellingham",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Jude_Bellingham_2023.jpg"
    }
]

# Section du composant
st.header("🎯 Carrousel de Joueurs")

# Paramètres de personnalisation
st.subheader("🎨 Personnalisation")

col1, col2 = st.columns(2)

with col1:
    max_visible = st.slider("Nombre de joueurs visibles", 3, 9, 5, 2)
    background_color = st.color_picker("Couleur de fond", "#ffffff")
    active_border_color = st.color_picker("Couleur bordure active", "#000000")
    text_color = st.color_picker("Couleur du texte", "#000000")

with col2:
    orientation = st.selectbox(
        "Orientation du carrousel",
        ["horizontal", "vertical"],
        help="Choisissez l'orientation d'affichage du carrousel"
    )
    active_glow_color = st.color_picker("Couleur lueur active", "#ffffff", help="Couleur de l'effet de lueur autour du joueur sélectionné")
    fallback_background = st.color_picker("Couleur fond fallback", "#ffffff")
    fallback_gradient_end = st.color_picker("Couleur fin gradient", "#ffffff")
    arrow_color = st.color_picker("Couleur des flèches", "#31333f", help="Couleur des flèches de navigation")

# Utiliser le composant avec personnalisation
result = image_carousel(
    images=joueurs_images,
    selected_image=None,
    max_visible=max_visible,
    orientation=orientation,
    background_color=background_color,
    active_border_color=active_border_color,
    active_glow_color=f"rgba({int(active_glow_color[1:3], 16)}, {int(active_glow_color[3:5], 16)}, {int(active_glow_color[5:7], 16)}, 0.5)",
    fallback_background=fallback_background,
    fallback_gradient_end=fallback_gradient_end,
    text_color=text_color,
    arrow_color=arrow_color,
    key="joueur_carousel"
)

#  NOUVELLE SECTION : Barre de recherche
st.header("🔍 Recherche de Joueurs")

# Barre de recherche
search_term = st.text_input(
    "Rechercher un joueur par nom :",
    placeholder="Ex: Messi, Dupont, Ronaldo...",
    help="Tapez le nom ou une partie du nom du joueur"
)

# Fonction de recherche
def search_players(players_list, search_term):
    """Recherche des joueurs par nom"""
    if not search_term:
        return []
    
    search_term = search_term.lower().strip()
    results = []
    
    for i, player in enumerate(players_list):
        if search_term in player["name"].lower():
            results.append({
                "index": i,
                "name": player["name"],
                "url": player["url"]
            })
    
    return results

# Afficher les résultats de recherche
if search_term:
    search_results = search_players(joueurs_images, search_term)
    
    if search_results:
        st.success(f"✅ {len(search_results)} joueur(s) trouvé(s) pour '{search_term}'")
        
        # Afficher les résultats dans des colonnes
        cols = st.columns(min(3, len(search_results)))
        
        for i, result in enumerate(search_results):
            with cols[i % 3]:
                st.markdown(f"**{result['name']}**")
                st.markdown(f"Position dans le carrousel: {result['index'] + 1}")
                
                # Bouton pour centrer le joueur dans le carrousel
                if st.button(f"Centrer {result['name']}", key=f"center_{i}"):
                    st.session_state.selected_player_index = result['index']
                    st.rerun()
    else:
        st.warning(f"❌ Aucun joueur trouvé pour '{search_term}'")
        
        # Suggestions de recherche
        st.info("💡 Suggestions :")
        all_names = [player["name"] for player in joueurs_images]
        suggestions = [name for name in all_names if any(letter in name.lower() for letter in search_term.lower())]
        
        if suggestions:
            st.write("Joueurs similaires :")
            for suggestion in suggestions[:5]:  # Limiter à 5 suggestions
                st.write(f"• {suggestion}")
        else:
            st.write("Essayez avec un nom plus court ou vérifiez l'orthographe")

# Section des résultats du carrousel
st.header("📊 Informations du Joueur Sélectionné")

if result is not None:
    st.success("✅ Joueur sélectionné !")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Nom du Joueur", result.get("selected_image", "Aucun"))
    
    with col2:
        st.metric("Position", result.get("current_index", 0) + 1)
    
    with col3:
        st.metric("Total Joueurs", len(joueurs_images))
    
    # Afficher l'image du joueur sélectionné
    if result.get("selected_url"):
        st.subheader("🖼️ Image du joueur sélectionné")
        st.image(result["selected_url"], width=200)
else:
    st.info(" Cliquez sur un joueur dans le carrousel pour voir ses informations")

# Comparaison des orientations
st.header("🔄 Comparaison des Orientations")

st.markdown("""
Voici une comparaison des deux orientations disponibles :
- **Horizontal** : Affichage classique de gauche à droite
- **Vertical** : Affichage de haut en bas, idéal pour les espaces étroits
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📏 Orientation Horizontale")
    result_horizontal = image_carousel(
        images=joueurs_images[:7],  # Limiter pour l'exemple
        selected_image=None,
        max_visible=5,
        orientation="horizontal",
        background_color="#f0f0f0",
        active_border_color="#007bff",
        active_glow_color="rgba(0, 123, 255, 0.5)",
        fallback_background="#e9ecef",
        fallback_gradient_end="#dee2e6",
        text_color="#212529",
        arrow_color="#6c757d",
        key="horizontal_example"
    )

with col2:
    st.subheader("📐 Orientation Verticale")
    result_vertical = image_carousel(
        images=joueurs_images[:7],  # Limiter pour l'exemple
        selected_image=None,
        max_visible=5,
        orientation="vertical",
        background_color="#f8f9fa",
        active_border_color="#28a745",
        active_glow_color="rgba(40, 167, 69, 0.5)",
        fallback_background="#d4edda",
        fallback_gradient_end="#c3e6cb",
        text_color="#155724",
        arrow_color="#6c757d",
        key="vertical_example"
    )

# 📊 Statistiques
st.header("📈 Statistiques")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de joueurs", len(joueurs_images))
    
with col2:
    # Compter les joueurs par nationalité (exemple)
    nationalities = {
        "France": len([p for p in joueurs_images if "Dupont" in p["name"]]),
        "Argentine": len([p for p in joueurs_images if "Messi" in p["name"]]),
        "Portugal": len([p for p in joueurs_images if "Ronaldo" in p["name"]]),
    }
    st.metric("Joueurs français", nationalities.get("France", 0))
    
with col3:
    st.metric("Joueurs visibles", max_visible)