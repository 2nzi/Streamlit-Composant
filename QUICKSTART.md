# 🚀 Guide de Démarrage Rapide

Ce guide vous permet de démarrer rapidement avec votre composant Streamlit personnalisé.

## ⚡ Démarrage en 5 minutes

### 1. Prérequis

Assurez-vous d'avoir installé :
- **Python 3.8+**
- **Node.js 16+**
- **npm**

### 2. Installation automatique

```bash
# Démarrer automatiquement le mode développement
python start_dev.py
```

Le script `start_dev.py` va :
- ✅ Vérifier que Node.js et npm sont installés
- ✅ Configurer le mode développement
- ✅ Installer toutes les dépendances
- ✅ Vous proposer de démarrer les serveurs

### 3. Démarrage manuel

Si vous préférez faire les étapes manuellement :

```bash
# 1. Installer les dépendances Python
pip install -e .

# 2. Installer les dépendances frontend
cd streamlit_custom_component/frontend
npm install

# 3. Démarrer le serveur de développement frontend
npm run start

# 4. Dans un autre terminal, lancer Streamlit
streamlit run example.py
```

## 🎯 Utilisation

### Mode Développement

1. **Modifiez le composant React** dans `streamlit_custom_component/frontend/src/CustomComponent.tsx`
2. **Modifiez l'API Python** dans `streamlit_custom_component/__init__.py`
3. **Voir les changements en temps réel** dans votre navigateur

### Mode Production

```bash
# Build le frontend
cd streamlit_custom_component/frontend
npm run build
```

## 📝 Exemple d'utilisation

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

## 🔧 Personnalisation

### Changer le nom du composant

1. **Renommer le dossier** : `streamlit_custom_component/` → `votre_nom_composant/`
2. **Mettre à jour les fichiers** :
   - `setup.py` : changer le nom du package
   - `pyproject.toml` : mettre à jour les métadonnées
   - `example.py` : changer l'import

### Ajouter des paramètres

Dans `streamlit_custom_component/__init__.py` :
```python
def custom_component(message: str = "Hello", color: str = "blue", size: int = 12, key=None):
    # Votre logique ici
    pass
```

Dans `streamlit_custom_component/frontend/src/CustomComponent.tsx` :
```typescript
function CustomComponent({ args }: ComponentProps) {
    const { message, color, size } = args;
    // Utiliser les paramètres
}
```

## 🐛 Dépannage

### Erreurs communes

**"Module not found"**
```bash
pip install -e .
```

**"npm command not found"**
- Installez Node.js depuis https://nodejs.org/

**"Port 3001 already in use"**
```bash
# Trouver le processus
lsof -i :3001
# Tuer le processus
kill -9 <PID>
```

**"Composant ne s'affiche pas"**
- Vérifiez que `_RELEASE = False` dans `__init__.py` (mode développement)
- Vérifiez que le serveur frontend tourne sur http://localhost:3001

### Debug

**Mode debug frontend** :
```bash
cd streamlit_custom_component/frontend
npm run start
# Ouvrir http://localhost:3001 dans le navigateur
```

**Mode debug Streamlit** :
```bash
streamlit run example.py --logger.level=debug
```

## 📚 Prochaines étapes

1. **Lire la documentation complète** : `DEVELOPMENT.md`
2. **Personnaliser le composant** selon vos besoins
3. **Ajouter des tests** : créer un dossier `tests/`
4. **Développer vos fonctionnalités** spécifiques

## 🆘 Besoin d'aide ?

- 📖 **Documentation complète** : `DEVELOPMENT.md`
- 🐛 **Issues** : Créez une issue sur GitHub
- 💬 **Discussions** : Utilisez les discussions GitHub

---

**Bon développement ! 🎉** 