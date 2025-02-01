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
        conversions = {
            1: ("feet to meters", lambda x: x / 3.281),
            2: ("meters to feet", lambda x: x * 3.281),
            3: ("inches to centimeters", lambda x: x * 2.54),
            4: ("centimeters to inches", lambda x: x / 2.54),
            5: ("kilometers to miles", lambda x: x * 0.621371),
            6: ("miles to kilometers", lambda x: x / 0.621371),
            7: ("yards to meters", lambda x: x * 0.9144),
            8: ("meters to yards", lambda x: x / 0.9144),
            9: ("nautical miles to kilometers", lambda x: x * 1.852),
            10: ("kilometers to nautical miles", lambda x: x / 1.852),
            11: ("millimeters to inches", lambda x: x / 25.4),
            12: ("inches to millimeters", lambda x: x * 25.4),
            13: ("centimeters to feet", lambda x: x / 30.48),
            14: ("feet to centimeters", lambda x: x * 30.48),
            15: ("meters to miles", lambda x: x / 1609.34),
            16: ("miles to meters", lambda x: x * 1609.34),
            17: ("kilometers to yards", lambda x: x * 1093.61),
            18: ("yards to kilometers", lambda x: x / 1093.61),
            19: ("nanometers to meters", lambda x: x / 1e9),
            20: ("meters to nanometers", lambda x: x * 1e9),
            21: ("micrometers to meters", lambda x: x / 1e6),
            22: ("meters to micrometers", lambda x: x * 1e6),
            23: ("light-years to kilometers", lambda x: x * 9.461e12),
            24: ("kilometers to light-years", lambda x: x / 9.461e12),
            25: ("astronomical units to kilometers", lambda x: x * 1.496e8),
            26: ("kilometers to astronomical units", lambda x: x / 1.496e8),
        }
        
        # Display the conversion options with index numbers
        print('Choose a conversion type by entering the index number:')
        for index, (description, _) in conversions.items():
            print(f"{index}: {description}")

        # Take user's choice
        choice = int(input("Enter the index number of the conversion type: "))
        
        if choice in conversions:
            conversion_type, formula = conversions[choice]
            value = float(input(f"Enter the value to convert ({conversion_type}): "))
            result = formula(value)
            unit_from, unit_to = conversion_type.split(" to ")
            print(f'{value} {unit_from} is equal to {result:.2f} {unit_to}.')
        else:
            print("Invalid choice. Please enter a valid index number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
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