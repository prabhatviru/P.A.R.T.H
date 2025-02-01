import wikipedia,time,pywhatkit as kit,pywikihow as py #^ pip install wikipedia,pywhatkit,pywikihow
from speak import speak
from TakeCommand import takeCommand 
from list_of_commands import browser_commands

#? Have all the search function (wikipedia, how to and what ,google search)
class Browser:
    def browsing(self,search): 
        match search:
            case _ if any(se in search for se in browser_commands[:2]):
                search = search.replace('wikipedia','').replace('tell me','').replace('something','').replace('about','')
                self.wikipedia(search)
            case _ if any(se in search for se in browser_commands[2:5]):self.activate_Browser()
            case _ if any(se in search for se in browser_commands[5:]):self.google_search(search)
        
    #! function for searching in wikipedia
    def wikipedia(self,searc):
        import random as rd
        speak(rd.choice(['searching WikiPedia ...',"going through wikipedia"]))
        result = wikipedia.summary(searc, sentences=51)
        speak(rd.choice(['wikipedia says ',"According to wikipedia"]))
        speak(result)
        
    #? function for searching in browser and opening the video related to it 
    def activate_Browser(self):
        import random as rd
        speak(rd.choice(['Browser is being activated','Okay sir, I would like to hear your question','I am ready to assist']))
        com = takeCommand()
        if 'how to' in com:
            query = com.replace("how to"," ").strip() 
            result = py.search_wikihow(query, 1)
            speak(result[0].summary if result else 'No results found.')
        else:
            search = wikipedia.summary(com, sentences=5)
            speak(f'According to your search: {search}')
            time.sleep(5)
            speak('Playing video related to your search.')
            kit.playonyt(search)
    
    #^ function for opening the search item in google chrome  
    def google_search(self,search_element):
        self.querry = search_element.replace('shivaji', '').replace('google search', '').replace("search","").strip()
        kit.search(self.querry)
        speak('This is what I have found from the search')