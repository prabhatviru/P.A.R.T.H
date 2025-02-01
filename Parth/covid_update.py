from TakeCommand import takeCommand
import requests # 

from speak import speak
from bs4 import BeautifulSoup # pip install bs4

# creating function for counting covid 19 cases ,deaths , recoveries -|>
def CoronaVirus():
    speak('Please tell me the country name for which you want to find the COVID cases')
    country = takeCommand().strip().replace(' ', '').lower()
    url = f'https://www.worldometers.info/coronavirus/country/{country}/'
    try:
        result = requests.get(url)
        result.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        speak(f'Failed to retrieve data: {e}')
        return
    soup = BeautifulSoup(result.text, 'lxml')
    data = [span.text.strip() for span in soup.select('div.maincounter-number span')]
    if len(data) >= 3:
        cases, deaths, recovered = data[:3]
        speak(f'Number of cases in {country} are {cases}')
        speak(f'Number of deaths in {country} are {deaths}')
        speak(f'Number of recoveries in {country} are {recovered}')
    else:speak('Could not retrieve complete data. Please try again later.')