import pyttsx3
import datetime
import speech_recognition as sr
from arduino_interface import ser


def speak(audio):
    engine = pyttsx3.init() # initialize
    voices = engine.getProperty('voices') # get the properties of voices
    engine.setProperty('voice', voices[1].id) # set the property to one
    engine.say(audio)
    engine.runAndWait()

def takeCommandCMD():
    query = input("How may I help you? ")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to command.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio , language= "en-GH")
        print(query)
    except Exception as e:
        print(e)
        speak("I didn't get that can you repeat it please")
        return None
    return query


def led1on():
    ser.write(b'A')  # Turn LED1 ON
    speak("LED 1 turned on")

def led1off():
    ser.write(b'a')
    speak("LED 2 turned off")

def Logic():
    query = takeCommandMic().lower()
    if 'keep charging' in query:
        led1on()
    elif "that's fine" in query:
        led1off()

    elif 'cheap charger' in query:
        led1on()
    elif 'continue' in query:
        led1on()

