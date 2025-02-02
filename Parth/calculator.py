import operator # pip install operator
from speak import speak
from TakeCommand import takeCommand
import speech_recognition as Sr
import math        
import datetime # pip install datetime

class Calcutation:
    def calculate(self,querry):
        match querry:
            case "activate calculator":self.activate_calculator()
            case 'give me the factorial of':self.factorial()    
            case "activate converter tool":self.convert_length()   
            case 'activate age calculator':self.age_calculator()

    def activate_calculator(self):
        try:
            speak('Do you want a standard or scientific calculator?')
            choice = takeCommand().lower()
            if 'standard' in choice:
                speak('Standard calculator activated. What to calculate? E.g., "2 plus 2"')
                with Sr.Microphone() as source:
                    r = Sr.Recognizer()
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    expr = r.recognize_google(audio)
                op1, oper, op2 = expr.split()
                result = {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divide': operator.truediv
                }[oper](float(op1), float(op2))
                speak(f'Result: {result}')
            elif 'scientific' in choice:
                speak('Factorial or logarithm?')
                adv = takeCommand().lower()
                if 'log' in adv:
                    base = 10 if 'base 10' in adv else 'e'
                    num = float(input(f'Enter number for log base {base}: '))
                    result = math.log10(num) if base == 10 else math.log(num)
                    speak(f'Log base {base}: {result}')
            elif 'leave it' in choice:speak('Okay.')
            
        except ValueError:speak('Invalid input. Please enter a number.')

        except Exception as e:speak(f'An error occurred: {e}')

        finally:speak('calculation complete.')
    # creating the function to find the factorial -|>
    def factorial():
        try:    
            speak('Enter the number to find the factorial:')
            number = int(input('Enter the number: '))
            result = 1
            if number < 0:
                speak('Error: Factorial of negative numbers is not defined.')
            else:
                for i in range(1, number + 1):
                    result *= i
                speak(f'The factorial of {number} is {result}.')

        except ValueError:speak('Invalid input. Please enter a number.')

        except Exception as e:speak(f'An error occurred: {e}')

        finally:speak('Factorial calculation is completed.')

    def convert_length():
        try:
            speak('Do you want to convert feet to meters or meters to feet? (feet to meters/meters to feet)')
            choice = takeCommand().lower()
            if 'feet to meters' in choice:
                feet = float(input("Enter the length in feet: "))
                meters = feet / 3.281
                speak(f'{feet} feet is equal to {meters:.2f} meters.')

            elif 'meters to feet' in choice:
                meters = float(input("Enter the length in meters: "))
                feet = meters * 3.281
                speak(f'{meters} meters is equal to {feet:.2f} feet.')

            elif 'inches to centimeters' in choice:
                inches = float(input("Enter the length in inches: "))
                centimeters = inches * 2.54
                speak(f'{inches} inches is equal to {centimeters:.2f} centimeters.')

            elif 'centimeters to inches' in choice:
                centimeters = float(input("Enter the length in centimeters: "))
                inches = centimeters / 2.54
                speak(f'{centimeters} centimeters is equal to {inches:.2f} inches.')

            elif 'kilometers to miles' in choice:
                kilometers = float(input("Enter the length in kilometers: "))
                miles = kilometers * 0.621371
                speak(f'{kilometers} kilometers is equal to {miles:.2f} miles.')

            elif 'miles to kilometers' in choice:
                miles = float(input("Enter the length in miles: "))
                kilometers = miles / 0.621371
                speak(f'{miles} miles is equal to {kilometers:.2f} kilometers.')

            elif 'yards to meters' in choice:
                yards = float(input("Enter the length in yards: "))
                meters = yards * 0.9144
                speak(f'{yards} yards is equal to {meters:.2f} meters.')

            elif 'meters to yards' in choice:
                meters = float(input("Enter the length in meters: "))
                yards = meters / 0.9144
                speak(f'{meters} meters is equal to {yards:.2f} yards.')

            elif 'nautical miles to kilometers' in choice:
                nautical_miles = float(input("Enter the length in nautical miles: "))
                kilometers = nautical_miles * 1.852
                speak(f'{nautical_miles} nautical miles is equal to {kilometers:.2f} kilometers.')

            elif 'kilometers to nautical miles' in choice:
                kilometers = float(input("Enter the length in kilometers: "))
                nautical_miles = kilometers / 1.852
                speak(f'{kilometers} kilometers is equal to {nautical_miles:.2f} nautical miles.')


            else:speak('Invalid choice. Please be more specific.')

        except ValueError:speak('Invalid input. Please enter a number.')

        except Exception as e:speak(f'An error occurred: {e}')

        finally:speak('Conversion complete.')

    # creatimg a function for age calculation -|>
    def age_calculator():
        today = datetime.date.today()
        speak('Please tell me your birthdate in YYYY-MM-DD format:')
        birthdate_str = input('Enter your birthdate: ')
        try:
            birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d').date()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            speak(f'You are {age} years old.')
        except ValueError:speak('Invalid date format. Please use YYYY-MM-DD.')
