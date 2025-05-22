from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

def convert_heic_to_jpg(heic_path, output_path=None, quality=95):
    """
    Convierte un archivo HEIC a JPG.
    Advertencia: JPG no soporta profundidad de color de 16 bits.
    La información de 16 bits se reducirá a 8 bits.

    Args:
        heic_path (str): La ruta al archivo HEIC de entrada.
        output_path (str, optional): La ruta para el archivo JPG de salida.
                                     Si no se especifica, se usará el mismo
                                     nombre de archivo con extensión .jpg.
        quality (int, optional): La calidad de compresión JPG (0-100).
                                 100 es la mejor calidad, 0 es la peor.
                                 Default es 95.
    """
    try:
        img = Image.open(heic_path)

        if output_path is None:
            base_name = os.path.splitext(heic_path)[0]
            output_path = f"{base_name}.jpg"

        # Convertir a 'RGB' (o 'RGBA' si se quiere preservar la transparencia para JPG, aunque muchos visores no lo soportan bien)
        # Esto reduce cualquier profundidad de color > 8 bits a 8 bits.
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB") # O "RGBA" si la transparencia es importante

        img.save(output_path, format="JPEG", quality=quality)

        print(f"'{heic_path}' convertido a '{output_path}' (formato JPG con calidad {quality}).")
        print(f"Modo de imagen original: {img.mode}")
        print(f"Modo de imagen guardada (JPG): RGB (8 bits)")

    except FileNotFoundError:
        print(f"Error: El archivo '{heic_path}' no fue encontrado.")
    except Exception as e:
        print(f"Error al convertir '{heic_path}': {e}")

# Ejemplo de uso:
heic_file = "IMG_5744.HEIC" # Reemplaza
output_jpg_file = "IMG_5744.jpg"
convert_heic_to_jpg(heic_file, output_jpg_file, quality=100)