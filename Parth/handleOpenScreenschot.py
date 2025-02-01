from TakeCommand import takeCommand
import time,keyboard,pyautogui,os # pip install pysutogui keyboard
from speak import speak

class Screenshot_Handler:
    def handler(self,querry):
        match querry:
            case 'screenshot':self.handle_screenshot()   
            case 'show screenshot':self.open_screenshot()
    
    def get_file_name(self,prompt):
        speak(prompt)
        return takeCommand().lower()

    def handle_screenshot(self):
        speak('Take screenshot of whole screen or specific area?')
        choice = takeCommand().lower()
        if 'whole' in choice or 'full' in choice:
            name = self.get_file_name('File name for screenshot?')
            speak('Taking screenshot in 5 seconds.')
            time.sleep(5)
            pyautogui.screenshot(f'{name}.png')
            speak('Screenshot taken.')
        elif 'specific' in choice:
            keyboard.press_and_release('win + shift + s')
            speak('Select the area. Screenshot will be saved in 20 seconds.')
            time.sleep(20)
            name = self.get_file_name('File name for screenshot?')
            pyautogui.screenshot(f'{name}.png')
            speak('Screenshot taken.')

    def open_screenshot(self):
        name = self.get_file_name('Enter screenshot file name to open?')
        file_path = f'{name}.png'
        if os.path.exists(file_path):
            os.startfile(file_path)
            speak('Screenshot opened.')
        else:speak('Screenshot file not found.')