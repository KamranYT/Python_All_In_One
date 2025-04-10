import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the Gemini API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure the Google Generative AI SDK with your API key
genai.configure(api_key=gemini_api_key)

# Initialize the Gemini model (⚠️ double-check that 'gemini-2.0-flash' exists)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Event handler for when a chat session starts
@cl.on_chat_start
async def handle_chat_start():
    # Send a welcome message to the user
    await cl.Message(content="Hello! how can I help you today?").send()

# Event handler for incoming messages from the user
@cl.on_message
async def handle_message(message: cl.Message):
    # Extract the prompt from the incoming message
    prompt = message.content

    # Use the Gemini model to generate a response based on the prompt
    response = model.generate_content(prompt)

    # Extract the response text safely
    response_text = response.text if hasattr(response, "text") else ""

    # Send the AI-generated response back to the user
    await cl.Message(content=response_text).send()
