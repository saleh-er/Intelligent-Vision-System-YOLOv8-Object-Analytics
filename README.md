#  Real-Time Object Detection & Counting (YOLOv8)

![Démo du projet](resultat.gif) 

##  Présentation
Ce projet implémente un système de vision par ordinateur capable de détecter, localiser et compter des objets en temps réel. En utilisant l'architecture **YOLOv8**, le système analyse chaque image pour identifier 80 classes d'objets différentes avec une haute précision et une latence minimale.

##  Fonctionnalités Clés
- **Inférence Temps Réel** : Optimisé pour fonctionner de manière fluide sur CPU.
- **Compteur Dynamique** : Un dictionnaire Python traite les résultats en direct pour afficher le nombre d'objets par catégorie sur l'écran.
- **Traitement de Flux** : Supporte la Webcam, les fichiers vidéo (`.mp4`, `.avi`) et les flux d'images.
- **Modularité** : Séparation de la logique de détection (`main.py`) et des outils de post-traitement (`src/utils.py`).

##  Stack Technique
- **Python 3.11**
- **Ultralytics (YOLOv8)** : Modèle de détection SOTA (State Of The Art).
- **OpenCV** : Manipulation des flux vidéo et rendu graphique des annotations.
- **MoviePy** : Pipeline de conversion vidéo pour la création de démonstrations (GIF).

##  Architecture du Projet
```text
object-detection-yolo/
├── src/
│   ├── utils.py        # Logique de comptage et dessin personnalisé
│   └── __init__.py
├── models/             # Stockage des poids du modèle (.pt)
├── data/
│   ├── input_videos/   # Vidéos sources pour analyse
│   └── output_results/ # Exportations des résultats annotés
└── main.py             # Point d'entrée du programme