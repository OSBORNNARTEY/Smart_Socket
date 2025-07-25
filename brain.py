import pyttsx3
import datetime
import speech_recognition as sr
from arduino_interface import ser, read_sensor


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

def check_flood():
    sensor_data = read_sensor()
    if sensor_data and sensor_data >= 350:
        speak("Flood alert! Water level critical. Cutting power.")
        ser.write(b'a')  # Force power off
        return True
    return False


def Logic():
    # Check flood first
    if check_flood():
        return

    query = takeCommandMic()
    if not query:
        return

    query = query.lower()

    # Power ON commands
    if any(k in query for k in [
        'keep charging', 'connect charger', 'supply power',
        'charge my laptop', 'charge my phone', 'activate the power',
        'boot up', 'power on', 'power up', 'start charging'
    ]) or ('on' in query and ('power' in query or 'charge' in query)):
        led1on()
        speak("Power activated")

    # Power OFF commands
    elif any(k in query for k in [
        'stop charging', 'disconnect', 'stop supplying power',
        'power off', 'shut down','shut down', "that's fine", 'continue'
    ]) or ('off' in query and ('power' in query or 'charge' in query)):
        led1off()
        speak("Power deactivated")

