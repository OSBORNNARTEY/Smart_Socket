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
    elif 'keep charging' in query:
        speak("Okay, I will keep charging")

    elif "that's fine" in query:
        speak("Okay, I will keep charging")

    elif 'stop charging' in query:
        speak("Okay, I will stop charging")

    elif 'stop' in query:
        speak("Okay, I will stop charging")

    elif 'cheap charger' in query:
        speak("Okay, I will keep charging")

    elif 'continue' in query:
        speak("Okay, I will continue charging")

    elif 'stop supplying power' in query:
        speak("Okay, I will stop supplying power")

    elif 'disconnect' in query:
        speak("Okay, I will disconnect the charger")

    elif 'connect charger' in query:
        speak("Okay, conecting charger")

    elif 'supply power' in query:
        speak("Okay, I will supply power")

    elif 'supply park' in query:
        speak("Okay, I will supply power")

    elif 'supply bar' in query:
        speak("Okay, I will supply power")

    elif 'to play power' in query:
        speak("Okay, I will supply power")

    elif 'power on' in query:
        speak("Okay, I will turn on the power")

    elif 'power off' in query:
        speak("Okay, I will turn off the power")

    elif 'keep Char' in query:
        speak("Okay, I will keep charging")

    elif 'top supplies' in query:
        speak("Okay, I will stop supplying power")

    elif 'on' in query:
        speak("Okay, I will turn on the power")

    elif 'off' in query:
        speak("Okay, I will turn off the power")

    elif 'charge my laptop' in query:
        speak("Okay, I will charge your laptop")

    elif 'charge my phone' in query:
        speak("Okay, I will charge your phone")

    elif 'activate the power' in query:
        speak("Okay, activating power")

    elif 'boot up' in query:
        speak("Okay, turning on the power")

    elif 'power up' in query:
        speak("Okay, powering up the system")

    elif 'start up' in query:
        speak("Okay, starting up the system")

    elif 'power' in query:
        speak("Okay, I will supply power")

    elif 'start' in query:
        speak("Okay, I will start the system")

    elif 'shutdown' in query:
        speak("Okay, I will shutdown the system")
    elif 'stop' in query:
        speak("Okay, I will stop the system")
