import os
import pyautogui
import time
import pyttsx3
import pygetwindow as gw
import speech_recognition
import pygame

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def GUI():
    pygame.mixer.init()
    audio = "Tools\sound.mp3"
    os.system('start msedge.exe --app="https://aarav-gui.netlify.app/"')
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    speak("Initializing....")
    time.sleep(3)
    pyautogui.hotkey('win', 'up')
    time.sleep(2)

    cmd_window = None
    while not cmd_window:
         cmd_window = gw.getWindowsWithTitle('Windows PowerShell')
    if not cmd_window:
        time.sleep(1)


    if cmd_window:
        cmd_window = cmd_window[0]  
        cmd_window.activate()  
        cmd_window.resizeTo(1400, 1600)  
        cmd_window.moveTo(1500, 100) 

