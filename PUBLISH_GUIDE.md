# 🚀 Guide de Publication sur PyPI

Ce guide vous accompagne étape par étape pour publier votre composant Streamlit sur PyPI.

## 📋 Prérequis

### 1. Compte PyPI
- Créez un compte sur [PyPI](https://pypi.org/account/register/)
- Créez un compte sur [TestPyPI](https://test.pypi.org/account/register/)

### 2. Tokens d'authentification

#### TestPyPI Token
1. Connectez-vous sur [TestPyPI](https://test.pypi.org/)
2. Allez dans "Account settings" → "API tokens"
3. Créez un nouveau token avec le scope "Entire account"
4. Copiez le token (format: `pypi-...`)

#### PyPI Token
1. Connectez-vous sur [PyPI](https://pypi.org/)
2. Allez dans "Account settings" → "API tokens"
3. Créez un nouveau token avec le scope "Entire account"
4. Copiez le token (format: `pypi-...`)

### 3. Configuration des tokens

Éditez le fichier `.pypirc` et remplacez les placeholders :

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-VOTRE_VRAI_TOKEN_PYPI

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-VOTRE_VRAI_TOKEN_TESTPYPI
```

## 🔧 Préparation

### 1. Vérification du code
```bash
# Assurez-vous que tout fonctionne
python example.py
```

### 2. Mise à jour de la version
Éditez `pyproject.toml` et incrémentez la version :
```toml
version = "1.0.1"  # ou la version suivante
```

### 3. Commit des changements
```bash
git add .
git commit -m "Release v1.0.1"
git tag v1.0.1
git push origin main --tags
```

## 🚀 Publication

### Option 1: Script automatisé (Recommandé)
```bash
python build_and_publish.py
```

Le script va :
1. ✅ Builder le frontend React
2. ✅ Builder le package Python
3. ✅ Vérifier le package
4. ✅ Vous proposer de publier sur TestPyPI ou PyPI

### Option 2: Commandes manuelles

#### TestPyPI (Recommandé en premier)
```bash
# Build du frontend
cd streamlit_image_carousel/frontend
npm install
npm run build
cd ../..

# Build du package
python -m build

# Vérification
python -m twine check dist/*

# Publication sur TestPyPI
python -m twine upload --repository testpypi dist/*
```

#### PyPI (Après test réussi)
```bash
# Publication sur PyPI
python -m twine upload dist/*
```

## 🧪 Test de l'installation

### TestPyPI
```bash
# Créer un environnement virtuel de test
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# ou
test_env\Scripts\activate     # Windows

# Installation depuis TestPyPI
pip install --index-url https://test.pypi.org/simple/ streamlit-image-carousel

# Test
python -c "from streamlit_image_carousel import image_carousel; print('✅ Installation réussie!')"
```

### PyPI
```bash
# Installation depuis PyPI
pip install streamlit-image-carousel

# Test
python -c "from streamlit_image_carousel import image_carousel; print('✅ Installation réussie!')"
```

## 📝 Checklist finale

- [ ] ✅ Code testé et fonctionnel
- [ ] ✅ Version mise à jour dans `pyproject.toml`
- [ ] ✅ Tokens configurés dans `.pypirc`
- [ ] ✅ Frontend buildé
- [ ] ✅ Package buildé et vérifié
- [ ] ✅ Test sur TestPyPI réussi
- [ ] ✅ Publication sur PyPI
- [ ] ✅ Installation testée depuis PyPI

## 🎯 URLs utiles

- **PyPI**: https://pypi.org/project/streamlit-image-carousel/
- **TestPyPI**: https://test.pypi.org/project/streamlit-image-carousel/
- **Documentation**: Votre README.md

## 🆘 Dépannage

### Erreur de token
```
HTTPError: 403 Client Error: Invalid or non-existent authentication information
```
→ Vérifiez vos tokens dans `.pypirc`

### Erreur de build
```
ModuleNotFoundError: No module named 'streamlit_image_carousel'
```
→ Vérifiez que le frontend est bien buildé

### Erreur de version
```
File already exists
```
→ Incrémentez la version dans `pyproject.toml`

## 🎉 Félicitations !

Votre composant est maintenant disponible sur PyPI ! Les utilisateurs peuvent l'installer avec :
```bash
pip install streamlit-image-carousel
```

---

**💡 Conseil**: Commencez toujours par TestPyPI pour tester votre package avant de le publier sur PyPI principal. 