"""
Simple script to send a chat message to a local Ollama model and print the response, using the official `ollama` Python library.

Requires Ollama to be running locally (either the desktop app or `ollama serve`) and a model already pulled (e.g. `ollama pull llama3.2`).
"""

import ollama

MODEL = "llama3.2"  # must match the exact tag shown by `ollama list`


def chat(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]


if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ("exit", "quit"):
            break

        reply = chat(user_input)
        print(f"\nModel: {reply}")