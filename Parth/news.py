#creating function to find the news
from speak import speak
import requests #! pip install requests

def getNews(topic, api_key):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        news = [article["title"] for article in data["articles"][:5]]
        descrip = [article["description"] for article in data["articles"][:5]]
        for i, title in enumerate(news):
            speak(title)
            speak(descrip[i])
            print(" ")
    else:
        print("Error fetching news")
        speak("Error fetching news")