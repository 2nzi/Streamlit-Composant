# Guide de Développement

Ce guide vous explique comment développer, tester et publier votre composant Streamlit personnalisé.

## 🚀 Démarrage Rapide

### Prérequis

- **Python 3.8+**
- **Node.js 16+**
- **npm ou yarn**

### Installation

1. **Cloner le repository**
   ```bash
   git clone <votre-repo>
   cd streamlit-custom-component
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   # Sur Windows
   venv\Scripts\activate
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances Python**
   ```bash
   pip install -e .
   ```

4. **Installer les dépendances frontend**
   ```bash
   cd streamlit_custom_component/frontend
   npm install
   ```

## 🛠️ Développement

### Mode Développement

1. **Démarrer le serveur de développement frontend**
   ```bash
   cd streamlit_custom_component/frontend
   npm run start
   ```
   Le serveur démarre sur `http://localhost:3001`

2. **Modifier le mode de développement dans Python**
   Dans `streamlit_custom_component/__init__.py`, changez :
   ```python
   _RELEASE = False  # Au lieu de True
   ```

3. **Lancer l'application Streamlit**
   ```bash
   streamlit run example.py
   ```

### Structure des Fichiers

```
streamlit-custom-component/
├── setup.py                          # Configuration du package
├── pyproject.toml                    # Configuration moderne
├── README.md                         # Documentation utilisateur
├── DEVELOPMENT.md                    # Ce guide
├── example.py                        # Exemple d'utilisation
├── build.py                          # Script de build automatisé
├── streamlit_custom_component/
│   ├── __init__.py                   # API Python du composant
│   └── frontend/
│       ├── package.json              # Dépendances npm
│       ├── vite.config.ts            # Configuration Vite
│       ├── tsconfig.json             # Configuration TypeScript
│       ├── index.html                # Page HTML de développement
│       └── src/
│           ├── CustomComponent.tsx   # Composant React principal
│           ├── index.tsx             # Point d'entrée pour le build
│           └── main.tsx              # Point d'entrée pour le développement
└── MANIFEST.in                       # Fichiers à inclure dans le package
```

### Modification du Composant

#### Frontend (React/TypeScript)

Le composant principal se trouve dans `streamlit_custom_component/frontend/src/CustomComponent.tsx`.

**Points clés :**
- Utilisez `withStreamlitConnection()` pour wrapper votre composant
- Accédez aux props via `args` (ex: `args.message`, `args.color`)
- Envoyez des données à Python avec `Streamlit.setComponentValue()`
- Ajustez la hauteur avec `Streamlit.setFrameHeight()`

#### Backend (Python)

L'API Python se trouve dans `streamlit_custom_component/__init__.py`.

**Points clés :**
- Déclarez le composant avec `components.declare_component()`
- En mode développement, utilisez `url="http://localhost:3001"`
- En production, utilisez `path=build_dir`

## 🧪 Tests

### Test Manuel

1. **Mode développement**
   ```bash
   # Terminal 1
   cd streamlit_custom_component/frontend
   npm run start
   
   # Terminal 2
   streamlit run example.py
   ```

2. **Mode production**
   ```bash
   # Build le frontend
   cd streamlit_custom_component/frontend
   npm run build
   
   # Tester le package
   pip install -e .
   streamlit run example.py
   ```

### Test du Composant

```bash
# Build le frontend
cd streamlit_custom_component/frontend
npm run build

# Tester le composant
streamlit run example.py
```

## 📦 Build

### Build Frontend

```bash
cd streamlit_custom_component/frontend
npm run build
```

Ceci crée les fichiers de production dans le dossier `build/`.

## 🔧 Configuration

### Personnalisation du Nom

1. **Renommer le package**
   - `streamlit_custom_component/` → `votre_nom_composant/`
   - Mettre à jour `setup.py` et `pyproject.toml`
   - Mettre à jour les imports dans `example.py`

2. **Mettre à jour les métadonnées**
   - Nom, version, description dans `setup.py`
   - Informations d'auteur
   - URL du repository

### Ajout de Dépendances

#### Frontend
```bash
cd streamlit_custom_component/frontend
npm install nom-du-package
```

#### Backend
Ajoutez dans `setup.py` ou `pyproject.toml` :
```python
install_requires=[
    "streamlit>=1.28.0",
    "votre-dependance>=1.0.0",
]
```

## 🐛 Dépannage

### Erreurs Communes

1. **Module not found**
   - Vérifiez que le package est installé : `pip install -e .`
   - Vérifiez les imports dans `__init__.py`

2. **Frontend ne se charge pas**
   - Vérifiez que le serveur de développement tourne sur le bon port
   - Vérifiez `_RELEASE = False` en mode développement

3. **Build échoue**
   - Vérifiez que Node.js et npm sont installés
   - Nettoyez les caches : `npm cache clean --force`

4. **Composant ne s'affiche pas**
   - Vérifiez la console du navigateur pour les erreurs JavaScript
   - Vérifiez les logs Streamlit

### Debug

1. **Mode debug frontend**
   ```bash
   cd streamlit_custom_component/frontend
   npm run start
   # Ouvrir http://localhost:3001 dans le navigateur
   ```

2. **Mode debug Streamlit**
   ```bash
   streamlit run example.py --logger.level=debug
   ```

## 📚 Ressources

- [Documentation Streamlit Components](https://docs.streamlit.io/library/advanced-features/streamlit-components)
- [Template officiel](https://github.com/streamlit/component-template)
- [streamlit-component-lib](https://github.com/streamlit/streamlit-component-lib)
- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)

## 🤝 Contribution

1. Fork le repository
2. Créer une branche feature : `git checkout -b feature/nouvelle-fonctionnalite`
3. Commit les changements : `git commit -am 'Ajouter nouvelle fonctionnalité'`
4. Push la branche : `git push origin feature/nouvelle-fonctionnalite`
5. Créer une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 