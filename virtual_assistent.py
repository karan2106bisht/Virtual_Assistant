#importing modules
from typing import Text
import pyttsx3                                                                          #pip install pyttsx3
import datetime                                                                         #pip install datetime
import googletrans                                                                      #pip install googletrans
import speech_recognition as sr                                                         #pip install speech_recgnition
import wikipedia                                                                        #pip install wikipedia
import webbrowser
import random
import os
import smtplib
import time
#import pyautogui                                                                       #pip install pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Initializing Virtual Assistent...")
speak("i am Virtual Assistent")
speak("who are you, please enter your name")


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

    speak(('hello ') + (a) + (t))
    speak(f'it\'s {current_t}')
    print("it's " + current_t)

    speak(" please tell me how can i help you")


#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("i am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recoginsing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Say that again please....")
        return "None"
    return query

#email function
def sendEmail(to, content):
    speak("Enter your  mail id")
    M = input('Enter your mail id : ')
    speak("Enter your password")
    P = input('Enter your password : ')
    speak("Enter reciever mail id again please ")
    R = input('Enter reciever mail id again : ')
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(M, P)
    server.sendmail(R, to, content)
    server.close()


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
        songs_dir = "C:\\songs"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{a} ..., the time is {strTime}")

    elif "email" in query or "mail" in query:
        try:
            speak("please type what should I send")
            content = input("")
            speak("enter mail id or receiver")
            print("Enter mail id of reveiver : ")
            to = input("")
            sendEmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
            print(e)

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
        print("shutting down")
        os.system('shutdown -s')


        

    elif "stop" in query or "you can go" in query or "sleep" in query:
        speak("okh... " + (a) + " i am going to sleep now")
        exit()