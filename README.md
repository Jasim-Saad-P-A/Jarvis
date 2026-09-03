# 🤖 Jarvis — Python Voice Assistant

A Python-based voice assistant that listens to spoken commands and performs
common desktop and web automation tasks.

Jarvis uses speech recognition to understand commands and provides spoken
responses using text-to-speech.

## ✨ Features

- 🎙️ Voice command recognition
- 🔊 Text-to-speech responses
- 🕐 Get the current time
- 🌐 Open websites using voice commands
- 💻 Launch desktop applications
- 🪟 Close, minimize and maximize windows
- 🔄 Switch between applications
- 📑 Switch between browser tabs
- ▶️ Play and pause media
- 😴 Put the computer to sleep
- 🔌 Initiate system shutdown
- 🔎 Search the web when an application cannot be found
- 🧠 Fuzzy application matching using `difflib`

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAutoGUI
- Webbrowser
- datetime
- difflib

## ⚙️ How It Works

```text
                 ┌─────────────────┐
                 │   Voice Input   │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Speech          │
                 │ Recognition     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Command         │
                 │ Processing      │
                 └────────┬────────┘
                          ↓
        ┌─────────────────┼──────────────────┐
        ↓                 ↓                  ↓
   Open Website      Open Application    System Control
        ↓                 ↓                  ↓
   Web Browser       Desktop App       PyAutoGUI / OS
                          │
                          ↓
                 ┌─────────────────┐
                 │ Voice Response  │
                 │   pyttsx3       │
                 └─────────────────┘
```
# The commands you can work on:
"Hey Siri"
"What is the time?"
"Open YouTube"
"Open Google"
"Open Chrome"
"Open VS Code"
"Close window"
"Close tab"
"Switch app"
"Switch tab"
"Maximize window"
"Minimise window"
"Play"
"Pause"
"Sleep"
"Terminate"
"Exit"                 
