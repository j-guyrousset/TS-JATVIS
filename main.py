import os
import speech_recognition as sr
from random import choice
from utils import opening_text
from datetime import datetime
import pyttsx3
from decouple import config

import requests
from functions.online_ops import find_my_ip, find_wikipedia, play_yt, search_google, send_wtsapp_msg, send_email, get_news, get_joke, get_advice
from functions.os_ops import open_camera, open_cmd, open_notepad, open_calc, print_in_notepad
from pprint import pprint

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
        if ('exit' or 'stop') in query:
            hour = datetime.now().hour
            if hour < 6 or hour >= 21:
                #speak(query)
                speak('Good night my master')
            else:
                speak('thank you, have nice day sir.')
            exit()
        else:
            speak(choice(opening_text))
            #speak(query)
    except Exception:
        speak("I could not understand, please repeat.")
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        if 'open notepad' in query:
            open_notepad()
            speak('notepad is open')
        elif 'camera' in query:
            open_camera()
            speak('camera is now on: smile!')
        elif 'command prompt' in query:
            open_cmd()
            speak('command prompt is open')
        elif 'calculator' in query:
            open_calc()
            speak('claculator is open')
        elif 'ip address'in query:
            my_IP = find_my_ip()
            speak('I found your IP address')
            speak('May I print it?')
            ans = take_user_input()
            if 'yes' in ans:
                print_in_notepad('Your IP: {}'.format(my_IP))
                speak('say close to close and delete file')
                take_user_input()
                os.remove('log.txt')
            else:
                speak("I got it, we do not print it")
        elif 'wikipedia' in query:
            speak('What should I find on wikipedia?')
            search = take_user_input()
            result = find_wikipedia(search)
            speak('after wikipedia:')
            speak(result)
            speak('Should I print it ?')
            ans = take_user_input()
            if 'yes' in ans:
                speak('as you wish!')
                print_in_notepad(result)
            else:
                speak("I got it, we do not print it")
        elif 'youtube' in query:
            speak('Want would like to watch on youtube?')
            video = take_user_input().lower()
            play_yt(video)
        elif 'google' in query:
            speak('Tell me what you are looking for')
            gsearch = take_user_input()
            search_google(gsearch).lower()





