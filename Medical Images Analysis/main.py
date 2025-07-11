import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Google API key is missing in .env file")

# Configure Gemini with your API key
genai.configure(api_key=api_key)

# Load the image
image_path = "rash1.jpeg"  # Ensure this file exists
img = Image.open(image_path)

# Initialize the Gemini model (faster & free-tier friendly)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Start a chat session with vision capability
chat = model.start_chat(history=[])

print("Medical Image & Report Analysis Chatbot (Type 'exit' to quit)\n")

# Chat loop
while True:
    query = input("You: ")

    if query.lower() in ["exit", "quit"]:
        print("🔚 Chat ended.")
        break

    try:
        response = chat.send_message([query, img])
        print("\nGemini: " + response.text + "\n")
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
