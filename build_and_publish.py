#!/usr/bin/env python3
"""
Script pour builder et publier le package sur PyPI
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path

def run_command(command, cwd=None):
    """Exécute une commande et affiche le résultat"""
    print(f"🔄 Exécution: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    
    if result.stdout:
        print("📤 Sortie:", result.stdout)
    if result.stderr:
        print("⚠️ Erreurs:", result.stderr)
    
    if result.returncode != 0:
        print(f"❌ Erreur lors de l'exécution: {command}")
        return False
    
    print(f"✅ Succès: {command}")
    return True

def build_frontend():
    """Build le frontend React"""
    print("🏗️ Building du frontend...")
    frontend_dir = Path("streamlit_image_carousel/frontend")
    
    if not frontend_dir.exists():
        print("❌ Dossier frontend non trouvé")
        return False
    
    # Installation des dépendances
    if not run_command("npm install", cwd=frontend_dir):
        return False
    
    # Build pour production
    if not run_command("npm run build", cwd=frontend_dir):
        return False
    
    print("✅ Frontend buildé avec succès")
    return True

def clean_build():
    """Nettoie les anciens builds"""
    print("🧹 Nettoyage des anciens builds...")
    
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"🗑️ Supprimé: {path}")
            elif path.is_file():
                path.unlink()
                print(f"🗑️ Supprimé: {path}")

def build_package():
    """Build le package Python"""
    print("📦 Building du package Python...")
    
    # Nettoyage
    clean_build()
    
    # Build du package
    if not run_command("python -m build"):
        return False
    
    print("✅ Package buildé avec succès")
    return True

def check_package():
    """Vérifie le package avant publication"""
    print("🔍 Vérification du package...")
    
    # Vérification avec twine
    if not run_command("python -m twine check dist/*"):
        return False
    
    print("✅ Package vérifié avec succès")
    return True

def publish_to_testpypi():
    """Publie sur TestPyPI"""
    print("🚀 Publication sur TestPyPI...")
    
    if not run_command("python -m twine upload --repository testpypi dist/*"):
        return False
    
    print("✅ Package publié sur TestPyPI")
    return True

def publish_to_pypi():
    """Publie sur PyPI"""
    print("🚀 Publication sur PyPI...")
    
    if not run_command("python -m twine upload dist/*"):
        return False
    
    print("✅ Package publié sur PyPI")
    return True

def main():
    """Fonction principale"""
    print("🎯 Début du processus de publication")
    print("=" * 50)
    
    # Vérification des outils requis
    required_tools = ["npm", "python", "pip"]
    for tool in required_tools:
        if not shutil.which(tool):
            print(f"❌ {tool} n'est pas installé")
            return
    
    # Installation des dépendances Python
    print("📦 Installation des dépendances Python...")
    if not run_command("pip install build twine"):
        return
    
    # Build du frontend
    if not build_frontend():
        return
    
    # Build du package
    if not build_package():
        return
    
    # Vérification du package
    if not check_package():
        return
    
    # Demande de confirmation pour la publication
    print("\n" + "=" * 50)
    print("📋 Package prêt pour publication!")
    print("=" * 50)
    
    choice = input("\nChoisissez une option:\n1. Publier sur TestPyPI (recommandé)\n2. Publier sur PyPI\n3. Quitter\nVotre choix (1-3): ")
    
    if choice == "1":
        publish_to_testpypi()
    elif choice == "2":
        confirm = input("⚠️ Êtes-vous sûr de vouloir publier sur PyPI? (oui/non): ")
        if confirm.lower() in ["oui", "yes", "y"]:
            publish_to_pypi()
        else:
            print("❌ Publication annulée")
    else:
        print("👋 Au revoir!")

if __name__ == "__main__":
    main() 