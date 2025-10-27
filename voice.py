"""
ultimate_voice_assistant_v4.py
==============================
Full-featured Voice Assistant with Enhanced Notes and Time
✅ Open any website or local app
✅ Play/Pause/Volume control (system & YouTube)
✅ Scroll up/down/top/bottom in browser
✅ Search web or YouTube
✅ Take, open, and show notes (continuous dictation)
✅ Tell current time & date
✅ Tell jokes
✅ Exit on command
✅ Cross-platform compatible
"""

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import time
import platform
import pyjokes
import pywhatkit
import subprocess

# Optional automation tools
try:
    import pyautogui
except:
    pyautogui = None

try:
    import keyboard
except:
    keyboard = None

# For volume control (Windows only)
IS_WINDOWS = platform.system().lower() == "windows"
if IS_WINDOWS:
    try:
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        PYCAW_AVAILABLE = True
    except:
        PYCAW_AVAILABLE = False
else:
    PYCAW_AVAILABLE = False

# -------------------- Voice Setup --------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# -------------------- Speech Recognizer --------------------
r = sr.Recognizer()
r.energy_threshold = 300
r.pause_threshold = 0.8

def listen(timeout=None, phrase_time_limit=None, retry=2):
    """Capture voice input and convert to text"""
    for attempt in range(retry):
        try:
            with sr.Microphone() as source:
                print("🎧 Listening...")
                audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("🔍 Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("🗣 You said:", query)
            return query.lower().strip()
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that. Please repeat.")
        except sr.RequestError:
            speak("Network error while recognizing speech.")
            return ""
        except Exception as e:
            print("Error while listening:", e)
            speak("An error occurred while listening.")
    return ""

# -------------------- Apps and Websites --------------------
APP_MAP = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
}

def open_application(name):
    name = name.lower().strip()
    try:
        if IS_WINDOWS:
            if name in APP_MAP:
                os.startfile(APP_MAP[name])
            else:
                os.startfile(name)
        elif platform.system().lower() == "darwin":  # macOS
            subprocess.Popen(["open", "-a", name])
        else:  # Linux
            subprocess.Popen([name])
        speak(f"Opening {name}")
    except Exception as e:
        speak(f"Couldn't open {name}. Error: {e}")

def open_website(query):
    """Open known or custom websites"""
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "instagram": "https://www.instagram.com",
        "github": "https://github.com",
        "stackoverflow": "https://stackoverflow.com",
        "spotify": "https://open.spotify.com",
        "chatgpt": "https://chat.openai.com",
        "facebook": "https://www.facebook.com",
        "linkedin": "https://www.linkedin.com",
    }
    for site, url in sites.items():
        if site in query:
            speak(f"Opening {site}")
            webbrowser.open(url)
            return
    speak("Which website should I open?")
    site = listen(timeout=5, phrase_time_limit=8)
    if site:
        url = f"https://{site.replace(' ', '')}.com"
        speak(f"Opening {site}")
        webbrowser.open(url)
    else:
        speak("I didn't hear any website name.")

# -------------------- Volume & Media --------------------
def change_master_volume(delta_percent):
    if not PYCAW_AVAILABLE:
        return False
    sessions = AudioUtilities.GetSpeakers()
    interface = sessions.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = volume.GetMasterVolumeLevelScalar()
    new = max(0.0, min(1.0, current + delta_percent / 100.0))
    volume.SetMasterVolumeLevelScalar(new, None)
    return True

def volume_up(amount=5):
    if PYCAW_AVAILABLE and change_master_volume(amount):
        speak("Volume increased.")
        return
    if pyautogui:
        pyautogui.press("volumeup", presses=5)
    speak("Volume increased.")

def volume_down(amount=5):
    if PYCAW_AVAILABLE and change_master_volume(-amount):
        speak("Volume decreased.")
        return
    if pyautogui:
        pyautogui.press("volumedown", presses=5)
    speak("Volume decreased.")

def mute_toggle():
    if pyautogui:
        pyautogui.press("volumemute")
    speak("Mute toggled.")

def media_play_pause():
    if keyboard:
        keyboard.send("space")
    elif pyautogui:
        pyautogui.press("space")
    speak("Toggled play/pause.")

