from google import genai
from dotenv import load_dotenv
from PIL import Image
import os

# ==========================
# Cargar configuración
# ==========================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "No se encontró GEMINI_API_KEY en el archivo .env"
    )

# ==========================
# Crear cliente Gemini
# ==========================

client = genai.Client(api_key=api_key)

# ==========================
# Cargar imagen
# ==========================

ruta_imagen = "imagen.jpg"

try:
    imagen = Image.open(ruta_imagen)
except FileNotFoundError:
    print(f"No se encontró la imagen: {ruta_imagen}")
    exit()

# ==========================
# Consultas a Gemini
# ==========================

consultas = [
    "Describe detalladamente todo lo que aparece en la imagen.",
    "Indica los principales objetos visibles en la imagen.",
    "Resume la imagen en una sola frase.",
    "¿Hay texto visible en la imagen? Si lo hay, extráelo exactamente.",
    "¿Para qué podría utilizarse la escena mostrada en la imagen?"
]

print("=" * 70)
print("ANÁLISIS MULTIMODAL CON GEMINI")
print("=" * 70)

for numero, consulta in enumerate(consultas, start=1):

    print(f"\nPREGUNTA {numero}")
    print("-" * 70)
    print(consulta)

    try:

        respuesta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                consulta,
                imagen
            ]
        )

        print("\nRESPUESTA:")
        print(respuesta.text)

    except Exception as error:
        print(f"\nError: {error}")

    print("\n" + "=" * 70)