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


