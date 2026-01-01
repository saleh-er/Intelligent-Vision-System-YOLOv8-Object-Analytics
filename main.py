from ultralytics import YOLO
import cv2
import os
from src.utils import draw_counter

def main():
    # 1. Configuration des dossiers et fichiers
    input_video_path = 'data/input_videos/video.mp4'
    output_folder = 'data/output_results'
    output_video_path = os.path.join(output_folder, 'resultat_analyse.avi')
    
    os.makedirs(output_folder, exist_ok=True)

    # 2. Charger le modèle YOLO (Nano pour la rapidité)
    model = YOLO('models/yolov8n.pt') 

    # 3. Charger la vidéo source
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print(f"❌ Erreur : Impossible d'ouvrir la vidéo à l'emplacement : {input_video_path}")
        return

    # 4. Récupérer les propriétés de la vidéo pour l'enregistrement
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps == 0: fps = 24 # Valeur par défaut si non détectée

    # 5. Configurer l'écriture du fichier de sortie
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    print(f"🎬 Analyse de la vidéo commencée...")
    print(f"💾 Le résultat sera sauvegardé dans : {output_video_path}")
    print("⌨️  Appuie sur 'q' pour arrêter l'analyse prématurément.")

    while cap.isOpened():
        success, frame = cap.read()
        
        if success:
            # Lancer l'inférence YOLO sur la frame actuelle
            results = model(frame, stream=True)
            
            for r in results:
                # Récupérer l'image avec les boîtes englobantes de base
                annotated_frame = r.plot()
                
                # Ajouter ton compteur d'objets personnalisé (depuis src/utils.py)
                annotated_frame = draw_counter(annotated_frame, [r])
                
                # Sauvegarder la frame dans le fichier de sortie
                out.write(annotated_frame)
                
                # Afficher le résultat en direct à l'écran
                cv2.imshow("YOLOv8 Analysis", annotated_frame)
            
            # Arrêter si l'utilisateur appuie sur 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Fin de la vidéo
            break

    # 6. Libérer toutes les ressources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"✅ Analyse terminée avec succès !")

if __name__ == "__main__":
    main()