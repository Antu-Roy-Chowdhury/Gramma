import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cmd():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'gramma' in command:
                command = command.replace('gramma', '')
                talk(command)
            else:
                talk('call me gramma,')
    except:
        pass
    return command

def run_granmma():
    while True:
        engine.say("Hi, genious. Call me 'gramma'.")
        engine.runAndWait()
        command = take_cmd()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info) 
        if 'stop' in command:
            break
        
run_granmma()
