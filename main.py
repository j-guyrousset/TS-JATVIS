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


