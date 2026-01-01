from moviepy import VideoFileClip
import os

def convert_to_gif(input_path, output_path):
    print(f"🔄 Conversion de {input_path} en GIF...")
    
    # 1. Charger la vidéo
    clip = VideoFileClip(input_path)
    
    # 2. Découpage intelligent : On prend le minimum entre 10s et la durée réelle
    duration = clip.duration
    end_time = min(10, duration)
    print(f"🎬 Durée détectée : {duration:.2f}s. Découpage à : {end_time:.2f}s.")

    if hasattr(clip, 'subclipped'):
        clip = clip.subclipped(0, end_time)
    else:
        clip = clip.subclip(0, end_time)

    # 3. Redimensionner (plus petit = plus léger pour GitHub)
    if hasattr(clip, 'resized'):
        clip = clip.resized(width=480)
    else:
        clip = clip.resize(width=480)
    
    # 4. Écriture du GIF
    print("💾 Génération du GIF... (Patientez quelques secondes)")
    clip.write_gif(output_path, fps=10, logger=None)
    
    print(f"✅ Succès ! Ton fichier '{output_path}' est prêt à la racine.")

if __name__ == "__main__":
    input_file = 'data/output_results/resultat_analyse.avi'
    if os.path.exists(input_file):
        convert_to_gif(input_file, 'resultat.gif')
    else:
        print(f"❌ Erreur : Le fichier {input_file} n'existe pas.")