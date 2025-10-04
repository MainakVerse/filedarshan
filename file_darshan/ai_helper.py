import requests

# Replace this with your actual deployed backend URL
BACKEND_URL = "https://filedarshan-backend.onrender.com/api/summarize"

def ai_summary(info: dict) -> str:
    """
    Sends file/folder metadata to the backend and gets an AI summary.
    """
    try:
        response = requests.post(BACKEND_URL, json={"info": info}, timeout=10)
        response.raise_for_status()
        return response.json().get("summary", "No summary returned from backend.")
    except requests.exceptions.RequestException as e:
        return f"AI summarization failed: {e}"
