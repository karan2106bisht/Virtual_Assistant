#importing modules
from typing import Text
import pyttsx3                                                                          #pip install pyttsx3
import datetime                                                                         #pip install datetime

import speech_recognition as sr                                                         #pip install SpeechRecognition
import wikipedia                                                                        #pip install wikipedia
import webbrowser
import random
import requests
import json
import os
import time
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 170)



#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Initializing Virtual Assistent...")

speak("Hello, I'm your virtual assistant. What should I call you?")


#to get user name
def get_name():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please tell me your name.")
        print("Please tell me your name.")
        speak("Listening...")
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        name = r.recognize_google(audio,language='en-in')


    except Exception as e:
        speak("Sorry, I didn't get your name. Could you please say it again?")
        print("Sorry, I didn't get your name. Could you please say it again?")
        return get_name()
    return name


#wish function
def wish(name):
    hour = int(datetime.datetime.now().hour)
    current_t = time.strftime('%I:%M %p')

    if hour>=0 and hour<12:
        t = ' Good Morning'
    elif hour>=12 and hour<17:
        t = ' Good Afternoon'
    else:
        t = ' Good Evening'

    speak(f"Hello {name}, {t}")
    speak(f'it\'s {current_t}')
    speak("I'm ready to help you with whatever you need. How may I assist you today?")


#to convert voice into text
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        speak(f"{name} said: {query}\n")

    except Exception as e:
        speak("Say that again please....")
        return "None"
    return query


def getWeather(city_name):
    api_key = "b72af671ed2dda3965c6fb38d7a52768" # Enter your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    weather_data = json.loads(response.text)
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        temperature = main_data['temp'] - 273.15
        feels_like = main_data['feels_like'] - 273.15
        humidity = main_data['humidity']
        speak(f"The temperature in {city_name} is {temperature:.1f} degrees Celsius, feels like {feels_like:.1f} degrees Celsius, with a humidity of {humidity} percent.")
    else:
        speak("Sorry, I could not find weather information for that city.")






#task performing functions
name = get_name()
wish(name)
while True:
    query = takecommand().lower()

    if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

    elif "wikipedia" in query:
        speak("searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia ")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    elif "open reddit" in query:
        webbrowser.open("reddit.com")

    elif "music" in query:
        songs_dir = "C:\\music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{name} ..., the time is {strTime}")

    elif "open browser" in query:
        speak(random.choice(["Opening Browser...","Launching Browser..."]))
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

    elif "open google" in query:
        webbrowser.open("www.google.com")

    elif '.com' in query or '.org' in query:
        query = query.replace('open','')
        query = query.replace(' ','')
        webbrowser.open(query)

    elif 'weather' in query:
        speak("Sure! Please tell me the city name.")
        city_name = takecommand()
        getWeather(city_name)

    elif "shutdown" in query:
        speak("shutting down")
        os.system('shutdown -s')
    
    elif query == 'you can go now' or query == 'you can stop now':
        speak("ok, i am going now but if you need my help then start me, i will be there for you to help")
        break


