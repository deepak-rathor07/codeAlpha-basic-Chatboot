# InternshipBot

InternshipBot is a beginner-friendly, rule-based chatbot written in Python. It runs in the terminal, understands a small set of English and Hindi/Hinglish messages, and does not need any third-party packages.

## Requirements

- Python 3.8 or newer

## Run

Open a terminal in this folder and run:

```text
python main.py
```

Type `bye`, `goodbye`, `exit`, or `quit` to end the conversation.

## Try asking

- `Hello`
- `What is your name?`
- `How are you?`
- `Tell me about my internship`
- `Help`
- `Thanks`

The chatbot uses simple keyword and phrase rules in `chatbot.py`. Add more conditions to `get_response` to teach it new replies.

## Run tests

```text
python -m unittest -v
```
