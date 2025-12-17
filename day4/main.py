from google import genai
from dotenv import load_dotenv

load_dotenv() 
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is mathematics important in Learning AI applications?",
)

print(response.text)