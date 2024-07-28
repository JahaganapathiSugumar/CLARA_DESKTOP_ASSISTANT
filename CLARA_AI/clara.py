import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import sys
import webbrowser
import os

sys.stdout.reconfigure(encoding='utf-8')

engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! jaaha")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! jaaha")
    
    else:
        speak("Good Evening! jaaha")

    speak("I am claara your personal desktop assistent how can i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except sr.UnknownValueError:
            print("Say that again please...")
            return "None"
    return query

if __name__ == "__main__":
    wish()
    while(True):
        query = takecommand().lower()

        if('open my youtube' in query):
            webbrowser.open("youtube.com")

        elif('open google' in query):
            webbrowser.open("google.com")

        elif('open stack overflow ' in query):
            webbrowser.open("stackoverflow.com")

         
        elif 'play music' in query:
            music_dir = r'C:\Users\jahag\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))



        elif('wikipedia' in query):
            speak('Searching wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        
           
    




