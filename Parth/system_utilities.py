from speak import speak
import pyautogui,keyboard,os,time
from TakeCommand import takeCommand
from emptyRecycleBin import empty_recycle_bin

class System_Utilities:
    def Utilities(self,querry):
        querry = querry.lower().strip()
        match querry:
            case _ if 'volume up' in querry:
                querry = querry.replace('volume', '').replace('up', '').strip()
                try:
                    a = int(querry) if querry else 30  # Default to 30 if no number is provided
                    for _ in range(a):
                        pyautogui.hotkey('volumeup')
                    speak('Volume up is done')
                
                except ValueError:
                    speak('Invalid volume value provided')

            case _ if 'volume down' in querry:
                querry = querry.replace('volume', '').replace('down', '').strip()
                try:
                    a = int(querry) if querry else 30  # Default to 30 if no number is provided
                    for _ in range(a):
                        pyautogui.press('volumedown')
                    speak('Volume down is done')
                
                except ValueError:
                    speak('Invalid volume value provided')
                
            case 'mute':pyautogui.press('volumemute')

            case 'lock window':
                speak("locking the device")
                keyboard.press('win')
                keyboard.press('l')

            case 'shut down my system':
                speak('shutting down you laptop')
                os.system('shutdown /s /t 5')

            case 'restart my system':
                speak('restarting you laptop')
                os.system('shutdown /r /t 5')
            
            case 'empty the recycle bin':empty_recycle_bin()    
                
            case 'tab':
                speak('switching your window')
                pyautogui.keyDown('alt').press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
                
            case 'return to home':
                speak('returning to your home page')
                pyautogui.keyDown('win')
                pyautogui.press('d')
                time.sleep(1)
                pyautogui.keyUp('win')
                
            case 'go to search bar':
                time.sleep(1)
                keyboard.press_and_release("win+s")
                time.sleep(5)
                speak('sir,what should write on the search bar')
                ac  = takeCommand()
                keyboard.write(ac)
                keyboard.press('enter')