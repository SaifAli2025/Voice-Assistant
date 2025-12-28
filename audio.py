import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import sys

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            speak("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5)
            command = r.recognize_google(audio).lower()
            print("You said:", command)
            return command
    except sr.WaitTimeoutError:
        speak("Listening timed out.")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        speak("Could not request results from Google.")
    except Exception as e:
        speak(f"Microphone error: {e}")
    return ""

def run_assistant():
    speak("Hello Saif, how can I help you?")
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "exit" in command or "stop" in command:
            speak("Goodbye Saif!")
            sys.exit()
        elif command != "":
            speak("Sorry, I don't understand that command.")

run_assistant() 