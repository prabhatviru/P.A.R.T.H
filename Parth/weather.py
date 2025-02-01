import requests # pip install requests
from speak import speak
from bs4 import BeautifulSoup # pip install bs4
from list_of_commands import weather_commands

class Weather_Report:
    def weather(self,query):
        match query:
            case _ if any(report in query for report in weather_commands[:4]):self.temperture(query)
            case _ if any(report in query for report in weather_commands[4:]):
                query = query.replace("give the weather report"," ").replace("weather"," ").replace("give me report for"," ").strip(" ")
                self.weatRept(query)
            
    def weatRept(self,query):
        if not query:
            speak("I couldn't understand the location. Please try again.")
            return
        url = f'https://www.google.com/search?q=weather in {query}'
        r = requests.get(url)
        r.raise_for_status()
        data = BeautifulSoup(r.text, 'html.parser')
        temp = data.find('div', class_='BNeawe iBp4i AP7Wnd').text
        weather_condition = data.find('div', class_='BNeawe tAd8D AP7Wnd').text.split("\n")[1] 
        speak(f'The current temperature in {query} is {temp}.')
        speak(f'The weather is {weather_condition}.')
    
    def temperture(self,query):
        search = query.replace("tell me the temperature"," ").replace("tell me the temperture"," ").replace("temperature"," ").replace("what is the temperature at"," ").replace("at"," ").replace("in"," ").strip(" ")
        Search = f'temperature in {search}'
        url = f'https://www.google.com/search?q={Search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,'html.parser')
        temp = data.find('div',class_='BNeawe').text
        speak(f'current {Search} is {temp}')