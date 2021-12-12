import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    ip_address = requests.get(r'https://api64.ipify.org?format=json').json()
    return ip_address['ip']

def find_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_yt(video):
    kit.playonyt(video)


def search_google(query):
    kit.search(query)



play_yt('funny animals')
