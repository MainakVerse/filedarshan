from flask import Flask, request, jsonify
from google import genai
import os
import json

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/api/summarize", methods=["POST"])
def summarize():
    info = request.json.get("info", {})
    prompt = f"Summarize this file/folder information:\n{json.dumps(info, indent=2)}"
    try:
        resp = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return jsonify({"summary": resp.text})
    except Exception as e:
        return jsonify({"summary": f"AI summarization failed: {e}"})

@app.route("/", methods=["GET"])
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
