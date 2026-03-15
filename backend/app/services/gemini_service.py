from google import genai
import os
from dotenv import load_dotenv
import asyncio  # needed for async streaming

load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("VOXA_KIDS_GEMINI_API_KEY"))

# In-memory session storage
sessions = {}

async def stream_gemini_response(message: str, session_id: str):
    try:
        # Initialize chat history for new session
        if session_id not in sessions:
            sessions[session_id] = [
                """You are Voxa, a friendly AI tutor for children aged 6–12.
Rules:
- Explain things simply
- Use fun examples
- Encourage curiosity
- Be supportive and positive
- Avoid harmful or adult topics"""
            ]

        chat_history = sessions[session_id]

        # Basic child-safe filter
        if not message.strip():
            return
        if any(word in message.lower() for word in ["badword1", "badword2"]):
            yield "Oops! Please ask something safe and friendly."
            return

        # Add user message as string
        chat_history.append(f"Child: {message}")

        # Stream response from Gemini
        stream = client.models.generate_content_stream(
            model="gemini-flash-latest",
            contents=chat_history  # list of strings only
        )

        full_response = ""

        for chunk in stream:
            text = getattr(chunk, "text", None)
            if text:
                full_response += text
                yield text  # send chunk to frontend
                await asyncio.sleep(0.05)  # typing effect

        # Save assistant reply
        chat_history.append(f"Voxa: {full_response}")

    except Exception as e:
        print("Gemini Error:", e)
        yield "Sorry, something went wrong while contacting Voxa."