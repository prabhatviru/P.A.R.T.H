'''
#// from covid_update import CoronaVirus
#* This is a normal virtual assistant.This can perfrom tasks like whatsapp automation, youtube automation, telling the Hardware information,weather report, mediafile and pdf reader, apps opening, handling screenschot, gitting the IP address and internet speed, Mapping automation and also it checks browsing and calculator function, and all the clocks function all this is done via voice commands.
#^ but there is a problem these function are already present in youtube but there is still one thing unique that is not done till date by any programmer, the one thing is in fromnt of my eyes but I am unable to see it
#todo currently this virtual assistant has no GUI as its front end as it is still in the development phase and it lags with data logging and threading. Here Theading is more important because currently this virtual assistant takes only one command at a time but to provide it to the general public we need to make it in a way where we can give another commands at a time when the previous command is still executing to do that we need to provide threading to it. As far as logging is concern we need loggong to get the track of the flow and to find where the error is raising.
'''
try:  
    ##! -|> modules to be imported that has pre installed or installed using pip command
    import os ,sys ,time ,socket ,pyjokes ,datetime#* pip install pyjokes datetime socket
    from googletrans import Translator #* pip install googletrans
    #? -|> User defined module
    from tkinter import * #* pre defined module commes with python when download
    from list_of_commands import * #& Has all the list of users inputs that can be given to the VA to get the desired outputs
    from speak import speak
    from jarvisGUI_1 import Ui_JarvisGUI
    from news import getNews
    from clock import Timmer
    from apiKey import api_key
    from browser import Browser
    from llama3 import Mistralai
    from greetings import Greeting
    from maps import Maps_utilizer
    from weather import Weather_Report
    from calculator import Calcutation
    from openCloseApp import Open_close
    from website import Websites_Finder
    from hide_unhide_file import hideUnhide
    from speed_test import check_internet_speed
    from TakeCommand import takeCommand,takehindi
    from system_utilities import System_Utilities
    from MoviePlayer_and_PdfReader import PdfReader
    from youtube_automation import Youtube_Utilities
    from hardware_information import HardwareChecker
    from whatsapp_automation import WhatsApp_Utilities
    from handleOpenScreenschot import Screenshot_Handler

    name = input("Enter your name :- ") #// My name in my AI progromme
        
    #? creating a translation tool(hindi to english) -|>
    def Translate():
        try:
            speak('what do you want me to translate Sir')
            line = takehindi()
            tranlate = Translator()
            result = tranlate.translate(line)
            Text = result.text(   )
            speak('the translation for this line is :->' + Text)
        except Exception as e:
            print(e)
            speak('Sorry sir,not able to translate the line')
    
    #? creating the translation tool(english to hindi) -|>
    def translate_text(text, src_lang='hi', dest_lang='en'):
        translator = Translator()
        return translator.translate(text, src=src_lang, dest=dest_lang).text
    
    #^ To start the execution in jarvis -|>
    def start():
        Greeting(name)
        while True:
            querry = takeCommand().lower()
            #! Getting the name of the virtual assistant
            if 'who are you' in querry:
                speak('sir my name is Parth')
                speak('I am your personal ai assistant')
            
            #? Talks with the assistant
            elif 'hello parth ji' in querry or 'hello' in querry or 'hey' in querry or 'hi assistant' in querry:speak('Hello sir.How may i help')
                
            elif 'how are you' in querry:speak('I am good sir ,what about you')
                
            elif 'what do you know about me' in querry:
                speak('All i know is you are my creater')
                speak(f'And your name is {name}')
                speak('that all i know about you')
                
            elif 'fine' in querry or 'I am good 'in querry:speak('It is great to hear sir')
                
            elif 'thank you' in querry or 'good job' in querry:
                import random as rd
                speak(rd.choice(["thank you sir",'it is my pleasure sir',"happy to help","Happy to be at your service"]))
                
            elif 'ok' in querry:
                speak('thank you sir')
                speak('What is the next command for me sir')
                
            elif 'what can you do for me' in querry:speak('I can do any thing as per your command')
                
            elif 'what are the things that you can not do' in querry:
                speak('I can not do ')
                speak('I cant click photos')
                speak('I cant make a normal call')
                speak('I cant send any message')
                speak('I cant write on notepad')
                speak('I can download youtube video but you will face error')
                speak('I cant tell the proper weather report (means humidty air pressure and etc...)')
            
            elif 'what is the day' in querry or 'tell me the date' in   querry:
                today  = datetime.date.today()
                speak(f"sir today's date is {today}")
            
            #* For searching in wikipeaia or finding something in wikipedia and to google search
            elif any(commands in querry for commands in browser_commands):
                brow = Browser()
                brow.browsing(querry)
                
            #^ For opening and closing apps
            elif 'open' in querry:
                querry = querry.replace("open","")
                Open_close.open_App(querry)
                
            elif 'close' in querry:
                querry = querry.replace("close"," ")
                Open_close.close_App(querry)
                
            #& Open document folder 
            elif 'go to document' in querry:
                speak('opening document folder')
                os.system('documents')
                speak('Sir please select a pdf file that you want to read')
                            
            elif 'close document' in querry:
                speak('closing the document folder')
                os.system('taskkill /f /im document')
                
            #~ Sending messages ,Making a call(audio or video), Show chats fron whatsapp
            elif any(command in querry for command in whatsapp_commands):
                what_uti = WhatsApp_Utilities()
                what_uti.whatsapp_utilities(querry)
                
            #! Related to youtube. It can perform multiple tasks like open youtube, play a show on youtube, download a video form youtube, or search anything on youtube 
            elif any(command in querry for command in youtube_commands):
                you_uti = Youtube_Utilities()
                you_uti.youtube_utilities(querry)
                
            #? Related to Maps like open Maps, get your location, get the distance etc..
            elif any(command in querry for command in maps_commands):
                mapping = Maps_utilizer()
                mapping.mapping(querry)
                
            #* Related to opening and closing websites like stackoverflow, filpkart, amazon, etc... 
            elif 'visit' in querry or 'from' in querry:
                shop = Websites_Finder()
                shop.OpenClosesites(querry) 
            
            #todo Related to getting the news report                 
            #// elif 'covid update' in querry or "give covid update" in querry:CoronaVirus()
            elif 'tell me the news' in querry:
                querry = querry.replace('tell me the news', ' ').replace('about',' ').strip()
                getNews(querry,api_key)
            
            #? -|> need to work on this section to make to more workable for translation between to language            
            elif 'activate translator' in querry:
                speak('Transtlator is been activated')
                speak('from which language to which language you want to activate the translator')
                tan = takeCommand().lower()
                if 'hindi to english' in tan:
                    speak('sir hindi to english translator is been activated')
                    speak('sir, what sholud I translate')
                    Translate()
                
                elif 'english to hindi' in tan:
                    speak('sir english to hindi translator is been activated')
                    speak('sir,what should I translate')#// trans_engtohin()
            
            #^ Related to getting the hardware information of the system of the system    
            elif any(commands in querry for commands in battery_commands):
                hard=HardwareChecker()
                hard.hardwarechecker(querry)
                
            #& Related to getting the time, setting the alarm for a given time, setting up the remnder and retriving it when needed    
            elif any(commands in querry for commands in time_commands):
                tim = Timmer()
                tim.Watch(querry)
                    
            #~ Related to getting internet speed and the ip address of the system   
            elif 'internet speed' in querry:check_internet_speed()
            
            elif 'ip address' in querry:
                import random as rd
                hostname = socket.gethostname()
                local_ip = socket.gethostbyname(hostname)
                speak(rd.choice([f"your ip address is {local_ip}",f"sir, IP address of your system is {local_ip}"]))    
            
            elif 'joke' in querry:
                j = pyjokes.get_joke()
                speak(j)
                
            elif any(commands in querry for commands in weather_commands):
                wet=Weather_Report()
                wet.weather(querry)
                
            elif 'hide file' in querry or 'make it visible' in querry:
                querry = querry.replace('file',' ').replace('make it',' ').strip()
                hideUnhide(querry)
            
            #! Related to handle screenshot and then open it
            elif 'screenshot' in querry or 'show screenshot' in querry:
                screenshot = Screenshot_Handler()
                screenshot.handler(querry)
                
            #? Related to play movies and webseries
            elif 'play movie' in querry or "play webseries" in querry or "play" in querry:
                filename = querry.replace('play'," ").strip()
                Movie = PdfReader()
                Movie.play_movie(filename)
            
            #* Related to reading pdf files present in the system
            elif 'read pdf' in querry or "read" in querry:
                querry.replace("read"," ").replace("pdf"," ")
                Pdf = PdfReader()
                Pdf.pdf_reader(querry)
            
            #^ Related to caluclator handles calculation like standard, sctentific, factorial,age calcutation and much more
            elif any(command in querry for command in utility_commands):
                calcu = Calcutation()
                calcu.calculate(querry)
            
            #& Related to system utilities like volume up, dowm, mute, lock window, shutdown, restart, empty recycle bin etc...   
            elif any(command in querry for command in system_commands):
                sys_uti = System_Utilities()
                sys_uti.Utilities(querry)
                    
            elif "don't listen" in querry or "stop listening" in querry:
                speak("for how much time you want to stop me from listening your commands")
                a = int(input('for how much time you want to stop me from listening your commands :->'))
                time.sleep(a)
                speak('what is the next command for me sir')

            #~ Sends Parth to sleep at the end it can be removed if needed
            elif 'go back to sleep' in querry or 'see you later' in querry:
                import random as rd
                speak(rd.choice(['If you have any work for me you can wake me up any time.',"If you need any help for something, always feel free to ask"]))
                speak(rd.choice(['have a good day sir',"have a nice day","good day "]))
                sys.exit()
            
            elif "generate code" in querry or "write a program" in querry or "tell me a story" in querry:
                mist = Mistralai()
                mist.Mistral(querry)
                
            else:speak(' ')
           
    #^ Hotword for Parth -|>
    if __name__ == '__main__':
        print('Initiating parth')
        gui = Ui_JarvisGUI()
        while True:
            permission = takeCommand()
            if any(cmd in permission for cmd in wake_commands):start()
            
            elif 'goodbye' in permission:
                speak('Okay, have a good day sir')
                sys.exit()
            
            else:speak("if you need help feel free to ask")
            
except Exception as e:print(e)
