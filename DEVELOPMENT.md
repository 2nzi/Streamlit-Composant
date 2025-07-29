# 🛠️ Guide de Développement - Streamlit Image Carousel

Ce guide vous accompagne dans le développement et la contribution au composant Streamlit Image Carousel.

## 📋 Prérequis

- **Python 3.8+**
- **Node.js 16+**
- **npm ou yarn**
- **Git**

## 🚀 Installation pour le développement

### 1. Cloner le repository
```bash
git clone https://github.com/yourusername/streamlit-image-carousel.git
cd streamlit-image-carousel
```

### 2. Installation des dépendances Python
```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Installer les dépendances
pip install -e .
pip install -r requirements.txt
```

### 3. Installation des dépendances frontend
```bash
cd streamlit_image_carousel/frontend
npm install
```

## 🔧 Mode Développement

### Démarrage du serveur frontend
```bash
cd streamlit_image_carousel/frontend
npm run dev
```
Le serveur frontend sera accessible sur `http://localhost:3001`

### Démarrage de l'application Streamlit
```bash
# Dans un autre terminal
streamlit run example.py
```

### Démarrage rapide avec le script
```bash
python start_dev.py
```

## 📁 Structure du Projet

```
streamlit-image-carousel/
├── README.md                 # Documentation principale
├── DEVELOPMENT.md           # Ce guide
├── LICENSE                  # Licence MIT
├── pyproject.toml          # Configuration du package
├── setup.py                # Script d'installation
├── requirements.txt        # Dépendances Python
├── start_dev.py           # Script de démarrage rapide
├── example.py             # Application d'exemple principale
├── example_image_selector.py  # Exemples simples
├── streamlit_image_carousel/  # Package principal
│   ├── __init__.py        # API Python
│   └── frontend/          # Application React
│       ├── package.json
│       ├── tsconfig.json
│       ├── vite.config.ts
│       ├── index.html
│       └── src/
│           ├── CustomComponent.tsx  # Composant principal
│           ├── index.tsx
│           └── main.tsx
└── venv/                  # Environnement virtuel Python
```

## 🎯 Architecture

### Backend (Python)
- **`__init__.py`** : Définit l'API publique du composant
- **`components.declare_component()`** : Déclare le composant Streamlit
- **Gestion des paramètres** : Validation et transmission au frontend

### Frontend (React + TypeScript)
- **`CustomComponent.tsx`** : Composant React principal
- **`withStreamlitConnection()`** : Connexion avec Streamlit
- **Gestion d'état** : `useState` pour l'index actif
- **Navigation** : Logique de carrousel infini
- **Styling** : CSS-in-JS avec personnalisation dynamique

## 🔄 Workflow de Développement

### 1. Modification du frontend
```bash
# Modifier le fichier
streamlit_image_carousel/frontend/src/CustomComponent.tsx

# Les changements sont automatiquement rechargés
# grâce au hot reload de Vite
```

### 2. Modification du backend
```bash
# Modifier le fichier
streamlit_image_carousel/__init__.py

# Redémarrer l'application Streamlit
# Ctrl+C puis streamlit run example.py
```

### 3. Test des modifications
- Ouvrir `http://localhost:8501` dans le navigateur
- Tester les nouvelles fonctionnalités
- Vérifier la console pour les erreurs

## 🧪 Tests

### Tests manuels
1. **Navigation** : Tester les flèches et les clics
2. **Personnalisation** : Tester tous les paramètres de couleur
3. **Responsive** : Tester sur différentes tailles d'écran
4. **Gestion d'erreurs** : Tester avec des URLs d'images invalides

### Tests automatisés (à implémenter)
```bash
# Tests Python
pytest tests/

# Tests frontend
npm test
```

## 📦 Build pour Production

### Build du frontend
```bash
cd streamlit_image_carousel/frontend
npm run build
```

### Configuration pour production
```python
# Dans __init__.py, changer :
_RELEASE = True
```

### Test du build
```bash
# Installer le package en mode développement
pip install -e .

# Tester avec l'exemple
streamlit run example.py
```

## 🚀 Publication

### 1. Préparation
```bash
# Mettre à jour la version dans pyproject.toml
# Mettre à jour le CHANGELOG.md
# Tester le build de production
```

### 2. Build et publication
```bash
# Build du package
python -m build

# Publication sur PyPI
twine upload dist/*
```

### 3. Vérification
```bash
# Installer depuis PyPI
pip install streamlit-image-carousel

# Tester l'installation
python -c "from streamlit_image_carousel import image_carousel; print('OK')"
```

## 🐛 Débogage

### Erreurs communes

#### "Module not found"
```bash
pip install -e .
```

#### "npm command not found"
- Installer Node.js depuis https://nodejs.org/

#### "Composant ne s'affiche pas"
- Vérifier que le serveur frontend tourne sur `http://localhost:3001`
- Vérifier que `_RELEASE = False` dans `__init__.py`

#### "Erreurs TypeScript"
```bash
cd streamlit_image_carousel/frontend
npm run build
```

### Outils de débogage

#### Frontend
- **React DevTools** : Extension navigateur
- **Console navigateur** : `F12` pour voir les erreurs
- **Network tab** : Vérifier les requêtes

#### Backend
- **Streamlit debug** : `streamlit run example.py --logger.level=debug`
- **Python debugger** : `import pdb; pdb.set_trace()`

## 📝 Contribution

### 1. Fork et clone
```bash
git clone https://github.com/yourusername/streamlit-image-carousel.git
cd streamlit-image-carousel
```

### 2. Créer une branche
```bash
git checkout -b feature/nouvelle-fonctionnalite
```

### 3. Développer
- Suivre les conventions de code
- Ajouter des tests si possible
- Documenter les nouvelles fonctionnalités

### 4. Commit et push
```bash
git add .
git commit -m "feat: ajouter nouvelle fonctionnalité"
git push origin feature/nouvelle-fonctionnalite
```

### 5. Pull Request
- Créer une PR sur GitHub
- Décrire les changements
- Attendre la review

## 📚 Ressources

- [Documentation Streamlit Components](https://docs.streamlit.io/library/advanced-features/streamlit-components)
- [React Documentation](https://reactjs.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Documentation](https://vitejs.dev/)

## 🤝 Support

- **Issues** : [GitHub Issues](https://github.com/yourusername/streamlit-image-carousel/issues)
- **Discussions** : [GitHub Discussions](https://github.com/yourusername/streamlit-image-carousel/discussions)
- **Email** : contact@example.com

---

**Happy coding! 🎨✨** 