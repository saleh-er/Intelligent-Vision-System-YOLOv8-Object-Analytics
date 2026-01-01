import cv2

def draw_counter(frame, results):
    # Récupérer les noms des classes détectées
    names = results[0].names
    counts = {}

    # Parcourir chaque boîte détectée
    for c in results[0].boxes.cls:
        class_name = names[int(c)]
        counts[class_name] = counts.get(class_name, 0) + 1

    # Afficher les compteurs sur l'image
    y_offset = 30
    for name, count in counts.items():
        text = f"{name}: {count}"
        cv2.putText(frame, text, (10, y_offset), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        y_offset += 30
    
    return frame