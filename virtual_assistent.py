#importing modules
from typing import Text
import pyttsx3                                                                          #pip install pyttsx3
import datetime                                                                         #pip install datetime
import googletrans                                                                      #pip install googletrans
import speech_recognition as sr                                                         #pip install SpeechRecognition
import wikipedia                                                                        #pip install wikipedia
import webbrowser
import random
import os
import smtplib
import time


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

speak("Before we get started, may I have your name please?")


#entering name
a = input("Enter you name : ")


#wish function
def wish():
    

    hour = int(datetime.datetime.now().hour)
    current_t = time.strftime('%I:%M %p')

    if hour>=0 and hour<12:
        t = ' Good Morning'
    elif hour>=12 and hour<17:
        t = ' Good Afternoon'
    else:
        t = ' Good Evening'

    speak(("hello") + (a) + (t))
    speak(f'it\'s {current_t}')
    #print("it's " + current_t)

    speak("I'm your virtual assistant, ready to help you with whatever you need. How may I assist you today?")


#to convert voice into text
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = r.listen(source)

    try:
        speak("Recoginsing...")
        query = r.recognize_google(audio,language='en-in')
        speak(f"{a} said: {query}\n")

    except Exception as e:
        ("Say that again please....")
        return "None"
    return query


#task performing functions
wish()
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
        speak(f"{a} ..., the time is {strTime}")

    elif "open browser" in query:
        speak(random.choice(["Opening Browser...","Launching Browser..."]))
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

    elif "open google" in query:
        webbrowser.open("www.google.com")

    elif '.com' in query or '.org' in query:
        query = query.replace('open','')
        query = query.replace(' ','')
        webbrowser.open(query)

    elif "shutdown" in query:
        speak("shutting down")
        os.system('shutdown -s')
    
    elif query == 'you can go now' or query == 'you can stop now':
        speak("ok, i am going now but if you need my help then start me, i will be there for you to help")
        break



