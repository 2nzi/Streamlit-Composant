#!/usr/bin/env python3
"""
Script de build automatisé pour le composant Streamlit Image Carousel.
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path

def run_command(command, cwd=None, check=True):
    """Exécute une commande shell."""
    print(f"🔄 {command}")
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return False

def check_prerequisites():
    """Vérifie les prérequis pour le build."""
    print("🔍 Vérification des prérequis...")
    
    # Vérifier Node.js
    if not run_command("node --version", check=False):
        print("❌ Node.js n'est pas installé")
        return False
    
    # Vérifier npm
    if not run_command("npm --version", check=False):
        print("❌ npm n'est pas installé")
        return False
    
    # Vérifier Python
    if not run_command("python --version", check=False):
        print("❌ Python n'est pas installé")
        return False
    
    print("✅ Tous les prérequis sont satisfaits")
    return True

def build_frontend():
    """Build le frontend React."""
    print("📦 Build du frontend...")
    
    frontend_dir = Path("streamlit_image_carousel/frontend")
    if not frontend_dir.exists():
        print("❌ Dossier frontend non trouvé")
        return False
    
    # Installer les dépendances
    if not run_command("npm install", cwd=frontend_dir):
        print("❌ Erreur lors de l'installation des dépendances npm")
        return False
    
    # Build de production
    if not run_command("npm run build", cwd=frontend_dir):
        print("❌ Erreur lors du build du frontend")
        return False
    
    print("✅ Build du frontend terminé")
    return True

def update_release_mode():
    """Met à jour le mode release dans __init__.py."""
    print("🔧 Configuration du mode release...")
    
    init_file = Path("streamlit_image_carousel/__init__.py")
    if not init_file.exists():
        print("❌ Fichier __init__.py non trouvé")
        return False
    
    # Lire le contenu
    with open(init_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Changer en mode release
    content = content.replace("_RELEASE = False", "_RELEASE = True")
    
    # Écrire le contenu modifié
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Mode release activé")
    return True

def build_python_package():
    """Build le package Python."""
    print("🐍 Build du package Python...")
    
    # Nettoyer les builds précédents
    if Path("dist").exists():
        shutil.rmtree("dist")
    if Path("build").exists():
        shutil.rmtree("build")
    if Path("*.egg-info").exists():
        for egg_info in Path(".").glob("*.egg-info"):
            shutil.rmtree(egg_info)
    
    # Build du package
    if not run_command("python -m build"):
        print("❌ Erreur lors du build du package Python")
        return False
    
    print("✅ Build du package Python terminé")
    return True

def test_package():
    """Teste le package buildé."""
    print("🧪 Test du package...")
    
    # Installer le package en mode développement
    if not run_command("pip install -e ."):
        print("❌ Erreur lors de l'installation du package")
        return False
    
    # Test d'import
    try:
        import streamlit_image_carousel
        print("✅ Import du package réussi")
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False
    
    print("✅ Test du package réussi")
    return True

def restore_dev_mode():
    """Remet le mode développement."""
    print("🔧 Restauration du mode développement...")
    
    init_file = Path("streamlit_image_carousel/__init__.py")
    if not init_file.exists():
        print("❌ Fichier __init__.py non trouvé")
        return False
    
    # Lire le contenu
    with open(init_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Changer en mode développement
    content = content.replace("_RELEASE = True", "_RELEASE = False")
    
    # Écrire le contenu modifié
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Mode développement restauré")
    return True

def main():
    """Fonction principale."""
    print("🚀 Build du composant Streamlit Image Carousel")
    print("=" * 60)
    
    # Vérifications préliminaires
    if not check_prerequisites():
        sys.exit(1)
    
    # Build du frontend
    if not build_frontend():
        sys.exit(1)
    
    # Configuration du mode release
    if not update_release_mode():
        sys.exit(1)
    
    # Build du package Python
    if not build_python_package():
        restore_dev_mode()
        sys.exit(1)
    
    # Test du package
    if not test_package():
        restore_dev_mode()
        sys.exit(1)
    
    # Restauration du mode développement
    if not restore_dev_mode():
        print("⚠️ Impossible de restaurer le mode développement")
    
    print("\n" + "=" * 60)
    print("🎉 Build terminé avec succès !")
    print("\n📦 Fichiers générés :")
    print("   - dist/streamlit_image_carousel-*.tar.gz")
    print("   - dist/streamlit_image_carousel-*.whl")
    print("\n🚀 Pour publier sur PyPI :")
    print("   twine upload dist/*")
    print("\n📚 Pour installer localement :")
    print("   pip install dist/streamlit_image_carousel-*.whl")

if __name__ == "__main__":
    main() 