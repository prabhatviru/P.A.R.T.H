import psutil # ^ pip install psutil
from speak import speak
from list_of_commands import *

class HardwareChecker:
    def hardwarechecker(self,hardware):
        match hardware:
            case _ if any(battery in hardware for battery in battery_commands[:4]):self.check_battery()
            case _ if any(battery in hardware for battery in battery_commands[4:9]):self.getram()
            case _ if any(battery in hardware for battery in battery_commands[9:]):self.getcpuper()
    
    def check_battery(self):
        try:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            status_messages = {
                (76, 100): 'You have full battery on your laptop.',
                (51, 75): 'You have sufficient battery left, you can continue your work.',
                (26, 50): 'You have low battery but you can continue your work.',
                (0, 25): 'Your battery is in the critical stage, so plug in power right now.'
            }
            message = next((msg for (low, high), msg in status_messages.items() if low <= percentage <= high), '')
            speak(f'Sir, our system has {percentage} percent battery remaining.')
            speak(message)
            if percentage <= 25:
                if battery.power_plugged:
                    speak("You have connected the charger successfully.")
                else:
                    speak("Please connect the charger.")

        #// except ValueError as ve:
        #  //   print(f"ValueError occurred: {ve}")
        #    // speak('Sorry, I could not retrieve battery information.')

        except Exception as e:
            print(f"An error occurred: {e}")
            speak('Sorry, I encountered an error while checking the battery status.')

        finally:print("Battery check completed.")

    def getram(self):
        ram_say="System memory usage is "
        memory=psutil.virtual_memory()
        ram_say+=str(memory.percent)+" percent."
        if memory.percent>85:
            ram_say+=" System overload detected."
        else:
            ram_say+=" No overload detected"
        speak(ram_say)

    def getcpuper(percpu=False):
        if percpu:
            cpu_say="The usages of cpu cores are "
            for x in psutil.cpu_percent(interval=1,percpu=percpu):
                cpu_say+=str(x)+", "
            cpu_say+="percent respectively"
        else:
            cpu_say="CPU usage is "+str(psutil.cpu_percent(interval=1,percpu=percpu))+" percent"
        speak(cpu_say)
        