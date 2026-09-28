from google import genai
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

# Crear cliente Gemini
client = genai.Client(api_key=api_key)

# 5 textos en español + 5 en inglés
textos = [
    "Microsoft anunció una nueva oficina en Madrid.",
    "Estoy muy contento con los resultados obtenidos.",
    "Este producto es terrible y no lo recomiendo.",
    "Google presentó nuevas herramientas para desarrolladores.",
    "He aprobado todos los exámenes del curso.",

    "Amazon launched a new cloud service.",
    "I am very happy with the customer support.",
    "This product is awful and disappointing.",
    "OpenAI released a new AI model.",
    "The weather is pleasant today."
]

for numero, texto in enumerate(textos, start=1):

    prompt = f"""
    Analiza el siguiente texto.

    Texto:
    "{texto}"

    Indica:

    1. Sentimiento (Positivo, Negativo o Neutro)
    2. Entidades encontradas

    Formato:

    Sentimiento:
    ...

    Entidades:
    ...
    """

    respuesta = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )

    print("\n" + "=" * 60)
    print(f"TEXTO {numero}")
    print("=" * 60)
    print(texto)
    print()
    print(respuesta.text)