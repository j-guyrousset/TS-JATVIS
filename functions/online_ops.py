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


def send_wtsapp_msg(num, msg):
    kit.sendwhatmsg_instantly('+48{}'.format(num), msg)


EMAIL = config("EMAIL")
PWD = config("PWD")
def send_email(to_add, subject, msg):  #TODO: fix the connexion error( application specific identification)
    try:
        email = EmailMessage()
        email['To'] = to_add
        email['Subject'] = subject
        email['from'] = EMAIL
        email.set_content(msg)
        s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        s.ehlo()
        s.login(EMAIL, PWD)
        s.sendmail(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

"""sended = send_email('jguyrousset@gmail.com', 'test', 'This a test message from JARVIS')
if sended:
    print('mail sent!')
else:
    print('could not send email')"""

NEWS_API_KEY = config('NEWS_API_KEY')
def get_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


def get_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_advice():
    res = requests.get('https://api.adviceslip.com/advice').json()
    return res['slip']['advice']





