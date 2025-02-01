import speech_recognition as Sr # pip import speechrecognition 

def takeCommand(pause_threshold=0.5, phrase_time_limit=6, max_retries=3):
        r = Sr.Recognizer()
        retries = 0
        while retries < max_retries:    
            with Sr.Microphone() as source:
                print('Listening ...')
                r.adjust_for_ambient_noise(source,duration=1)
                r.pause_threshold = pause_threshold
                audio = r.listen(source, phrase_time_limit=phrase_time_limit)
            try:
                print('Recognizing...')
                querry = r.recognize_google(audio, language='en-in')
                print('User Said :-> ', querry,'\n')
            except Exception as e:
                print(e)
                print('Can you Say that again please ...')
                return 'None'
            querry=querry.lower()
            return querry
    
def takehindi():
    r = Sr.Recognizer()    
    with Sr.Microphone() as source:
        print('Listening ...')
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source, phrase_time_limit=4)
    try:
        print('Recognizing...')
        querry = r.recognize_google(audio, language='hi-in')
        print('User Said :-> ', querry,'\n')
    except Exception as e:
        print(e)
        print('Can you Say that again please ...')
        return 'None'
    querry=querry.lower()
    return querry   
#// takehindi()