# -------------------- Scroll --------------------
def control_scroll(command):
    if not pyautogui:
        speak("Scroll not supported on this system.")
        return
    if "down" in command:
        pyautogui.scroll(-1500)
        speak("Scrolling down.")
    elif "up" in command:
        pyautogui.scroll(1500)
        speak("Scrolling up.")
    elif "bottom" in command:
        pyautogui.hotkey("ctrl", "end")
        speak("Scrolled to bottom.")
    elif "top" in command:
        pyautogui.hotkey("ctrl", "home")
        speak("Scrolled to top.")

# -------------------- Notes --------------------
NOTES_FILE = "notes.txt"

def take_note():
    speak("What should I write in the note?")
    note_text = listen(timeout=10, phrase_time_limit=15, retry=2)
    if note_text:
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {note_text}\n")
        speak("Note saved.")
    else:
        speak("No note saved, I didn't catch that.")

def open_notes():
    """Opens or creates notes.txt and continuously listens for notes until user says 'save notes' or 'close notes'."""
    if not os.path.exists(NOTES_FILE):
        open(NOTES_FILE, "w", encoding="utf-8").close()
        speak("I created a new notes file for you.")
    else:
        speak("Opening your notes. You can start dictating. Say 'save notes' or 'close notes' when done.")

    collected_notes = []
    while True:
        speak("I'm listening for your notes.")
        note_text = listen(timeout=8, phrase_time_limit=10, retry=2)
        if not note_text:
            continue
        if any(word in note_text for word in ["save notes", "close notes", "stop notes"]):
            speak("Saving and closing your notes.")
            with open(NOTES_FILE, "a", encoding="utf-8") as f:
                if collected_notes:
                    f.write("\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                    f.write("\n".join(collected_notes) + "\n")
            speak("Your notes have been saved.")
            break
        else:
            collected_notes.append(note_text)
            speak("Added to notes.")

def show_notes():
    if not os.path.exists(NOTES_FILE):
        speak("You don’t have any notes yet.")
        return
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if content:
        speak("Here are your notes:")
        print("🗒️ Notes:\n", content)
    else:
        speak("Your notes file is empty.")

# -------------------- YouTube Playback --------------------
def play_youtube_song(query):
    song = query.replace("play", "").replace("on youtube", "").replace("song", "").strip()
    if song:
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
        time.sleep(6)
        if pyautogui:
            pyautogui.press("space")
    else:
        speak("Please say the song name you want to play.")

# -------------------- Command Handler --------------------
def perform_task(query):
    if not query:
        return

    # Open app/website
    if "open app" in query or "open application" in query:
        appname = query.split("app")[-1].strip()
        open_application(appname)
        return
    if "open" in query and "app" not in query and "notes" not in query:
        open_website(query)
        return

    # Notes
    if "open notes" in query:
        open_notes()
        return
    if "take note" in query:
        take_note()
        return
    if "show note" in query or "read note" in query:
        show_notes()
        return

    # YouTube
    if "play" in query and "youtube" in query:
        play_youtube_song(query)
        return

    # Media controls
    if any(x in query for x in ["pause", "resume", "play video"]):
        media_play_pause()
        return
    if "volume up" in query or "increase volume" in query:
        volume_up()
        return
    if "volume down" in query or "decrease volume" in query:
        volume_down()
        return
    if "mute" in query:
        mute_toggle()
        return

    # Scroll
    if "scroll" in query:
        control_scroll(query)
        return

    # General info
    if "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
        return
    if "date" in query:
        speak(f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}")
        return
    if "joke" in query:
        speak(pyjokes.get_joke())
        return
    if "search" in query:
        term = query.replace("search", "").strip()
        speak(f"Searching for {term}")
        webbrowser.open(f"https://www.google.com/search?q={term}")
        return

    # Exit
    if any(word in query for word in ["exit", "quit", "stop", "goodbye"]):
        speak("Goodbye! See you soon.")
        raise SystemExit

    speak("Sorry, I didn’t understand that command.")

# -------------------- Main Loop --------------------
def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        try:
            query = listen(timeout=6, phrase_time_limit=10, retry=2)
            if query:
                perform_task(query)
        except SystemExit:
            break
        except KeyboardInterrupt:
            speak("Assistant stopped manually. Goodbye.")
            break
        except Exception as e:
            print("Error in main loop:", e)
            speak("Something went wrong. Let's try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
