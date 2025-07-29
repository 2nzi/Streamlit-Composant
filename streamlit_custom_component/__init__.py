import os
import streamlit.components.v1 as components

# Déclarer le composant
_RELEASE = False  # Toujours en mode développement pour l'instant

if not _RELEASE:
    _component_func = components.declare_component(
        "custom_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend", "build")
    _component_func = components.declare_component("custom_component", path=build_dir)


def image_selector(images: list, selected_image: str = None, max_visible: int = 5, key=None):
    """
    Un composant Streamlit pour sélectionner des images avec style circulaire.
    
    Parameters:
    -----------
    images : list
        Liste des images avec format: [{"name": "nom_image", "url": "url_image"}, ...]
    selected_image : str
        Image actuellement sélectionnée (optionnel)
    max_visible : int
        Nombre maximum d'images visibles à la fois (défaut: 5)
    key : str
        Une clé unique pour le composant
    
    Returns:
    --------
    dict
        Les données retournées par le composant frontend
        {"selected_image": "nom_image", "selected_url": "url_image", "current_index": 0}
    """
    component_value = _component_func(
        images=images,
        selected_image=selected_image,
        max_visible=max_visible,
        key=key,
        default=None
    )
    
    return component_value 