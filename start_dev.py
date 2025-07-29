#!/usr/bin/env python3
"""
Script pour démarrer facilement le mode développement du composant Streamlit.
"""

import os
import subprocess
import sys
import time
from pathlib import Path

def run_command(command, cwd=None, background=False):
    """Exécute une commande shell."""
    print(f"🔄 {command}")
    
    if background:
        # Démarrer en arrière-plan
        if os.name == 'nt':  # Windows
            subprocess.Popen(command, shell=True, cwd=cwd)
        else:  # Unix/Linux/macOS
            subprocess.Popen(command, shell=True, cwd=cwd, start_new_session=True)
    else:
        # Exécuter en premier plan
        try:
            subprocess.run(command, shell=True, cwd=cwd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur: {e}")
            return False
    return True

def check_node_installed():
    """Vérifie que Node.js est installé."""
    try:
        result = subprocess.run("node --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js détecté: {result.stdout.strip()}")
            return True
        else:
            print("❌ Node.js n'est pas installé")
            return False
    except:
        print("❌ Impossible de vérifier Node.js")
        return False

def check_npm_installed():
    """Vérifie que npm est installé."""
    try:
        result = subprocess.run("npm --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ npm détecté: {result.stdout.strip()}")
            return True
        else:
            print("❌ npm n'est pas installé")
            return False
    except:
        print("❌ Impossible de vérifier npm")
        return False

def setup_development_mode():
    """Configure le mode développement."""
    init_file = Path("streamlit_custom_component/__init__.py")
    
    if not init_file.exists():
        print("❌ Fichier __init__.py non trouvé")
        return False
    
    # Lire le contenu actuel
    with open(init_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si déjà en mode développement
    if "_RELEASE = False" in content:
        print("✅ Déjà en mode développement")
        return True
    
    # Changer en mode développement
    content = content.replace("_RELEASE = True", "_RELEASE = False")
    
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Mode développement activé")
    return True

def install_dependencies():
    """Installe les dépendances."""
    frontend_dir = Path("streamlit_custom_component/frontend")
    
    if not frontend_dir.exists():
        print("❌ Dossier frontend non trouvé")
        return False
    
    print("📦 Installation des dépendances npm...")
    if not run_command("npm install", cwd=frontend_dir):
        return False
    
    print("📦 Installation des dépendances Python...")
    if not run_command("pip install -e ."):
        return False
    
    return True

def start_frontend_dev_server():
    """Démarre le serveur de développement frontend."""
    frontend_dir = Path("streamlit_custom_component/frontend")
    
    print("🚀 Démarrage du serveur de développement frontend...")
    print("📍 Le serveur sera accessible sur http://localhost:3001")
    
    return run_command("npm run start", cwd=frontend_dir, background=True)

def start_streamlit_app():
    """Démarre l'application Streamlit."""
    print("🚀 Démarrage de l'application Streamlit...")
    print("📍 L'application sera accessible sur http://localhost:8501")
    
    return run_command("streamlit run example.py")

def main():
    """Fonction principale."""
    print("🎯 Démarrage du mode développement du composant Streamlit")
    print("=" * 60)
    
    # Vérifications préliminaires
    if not check_node_installed():
        print("\n❌ Veuillez installer Node.js depuis https://nodejs.org/")
        sys.exit(1)
    
    if not check_npm_installed():
        print("\n❌ Veuillez installer npm")
        sys.exit(1)
    
    # Configuration
    if not setup_development_mode():
        print("\n❌ Impossible de configurer le mode développement")
        sys.exit(1)
    
    # Installation des dépendances
    if not install_dependencies():
        print("\n❌ Erreur lors de l'installation des dépendances")
        sys.exit(1)
    
    print("\n✅ Configuration terminée !")
    print("\n" + "=" * 60)
    print("🎮 Choisissez une option :")
    print("1. Démarrer le serveur frontend (pour le développement)")
    print("2. Démarrer l'application Streamlit")
    print("3. Démarrer les deux (recommandé)")
    print("4. Quitter")
    
    while True:
        choice = input("\nVotre choix (1-4) : ").strip()
        
        if choice == "1":
            start_frontend_dev_server()
            print("\n✅ Serveur frontend démarré !")
            print("📍 Accédez à http://localhost:3001 pour voir le composant")
            break
            
        elif choice == "2":
            start_streamlit_app()
            break
            
        elif choice == "3":
            print("\n🚀 Démarrage des deux serveurs...")
            start_frontend_dev_server()
            time.sleep(3)  # Attendre que le frontend démarre
            start_streamlit_app()
            break
            
        elif choice == "4":
            print("👋 Au revoir !")
            sys.exit(0)
            
        else:
            print("❌ Choix invalide. Veuillez choisir 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main() 