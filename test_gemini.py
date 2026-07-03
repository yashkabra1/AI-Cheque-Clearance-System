from dotenv import load_dotenv
import os

from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say only: Gemini Connected Successfully!"
)

print(response.text)