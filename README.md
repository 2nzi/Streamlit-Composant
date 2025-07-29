# Streamlit Custom Component

Un composant Streamlit personnalisé pour le développement local.

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.8+
- Node.js 16+
- npm ou yarn

### Installation

1. **Installer les dépendances Python** :
   ```bash
   pip install -e .
   ```

2. **Installer les dépendances frontend** :
   ```bash
   cd streamlit_custom_component/frontend
   npm install
   ```

3. **Démarrer le serveur de développement frontend** :
   ```bash
   npm run start
   ```

4. **Lancer l'application Streamlit** (dans un autre terminal) :
   ```bash
   streamlit run example.py
   ```

## 🎯 Utilisation

```python
import streamlit as st
from streamlit_custom_component import custom_component

# Utiliser le composant
result = custom_component(
    message="Bonjour le monde !",
    color="blue"
)

# Afficher le résultat
if result:
    st.write(f"Nombre de clics : {result.get('clickCount', 0)}")
```

## 🛠️ Développement

### Mode Développement

Le composant est configuré pour fonctionner en mode développement par défaut. Pour modifier le composant :

1. **Modifiez le composant React** dans `streamlit_custom_component/frontend/src/CustomComponent.tsx`
2. **Modifiez l'API Python** dans `streamlit_custom_component/__init__.py`
3. **Voir les changements en temps réel** dans votre navigateur

### Structure du projet

```
streamlit-custom-component/
├── README.md
├── example.py
├── streamlit_custom_component/
│   ├── __init__.py
│   └── frontend/
│       ├── package.json
│       ├── src/
│       │   └── CustomComponent.tsx
│       └── build/
└── .gitignore
```

## 📚 Documentation

- **QUICKSTART.md** : Guide de démarrage rapide
- **DEVELOPMENT.md** : Guide de développement complet
- **example.py** : Exemple d'utilisation détaillé

## 🐛 Dépannage

### Erreurs communes

**"Module not found"**
```bash
pip install -e .
```

**"npm command not found"**
- Installez Node.js depuis https://nodejs.org/

**"Composant ne s'affiche pas"**
- Vérifiez que le serveur frontend tourne sur http://localhost:3001
- Vérifiez que `_RELEASE = False` dans `__init__.py`

## 📄 Licence

MIT License 