import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

#set rate
engine.setProperty('rate', 190)

#set volume
engine.setProperty('volume', 1.0)

#set voice
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0]) #male voice
engine.setProperty('voice', voices[1]) #female voice
