# In-memory session storage
sessions = {}

def get_history(session_id: str):
    return sessions.get(session_id, [])

def update_history(session_id: str, role: str, content: str):
    if session_id not in sessions:
        sessions[session_id] = []

    sessions[session_id].append({
        "role": role,
        "parts": [{"text": content}]
    })