Voxa Kids – Gemini Live AI Agent

Overview

Voxa Kids is a real-time conversational AI assistant designed for children.
It demonstrates a live AI agent experience using WebSockets, FastAPI, and Google's Gemini model.

The project was created for the Gemini Live Agent Challenge and focuses on real-time interaction between users and an AI assistant.

---

Features

- Real-time chat interface
- WebSocket communication
- AI responses powered by Gemini
- FastAPI backend
- Lightweight HTML + JavaScript frontend
- Designed for Google Cloud deployment

---

Tech Stack

Frontend:

- HTML
- JavaScript

Backend:

- FastAPI
- WebSockets
- Python

AI:

- Google Gemini API

Cloud (planned deployment):

- Google Cloud Run
- Vertex AI

---

Project Architecture

User → Frontend (HTML + JS)
Frontend → WebSocket
WebSocket → FastAPI Backend
FastAPI → Gemini API
Gemini → AI Response → User

---

Running the Project Locally

Step 1

Clone the repository

git clone https://github.com/OreoAura/voxa-kids-live-agent.git
cd voxa-kids-live-agent

Step 2

Install dependencies

pip install -r requirements.txt

Step 3

Add Gemini API Key

Create a ".env" file:

VOXA_KIDS_GEMINI_API_KEY=YOUR_API_KEY

Step 4

Run backend server

python -m uvicorn app.main:app --host 127.0.0.1 --port 8001

Step 5

Run frontend server

python -m http.server 5500

Open browser:

http://127.0.0.1:5500/test.html

---

Demo

A demo video showing the live AI interaction is included in the hackathon submission.

---

Future Improvements

- Voice interaction
- Image understanding
- Full multimodal Gemini integration
- Deployment on Google Cloud Run

---

Author

Aurbagni Majumdar