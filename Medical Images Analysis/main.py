import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Google API key is missing in .env file")


genai.configure(api_key=api_key)


image_path = "rash1.jpeg"  
img = Image.open(image_path)


model = genai.GenerativeModel("models/gemini-1.5-flash-8b")
chat = model.start_chat(history=[])

print("Medical Image & Report Analysis Chatbot (Type 'exit' to quit)\n")

# Chat loop
while True:
    query = input("You: ")

    if query.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break

    try:
        response = chat.send_message([query, img])
        print("\nBot: " + response.text + "\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")
