---

# 🗣️ Voice Assistant 

### 🚀 Full-featured Voice Assistant with Enhanced Notes and Time

A cross-platform, Python-powered **AI voice assistant** that performs daily automation tasks — from opening apps and websites to controlling system volume, managing notes, playing YouTube songs, telling jokes, and much more.

---

## 🌟 Features

✅ **Voice-controlled automation** – execute commands hands-free
✅ **Open any website or local application**
✅ **Play/Pause/Volume control** (system & YouTube)
✅ **Scroll up/down/top/bottom** in browsers
✅ **Search the web or YouTube**
✅ **Take, open, and show notes** (continuous dictation supported)
✅ **Tell current time & date**
✅ **Tell jokes**
✅ **Exit on command**
✅ **Cross-platform compatible (Windows, macOS, Linux)**

---

## 🧠 Tech Stack

* **Python 3.11+**
* **SpeechRecognition** – for capturing voice input
* **pyttsx3** – for text-to-speech output
* **pyautogui**, **keyboard** – for system automation
* **pycaw** – for precise volume control (Windows only)
* **pyjokes** – for fun responses
* **pywhatkit** – for YouTube playback
* **webbrowser**, **os**, **datetime**, **subprocess** – for system operations

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ultimate-voice-assistant.git
cd ultimate-voice-assistant
```

### 2️⃣ Install dependencies

```bash
pip install speechrecognition pyttsx3 pyautogui keyboard pycaw pyjokes pywhatkit comtypes
```

> 💡 *Note:*
>
> * For macOS/Linux, `pycaw` isn’t required.
> * You may need to install `portaudio`:
>
>   ```bash
>   pip install pyaudio
>   ```
>
>   or use
>
>   ```bash
>   pip install pipwin
>   pipwin install pyaudio
>   ```

---

## ▶️ How to Run

```bash
python ultimate_voice_assistant_v4.py
```

The assistant will greet you and start listening.
Speak commands naturally (e.g., “Open YouTube”, “Tell me a joke”, “Take note”, “What’s the time?”).

---

## 📋 List of Supported Voice Commands

### 🖥️ **System & Apps**

| Command           | Action                    |
| ----------------- | ------------------------- |
| "Open Notepad"    | Opens Notepad             |
| "Open Chrome"     | Launches Google Chrome    |
| "Open Calculator" | Opens Calculator          |
| "Open Spotify"    | Opens Spotify web         |
| "Open LinkedIn"   | Opens LinkedIn in browser |

---

### 🌐 **Web Search & YouTube**

| Command                       | Action                    |
| ----------------------------- | ------------------------- |
| "Open YouTube"                | Opens YouTube             |
| "Play [song name] on YouTube" | Plays the song on YouTube |
| "Search [topic]"              | Performs a Google search  |

---

### 🎵 **Media & Volume**

| Command                      | Action                  |
| ---------------------------- | ----------------------- |
| "Play video" / "Pause video" | Toggles play/pause      |
| "Volume up"                  | Increases system volume |
| "Volume down"                | Decreases system volume |
| "Mute"                       | Toggles mute/unmute     |

---

### 📝 **Notes**

| Command      | Action                                                      |
| ------------ | ----------------------------------------------------------- |
| "Take note"  | Dictates and saves a single note                            |
| "Open notes" | Starts continuous note dictation (say “save notes” to stop) |
| "Show notes" | Displays saved notes                                        |

---

### ⏰ **General Information**

| Command            | Action              |
| ------------------ | ------------------- |
| "What’s the time?" | Tells current time  |
| "What’s the date?" | Tells today’s date  |
| "Tell me a joke"   | Tells a random joke |

---

### 🚪 **Exit**

| Command                           | Action               |
| --------------------------------- | -------------------- |
| "Exit", "Quit", "Stop", "Goodbye" | Closes the assistant |

---

## 🧾 Notes Storage

All your notes are saved automatically in a text file:

```
notes.txt
```

Each note entry includes a timestamp for better tracking.

---

## 💡 Tips

* Speak clearly and naturally for best recognition.
* Works best with a stable internet connection (for Google Speech API).
* Compatible with **Windows 10/11**, **macOS**, and **Linux**.

---
## Conclusion

The Voice Assistant successfully demonstrates the integration of speech technologies with automation. It simplifies human-computer interaction by enabling voice-based commands for daily tasks, showcasing the power of AI in productivity tools. Future improvements could include natural language understanding and integration with IoT devices.

---
