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

# Utiliser le composant
result = image_selector(
    images=joueurs_images,
    selected_image=None,
    max_visible=5,
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

# Section d'informations
st.header("ℹ️ Comment Utiliser le Carrousel")

st.markdown("""
### Fonctionnalités :

1. **Navigation par clic** : Cliquez sur une image pour la centrer
2. **Navigation par flèches** : Utilisez les flèches qui apparaissent au survol
3. **Carrousel infini** : Navigation circulaire dans la liste
4. **Affichage intelligent** : Seules les images pertinentes sont visibles
5. **Feedback visuel** : L'image centrale est mise en évidence

### Dans votre code :

```python
import streamlit as st
from streamlit_custom_component import image_selector

# Vos images
images = [
    {"name": "Nom du joueur", "url": "URL_de_l_image"},
    # ... plus d'images
]

# Utiliser le composant
result = image_selector(images=images, key="mon_carousel")

# Récupérer la sélection
if result:
    nom_joueur = result["selected_image"]
    position = result["current_index"]
    # Faire votre logique de filtrage ici
```
""")