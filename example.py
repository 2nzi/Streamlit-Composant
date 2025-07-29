import streamlit as st
from streamlit_custom_component import image_selector

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

# Exemple d'images de joueurs (plus d'images pour tester le carrousel)
joueurs_images = [
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
    background_color = st.color_picker("Couleur de fond", "#1a1a2e")
    active_border_color = st.color_picker("Couleur bordure active", "#ffffff")
    text_color = st.color_picker("Couleur du texte", "#ffffff")

with col2:
    active_glow_color = st.color_picker("Couleur lueur active", "#ffffff", help="Couleur de l'effet de lueur autour du joueur sélectionné")
    fallback_background = st.color_picker("Couleur fond fallback", "#2a2a3e")
    fallback_gradient_end = st.color_picker("Couleur fin gradient", "#000000")
    arrow_color = st.color_picker("Couleur des flèches", "#ffffff", help="Couleur des flèches de navigation")

# Utiliser le composant avec personnalisation
result = image_selector(
    images=joueurs_images,
    selected_image=None,
    max_visible=max_visible,
    background_color=background_color,
    active_border_color=active_border_color,
    active_glow_color=f"rgba({int(active_glow_color[1:3], 16)}, {int(active_glow_color[3:5], 16)}, {int(active_glow_color[5:7], 16)}, 0.5)",
    fallback_background=fallback_background,
    fallback_gradient_end=fallback_gradient_end,
    text_color=text_color,
    arrow_color=arrow_color,
    key="joueur_carousel"
)

# Section des résultats
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
    
    # Afficher l'image sélectionnée
    if result.get("selected_url"):
        st.subheader("🖼️ Image Sélectionnée")
        st.image(result.get("selected_url"), width=200)
    
    # Exemple de filtre basé sur la sélection
    st.subheader("🔍 Statistiques du Joueur")
    
    joueur_selectionne = result.get("selected_image")
    if joueur_selectionne:
        # Simuler des données de statistiques
        stats = {
            "Lionel Messi": {"buts": 800, "passes": 350, "trophées": 44},
            "Cristiano Ronaldo": {"buts": 850, "passes": 250, "trophées": 35},
            "Kylian Mbappé": {"buts": 300, "passes": 150, "trophées": 15},
            "Erling Haaland": {"buts": 200, "passes": 50, "trophées": 8},
            "Neymar Jr": {"buts": 400, "passes": 200, "trophées": 25},
            "Kevin De Bruyne": {"buts": 150, "passes": 300, "trophées": 12},
            "Mohamed Salah": {"buts": 250, "passes": 120, "trophées": 18},
            "Robert Lewandowski": {"buts": 600, "passes": 100, "trophées": 30},
            "Karim Benzema": {"buts": 450, "passes": 180, "trophées": 28},
            "Harry Kane": {"buts": 350, "passes": 90, "trophées": 20},
            "Vinícius Jr": {"buts": 150, "passes": 80, "trophées": 10},
            "Jude Bellingham": {"buts": 100, "passes": 120, "trophées": 5}
        }
        
        if joueur_selectionne in stats:
            joueur_stats = stats[joueur_selectionne]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("⚽ Buts", joueur_stats["buts"])
            with col2:
                st.metric("🎯 Passes", joueur_stats["passes"])
            with col3:
                st.metric("🏆 Trophées", joueur_stats["trophées"])
        else:
            st.info("Statistiques non disponibles pour ce joueur")
    
    # Afficher les données brutes
    with st.expander("🔍 Données brutes du composant"):
        st.json(result)
else:
    st.info("👆 Cliquez sur une image de joueur pour voir les informations !")

# Section d'exemples
st.header("🎨 Exemples de Configurations")

# Exemple 1: Thème sombre
st.subheader("🌙 Thème Sombre")
with st.expander("Configuration sombre élégante"):
         st.code("""
result = image_selector(
    images=joueurs_images,
    max_visible=7,
    background_color="#0f0f23",
    active_border_color="#00ff88",
    active_glow_color="rgba(0, 255, 136, 0.6)",
    fallback_background="#1a1a2e",
    fallback_gradient_end="#0a0a1a",
    text_color="#ffffff",
    arrow_color="#00ff88"
)
""")

# Exemple 2: Thème sportif
st.subheader("⚽ Thème Sportif")
with st.expander("Configuration aux couleurs du football"):
         st.code("""
result = image_selector(
    images=joueurs_images,
    max_visible=5,
    background_color="#1e3a8a",
    active_border_color="#fbbf24",
    active_glow_color="rgba(251, 191, 36, 0.7)",
    fallback_background="#3b82f6",
    fallback_gradient_end="#1e40af",
    text_color="#ffffff",
    arrow_color="#fbbf24"
)
""")

# Exemple 3: Thème moderne
st.subheader("✨ Thème Moderne")
with st.expander("Configuration moderne et minimaliste"):
         st.code("""
result = image_selector(
    images=joueurs_images,
    max_visible=9,
    background_color="#f8fafc",
    active_border_color="#3b82f6",
    active_glow_color="rgba(59, 130, 246, 0.5)",
    fallback_background="#e2e8f0",
    fallback_gradient_end="#cbd5e1",
    text_color="#1e293b",
    arrow_color="#3b82f6"
)
""")

# Section d'informations
st.header("ℹ️ Comment Utiliser le Carrousel")

st.markdown("""
### Fonctionnalités :

1. **Navigation par clic** : Cliquez sur une image pour la centrer
2. **Navigation par flèches** : Utilisez les flèches qui apparaissent au survol
3. **Carrousel infini** : Navigation circulaire dans la liste
4. **Affichage intelligent** : Seules les images pertinentes sont visibles
5. **Feedback visuel** : L'image centrale est mise en évidence

### Paramètres disponibles :

```python
result = image_selector(
    # Paramètres obligatoires
    images=images,                    # Liste des images avec name et url
    key="mon_carousel",              # Clé unique pour Streamlit
    
    # Paramètres optionnels
    selected_image=None,              # Image présélectionnée par nom
    max_visible=5,                    # Nombre de joueurs visibles (3-9)
    
    # Personnalisation des couleurs
    background_color="#1a1a2e",       # Couleur de fond du composant
    active_border_color="#ffffff",    # Couleur de la bordure du joueur actif
    active_glow_color="rgba(255, 255, 255, 0.5)",  # Couleur de l'effet de lueur
    fallback_background="#2a2a3e",    # Couleur de fond des fallbacks
    fallback_gradient_end="rgb(0, 0, 0)",  # Couleur de fin du gradient
    text_color="#ffffff",              # Couleur du texte
    arrow_color="#ffffff"              # Couleur des flèches
)
```

### Exemples d'utilisation :

```python
# Configuration basique
result = image_selector(images=images, key="basic")

# Configuration personnalisée
result = image_selector(
    images=images,
    max_visible=7,
    background_color="#0f0f23",
    active_border_color="#00ff88",
    active_glow_color="rgba(0, 255, 136, 0.6)",
    arrow_color="#00ff88",
    key="custom"
)

# Configuration pour thème clair
result = image_selector(
    images=images,
    background_color="#f8fafc",
    active_border_color="#3b82f6",
    text_color="#1e293b",
    arrow_color="#3b82f6",
    key="light_theme"
)
```
""")