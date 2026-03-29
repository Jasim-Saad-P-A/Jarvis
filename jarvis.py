import pyttsx3
import speech_recognition as sr # SpeechRecognition
import datetime
import webbrowser
import pyautogui
import os
import time
import difflib

def find_and_open_app(app_name):
    paths = [
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
    ]

    for path in paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_lower = file.lower()

                matches = difflib.get_close_matches(app_name, [file_lower], n=1, cutoff=0.6)
                if matches:
                    full_path = os.path.join(root, file)
                    print("Found:", full_path)
                    os.startfile(full_path)
                    return True
    return False

engine = pyttsx3.init()

apps = {
"vs code": "code",
"notepad": "notepad",
"chrome": "chrome",
"calculator": "calc",
"whatsapp": "https://web.whatsapp.com"
}

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def shutdown_():
    pyautogui.hotkey('win', 'x') 
    time.sleep(1)

    pyautogui.press('u')         
    time.sleep(1)

    pyautogui.press('u') 
    
def sleep_():
    pyautogui.hotkey('win', 'x') 
    time.sleep(1)

    pyautogui.press('u')         
    time.sleep(1)

    pyautogui.press('s')           

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)   # 🔥 important
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return ""

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

speak("How are you doing!")         

def run_jarvis():
    command = take_command()

    if command == "":
        return   # 🔥 skip empty input

    elif "hey siri" in command:
        speak("Bolo sir!")
        
    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M')
        speak("The time is " + time)

    # elif "open" in command:
    #     app_name = command.replace("open", "").strip()

    #     if app_name in apps:
    #         speak(f"Opening {app_name}")
        
    #         if "http" in apps[app_name]:
    #             webbrowser.open(apps[app_name])
    #         else:
    #             os.system(f"start {apps[app_name]}")
    #     else:
    #         speak("Application not found")  
        
    # elif "open youtube" in command:
    #     speak("Opening YouTube")
    #     webbrowser.open("https://youtube.com")

    # elif "open insta" in command:
    #     speak("Opening Instagram")
    #     webbrowser.open("https://www.instagram.com/?next=https%3A%2F%2Fwww.instagram.com%2Freels%2FDV1Fk5spFcD%2F%3F__coig_login%3D1")     

    # elif "open google" in command:
    #     speak("Opening Google")
    #     webbrowser.open("https://google.com")

    # elif "open laundry" in command:
    #     speak("Opening your app")
    #     webbrowser.open("https://laundryv2.netlify.app/")

    # elif "play quran" in command:
    #     speak("Playing Quran")
    #     webbrowser.open("https://youtu.be/qcm168-WltA")

    # elif "open chat" in command:
    #     speak("Opening AI")
    #     webbrowser.open("https://chatgpt.com/c/69b20b2b-0e8c-8320-aeee-4b6252e360ca")
    elif "open" in command:
         app_name = command.replace("open", "").strip().lower()

         print("App name:", app_name)
         speak(f"Opening {app_name}")

    # 🔴 Normalize speech
         if "you tube" in app_name:
           app_name = "youtube"
         if "insta" in app_name:
           app_name = "instagram"

         apps = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "instagram": "https://instagram.com",
        "whatsapp": "https://web.whatsapp.com",
        "chrome": "chrome",
        "notepad": "notepad",
        "calculator": "calc",
        "vs code": "code"
         }

    # 🔴 Step 1: Dictionary match
         if app_name in apps:
           target = apps[app_name]

           if target.startswith("http"):
              webbrowser.open(target)
           else:
              os.system(f"start {target}")
           return

    # 🔴 Step 2: Try system command
         os.system(f"start {app_name}")

    # 🔴 Step 3: Try dynamic search (IMPORTANT)
         if find_and_open_app(app_name):
            return

    # 🔴 Step 4: Fallback to web
         speak("Not found, searching online")
         webbrowser.open(f"https://www.google.com/search?q={app_name}")
        
    elif "close window" in command:
        speak("Closing the window")
        pyautogui.hotkey('alt', 'f4')
        
    elif "close tab" in command:
        speak("Closing the tab")
        pyautogui.hotkey('ctrl','w')    
        
    elif "switch app" in command:
        speak("Switching the app")
        pyautogui.hotkey('alt','tab')  
        
    elif "switch tab" in command:
        pyautogui.hotkey('ctrl','tab')      
        
    elif "minimise window" in command:
        speak("Minimizing the window")
        pyautogui.hotkey('win', 'down')
        
    elif "maximize window" in command:
        speak("Maximizing the window")
        pyautogui.hotkey('win', 'up')    

    elif "terminate" in command:
        speak("Shutting down the system")
        # os.system("shutdown /s /t 5")
        shutdown_()
        
    elif "pause" in command:
        pyautogui.hotkey('space')    
        
    elif "play" in command:
        pyautogui.hotkey('space')     
        
    elif "sleep" in command:
        speak("Going to sleep")
        sleep_()

    elif "open vs code" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")       

    elif "exit" in command:
        speak("Goodbye Sir!")
        exit()
    
# Main loop
while True:
    run_jarvis()

   