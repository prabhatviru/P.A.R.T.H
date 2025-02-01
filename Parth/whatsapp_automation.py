try:
    import pyautogui,keyboard,time
    from TakeCommand import takeCommand
    from speak import speak
    from AppOpener import open

    def search_bar():
        open('whatsapp')
        time.sleep(3)
        location = pyautogui.locateCenterOnScreen("C:\\Users\\Prabhat\\Desktop\\Desktop\\python\\new_jarvis\\search.png", confidence=0.8)
        if location:
            pyautogui.click(location)

    def send_msg(name,message):
        search_bar()
        time.sleep(1)
        keyboard.write(name)
        time.sleep(1)
        pyautogui.click(x=146,y=216)
        time.sleep(1)
        text_box = pyautogui.locateCenterOnScreen("C:\\Users\\Prabhat\\Desktop\\Desktop\\python\\new_jarvis\\text_box.png")
        pyautogui.click(text_box)
        time.sleep(1)
        keyboard.write(message)
        keyboard.press('enter')
    
    def makecall_audio(name):
        search_bar()
        time.sleep(1)
        keyboard.write(name)
        time.sleep(1)
        pyautogui.click(x=146,y=216)
        time.sleep(1)
        phone = pyautogui.locateCenterOnScreen("C:\\Users\\Prabhat\\Desktop\\Desktop\\python\\new_jarvis\\audio_call.png")
        pyautogui.click(phone)
        time.sleep(1)
    #   //  pyautogui.click(x=1723,y=66)
    
    def makecall_video(name):
        search_bar()
        time.sleep(1)
        keyboard.write(name)
        time.sleep(1)
        pyautogui.click(x=146,y=216)
        time.sleep(1)
        video = pyautogui.locateCenterOnScreen("C:\\Users\\Prabhat\\Desktop\\Desktop\\python\\new_jarvis\\video_call.png")
        pyautogui.click(video)
        time.sleep(1)
    
    def chat(name):
        search_bar()
        time.sleep(1)
        keyboard.write(name)
        time.sleep(1)
        pyautogui.click(x=146,y=216)
        time.sleep(10)
    
except Exception as e:print(e)
    
class WhatsApp_Utilities:
    def whatsapp_utilities(self,querry):
        match querry:
            case _ if 'send message' in querry:
                recipient = querry.replace('send message to', '').strip()  # Extract recipient name
                speak(f'What is the message for {recipient}?')
                # msg = takeCommand()  # Assuming this function gets the message input
                test_msg = input()
                send_msg(recipient, test_msg)  # Assuming send_msg is the function to send a message
                
            case _ if 'make a voice call' in querry:
                speak('To whom do you want to make an audio call?')
                recipient = querry.replace('make a voice call to', '').strip()  # Extract recipient name
                makecall_audio(recipient)  # Assuming makecall_audio handles audio calls
                
            case _ if 'make a video call' in querry:
                speak('To whom do you want to make a video call?')
                recipient = querry.replace('make a video call to',' ').strip()  # Extract recipient name
                makecall_video(recipient)  # Assuming makecall_video handles video calls
                
            case _ if 'show chat' in querry or 'chat' in querry:
                speak('Whose chat do you want me to show?')
                contact = takeCommand()  # Assuming takeCommand captures the contact name
                chat(contact)  # Assuming chat() shows the requested contact's chat