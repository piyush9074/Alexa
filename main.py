import os
import webbrowser
from datetime import date
from datetime import datetime
import win32api
import win32con
import win32gui
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
from wikipedia import wikipedia
import webbrowser


import scrapper
from weathersearch import getweather

MY_NAME="friday"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)
audio_file = os.path.dirname(os.path.abspath(__file__)) + '\my_notification.wav'


def talk(text):
    engine.say(text)
    engine.runAndWait()


def alexa(cmd):
    print(cmd)


def take_command():
    try:
        # print(str(audio_file))
        msg = ""
        with sr.Microphone(chunk_size=768) as source:
            print("Listening Main.....")
            voice = listener.listen(source, None, 8)
            msg = listener.recognize_google(voice)
            msg = msg.lower()
            if MY_NAME in msg:
                # playsound(audio_file)
                talk("Yes Sir")
                msg = msg.replace(MY_NAME, '')
            if "are you there" in msg:
                talk("Always at your service sir....")

    except:
        pass

    return msg


def run_friday(firstwake):
    if firstwake == 1:
        talk("Hello Sir..    how may I help you")

    command = take_command()
    command = command.lower()

    if 'play song' in command:
        command = command.replace('play song', '')
        talk("Playing" + command)
        pywhatkit.playonyt(command)
    elif 'pause' in command:
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif 'play' in command:
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif 'who is' in command:
        wikisearch(command)
    elif 'minimize' in command:
        talk("Minimizing Now")
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    elif 'search' in command:
        command=command.replace("search","")
        webbrowser.open(f"https://www.google.com/search?q={command}")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "what's the date" in command:
        datetoday = date.today().strftime("%B %d, %Y")
        print(datetoday)
        talk(datetoday)
    elif "what's the time" in command:
        time = datetime.today().strftime("%I:%M %p")
        print(time)
        talk(time)
    elif "open" in command:
        openApps(command)
    elif "who are you" in command:
        talk("Hey I am friday assistant of Mr. Stark")
    elif "how are you" in command:
        talk("I am doing great sir...")
    elif "what can you do" in command:
        print("Well, I can joke, tell the time and date and play a song for you")
        talk("Well, I can joke, tell the time and date and play a song for you")
    elif 'close the window' in command:
        talk("ok sir")
        pyautogui.hotkey('alt', 'f4')
    elif command == "go to sleep":
        talk("Byeee bye boss. ping me whenever u want")
        return None
    elif 'android news' in command:
        print("Fetching the headlines")
        headlines = scrapper.getheadlines()
        print(headlines)
        talk("Do you want me to read the headlines sir?")
        command = take_command()
        if "yes" in command:
            talk(headlines)
        if "no" in command:
            pass
    elif 'open task manager' in command:
        pyautogui.hotkey('ctrl', 'shift', 'esc')
    elif 'ohh yeahh' in command:
        talk("I am gald you are happy sir..")
    elif 'weather in' in command:
        command=command.replace('weather in', '')
        try:
            weather=getweather(command)
            print(f"Weather in {command} is {weather}")
            talk(f"feels like {weather}")
        except:
            talk('Sorry boss I am unable to fetch it...')
    else:
        print("Please say something")

    run_friday(0)


def openApps(cmd):
    if 'gmail' in cmd:
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    if 'facebook' in cmd:
        webbrowser.open('https://www.facebook.com/')
    if 'favourite songs' in cmd:
        webbrowser.open(
            'https://www.youtube.com/watch?v=QDYDRA5JPLE&list=PLYkfZlNx7d-SwVGNJktfutETLxbLbOP9m&ab_channel=LilNasXVEVO')
    return None

def wikisearch(command):
    command=command.replace('who is','')
    try:
        response=wikipedia.summary(command,1)
        print(response)
        talk('Found it boss....... according to wikipedia........'+response)
    except:
        talk("Sorry boss I didn't find anything about it...")
