import speech_recognition as sr
from random import choice
from utils import opening_text
from datetime import datetime
import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

#set rate
engine.setProperty('rate', 200)

#set volume
engine.setProperty('volume', 1.0)

#set voice
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0]) #male voice
engine.setProperty('voice', voices[2].id) #1:female voice - 2:male voice - 0: default

#text to speech conversion function
def speak(text, pace=200):
    """says whatever string is passed as text, with the given pace"""

    engine.setProperty('rate', pace)
    engine.say(text)
    engine.runAndWait()


#greet function
def greet_user():
    """Greets the user according to moment of the day"""

    hour = datetime.now().hour
    text2 = "I am {}. How may I asist you?".format(BOTNAME)
    if hour < 6:
        speak('It is much to early, let me sleep', 100)
        speak('come back later {}'.format(USERNAME), 80)
    elif (hour >= 6 and hour < 12):
        speak('Good morning {} '.format(USERNAME))
    elif (hour >= 12 and hour < 19):
        speak('Good afternoon {}'.format(USERNAME))
    elif (hour >= 19 and hour < 22):
        speak('Good evening {}'.format(USERNAME))
    else:
        speak('Oh comme on, let me sleep!')
        speak('We will talk about it tomorrow {}'.format(USERNAME))

    if (hour >= 6 and hour < 22):
        speak(text2)

#taking user input using speech recofnition module (sr)
def take_user_input():
    """Takes the user input, recognizes it using speech recognition module
    and converts it to text (a string)"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-US')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
            speak(query)
        else:
            hour = datetime.now().hour
            if hour < 6 or hour >= 21:
                speak(query)
                speak('Good night my master')
            else:
                speak('thank you, have nice day sir.')
            exit()
    except Exception:
        speak("I could not understand, please repeat.")
        query = 'None'
    return query

take_user_input()

