from PIL import Image
from pillow_heif import register_heif_opener
import os

# Registra el abridor HEIF para Pillow
register_heif_opener()

def convert_heic_to_png(heic_path, output_path=None):
    """
    Convierte un archivo HEIC a PNG, intentando preservar la profundidad de color.

    Args:
        heic_path (str): La ruta al archivo HEIC de entrada.
        output_path (str, optional): La ruta para el archivo PNG de salida.
                                     Si no se especifica, se usará el mismo
                                     nombre de archivo con extensión .png.
    """
    try:
        # Abrir la imagen HEIC
        img = Image.open(heic_path)

        # Si no se proporciona una ruta de salida, generar una
        if output_path is None:
            base_name = os.path.splitext(heic_path)[0]
            output_path = f"{base_name}.png"

        # Guardar como PNG. Pillow automáticamente manejará la profundidad de bits
        # que soporte el modo de la imagen. Si el HEIC original es 16-bit,
        # y Pillow puede leerlo como tal, el PNG resultante también lo será.
        img.save(output_path, format="PNG")

        print(f"'{heic_path}' convertido a '{output_path}' (formato PNG).")
        print(f"Modo de imagen original: {img.mode}")
        print(f"Modo de imagen guardada (PNG): {img.mode}") # El modo debería ser el mismo o compatible
    except FileNotFoundError:
        print(f"Error: El archivo '{heic_path}' no fue encontrado.")
    except Exception as e:
        print(f"Error al convertir '{heic_path}': {e}")

# Ejemplo de uso:
heic_file = "IMG_5744.HEIC" # Reemplaza con la ruta a tu archivo HEIC
output_png_file = "IMG_5744.png"

# Crea un archivo HEIC de prueba si no tienes uno
# En un iPhone, toma una foto y asegúrate de que el formato de la cámara esté en "Alta Eficiencia".
# Luego, transfiérela a tu computadora.
# Si no tienes un HEIC, puedes usar una herramienta online para convertir una imagen a HEIC para probar.

# Llama a la función de conversión
convert_heic_to_png(heic_file, output_png_file)
# O para procesar en el mismo directorio:
# convert_heic_to_png(heic_file)

# Para procesar múltiples archivos en un directorio:
def batch_convert_heic_to_png(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            convert_heic_to_png(heic_path)

# Ejemplo de uso para conversión por lotes:
# batch_convert_heic_to_png("ruta/a/tu/directorio/con/heic")