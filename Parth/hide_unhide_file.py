from speak import speak
import os

def hideUnhide(cond):
    if 'hide' in cond:
        os.system('attrib +h /s /d')
        speak('all file in this folder are now hidden from everyone')
        
    elif 'visible' in cond or 'unhide' in cond:
        os.system('attrib -h /s /d')
        speak('all file in this folder are now visible for everyone. sir, I think you took this decision in your own peace of mind')
        
    elif 'leave it' in cond or 'leave for now' in cond:speak('ok sir')