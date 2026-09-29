from google import genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

imagen = Image.open("image.jpg")

prompt = """
Analiza esta imagen.

Indica:
1. Qué aparece en la imagen.
2. Los objetos principales.
3. Un resumen de la escena.
"""

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=[
        prompt,
        imagen
    ]
)

print(response.text)