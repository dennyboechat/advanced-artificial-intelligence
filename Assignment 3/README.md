# ChatterBot Terminal Client

A terminal-based chatbot built with Django and ChatterBot. ChatterBot is a machine-learning based conversational dialog engine that generates responses based on collections of known conversations.

## Prerequisites

- Python 3.10+

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
```

4. Run Django migrations:

```bash
python manage.py migrate
```

## Usage

Start the chatbot in your terminal:

```bash
python manage.py chat
```

On first run, the bot will train itself on the ChatterBot English corpus. After training completes, you can start chatting:

```
==================================================
  ChatterBot Terminal Client
  Type your message and press Enter
  Type "quit" or "exit" to end the session
==================================================

user: Good morning! How are you doing?
bot: I am doing well, how about you?
user: You're welcome.
bot: Do you like hats?
user: quit
Goodbye!
```

Type `quit` or `exit` to end the session, or press `Ctrl+C`.