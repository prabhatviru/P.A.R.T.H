import pywhatkit as kit
import time,keyboard,pyautogui,webbrowser
from pytube import YouTube #* pip install pytube
from speak import speak
from TakeCommand import takeCommand
from website import Websites_Finder
from tkinter import Label , Entry , Button , Tk , StringVar
        
class Youtube_Utilities:
    def youtube_utilities(self,querry):
        match querry:
            case _ if'visit youtube' in querry or "go to youtube" in querry:self.open_youtube()     
            case _ if'play a video on youtube' in querry:self.play_video()    
            case _ if'activate youtube downloader' in querry:self.youtube()    
            case _ if'youtube search' in querry:self.youtube_search(querry)    
            case _ if'close youtube' in querry:self.close_youtube()
                
    def open_youtube(self):
        yt = Websites_Finder()
        yt.OpenClosesites("visit youtube")

    def play_video(self):
        speak('what should i play on youtube sir !')
        c = takeCommand().lower()
        speak('Ok Sir')
        kit.playonyt(c)
        time.sleep(10)
        keyboard.press_and_release('k')
        
    def youtube(self):
        def download_video():
            YouTube(url_var.get()).streams.filter(progressive=True,file_extension="mp4").order_by("resolution")[-1].download()
            status_label.config(text='Downloaded', font='verdana 14')
        root = Tk()
        root.geometry('500x200')
        root.title('YouTube Downloader')
        url_var = StringVar()
        Label(root, text='Please enter the URL').pack(pady=10)
        Entry(root, textvariable=url_var, width=60).pack(pady=5)
        Button(root, text='Download', command=download_video, bg='red', padx=5, pady=3).pack(pady=10)
        status_label = Label(root)
        status_label.pack()
        root.mainloop()

    def youtube_search(self,querry):
        querry = querry.replace('youtube search', '').strip(" ")  # Remove 'youtube search' from the query and strip spaces
        url = 'https://www.youtube.com/results?search_query=' + querry  # Generate YouTube search URL
        speak('This is what I have found from the search')
        webbrowser.open(url)
        kit.playonyt(url)  # Play the first result on YouTube

    def close_youtube(self):
        pyautogui.keyDown('ctrl')
        pyautogui.press('w')
        pyautogui.keyUp('ctrl')
        speak('closing youtube')

# try:
#     url = 'https://www.youtube.com'
#     webbrowser.open(url)
#     speak('opening youtube')
# except Exception as e:
#     print(e)
#     speak('Path not found')
