import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    print(f'Parth :-> {audio}')
    engine.runAndWait()
