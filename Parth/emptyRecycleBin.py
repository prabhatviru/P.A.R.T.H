from speak import speak
from TakeCommand import takeCommand
import winshell # pip install winshell

def empty_recycle_bin():
    speak('Do you want to empty the Recycle Bin? (yes/no)')
    response = takeCommand().lower()
    if 'yes' in response:
        speak('Emptying the Recycle Bin.')
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak('Recycle Bin emptied.')
    elif 'no' in response:speak('Recycle Bin not emptied.')
    else:speak('No valid response received. Leaving the Recycle Bin as is.')