"""
Simple script to send a chat message to a local Ollama model and print the response.

Requires Ollama to be running locally (ollama serve) and a model already pulled (e.g. `ollama pull llama3.2:3b`).
"""

import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "llama3.2"  # change to whichever model you have pulled


def chat(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]


if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ("exit", "quit"):
            break

        reply = chat(user_input)
        print(f"\nModel: {reply}")
