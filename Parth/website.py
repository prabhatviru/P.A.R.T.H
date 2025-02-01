import webbrowser,pyautogui #^pip install webbrowser pyautogui
from speak import speak

Names = {
    "ecommerce": {
        "amazon": "https://www.amazon.in/s?k=",
        "flipkart": 'https://www.flipkart.com/search?q=',
        "meesho": "https://www.meesho.com/search?q=",
        "myntra": "https://www.myntra.com/shirts?rawQuery=",
    },
    "social_media": {
        "chat gpt": "https://chatgpt.com",
        "linkedin":"https://www.linkedin.com/feed/",
        "meta":"https://www.facebook.com/login/?next=",
        "instagram":"https://www.instagram.com/",
    },
    "games":{
        "miniclip":"https://www.miniclip.com/games",
        "poki":"https://poki.com/en/g/",
        "kizi":"https://kizi.com/",
        "bgames":"https://www.bgames.com/"     
    },
    "coding":{
        "stack overflow": "https://stackoverflow.com",
        "github": "https://github.com/",
        "javatpoint":"https://www.javatpoint.com/",
        "geeksforgeeks":"https://www.geeksforgeeks.org/python-programming-language-tutorial/"
    },
    "others": {
        "book my show": "https://in.bookmyshow.com/delhi-ncr/movies/",
        "make my trip": "https://www.makemytrip.com/",
        "sonyliv": "https://www.sonyliv.com/",
        "youtube":"https://www.youtube.com",
        "google":"https://www.google.com/"
    }
}
class Websites_Finder:
    def OpenClosesites(self,sitename):
        if 'visit' in sitename or "from" in sitename:
            # Extract the site name and optional query
            if "from" in sitename:
                site_name = sitename.split("from")[-1].split('find')[0].strip()
                query = sitename.split('find')[-1].strip() if 'find' in sitename else ""
                    
            site_name = sitename.split("visit")[-1].split('and find')[0].strip()
            query = sitename.split('and find')[-1].strip() if 'and find' in sitename else ""

            url = None
            for category in Names.values():
                if site_name in category:
                    url = category[site_name]
                    break

            if url:
                if not query:speak(f"Opening {site_name}")
                if query:
                    url += query
                    speak(f"opening {site_name} with query {query}")
                webbrowser.open_new(url)
            else:print("The specified site is not recognized. Please try again.")

        elif 'close' in sitename:
            # Extract the site name to close
            site_name = sitename.split('close')[-1].strip().lower()
            found = False
            for category in Names.values():
                if site_name in category:
                    pyautogui.hotkey('ctrl', 'w')
                    print(f"Closing {site_name}")
                    found = True
                    break
            if not found:print("Cannot close: site not recognized!")
        else:print("Invalid command! Please enter a valid site name or action.")