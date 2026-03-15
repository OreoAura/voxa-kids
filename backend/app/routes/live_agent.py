from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.gemini_service import stream_gemini_response

router = APIRouter()

@router.websocket("/live")
async def live_chat(websocket: WebSocket):

    await websocket.accept()
    print("Client connected")

    session_id = "default-session"

    try:
        while True:

            # Receive message from browser
            message = await websocket.receive_text()
            print("User:", message)

            # Skip empty messages
            if not message.strip():
                continue  # Go back to waiting for the next message

            # Stream response from Gemini
            async for chunk in stream_gemini_response(message, session_id):

                print("Gemini chunk:", chunk)

                # Send chunk to frontend
                await websocket.send_text(chunk)

    except WebSocketDisconnect:
        print("Client disconnected")