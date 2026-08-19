# Ollama Chat (Python)

A minimal Python script that connects to a locally running Ollama server and lets you chat with a model from the terminal.

## Requirements

- [Ollama](https://ollama.com) installed and running locally
- Python 3.9+

## Setup

1. (Optional but recommended) create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Ollama is running (if the desktop app is not already running):
   ```bash
   ollama serve
   ```

## Usage

Run the script:
```bash
python chat.py
```

Type your message and press Enter. Type `exit` or `quit` to end the session.