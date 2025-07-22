import pyttsx3
from brain import Logic


def speak(audio):
    engine = pyttsx3.init() # initialize
    voices = engine.getProperty('voices') # get the properties of voices
    engine.setProperty('voice', voices[1].id) # set the property to one
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak("Smarttii at your service, systems online")



if __name__ == "__main__":
    wishme()
    while True:
        Logic()


