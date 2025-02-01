#####################################*#######################################*##############################*#####################*########################*###########################
#^ option 5
'''
#!the module which is used to compare the similarity between to words.
#?In this case we have used this module to find similar midia file and pdf files given by the user so as to get the media file or  pdf to get read by the system if the user dont have idea how it is pronounced or dont remember the name of the media file he is searching.

#^Here we have 2 classes MOviePlayer and PdfReader both class have 2 similar function a-> get_user_choice() b-> scand_directory() these 2 function are common in the in both classes.so, we are inheriting MoviePlayer into PdfReader class which not only increase the functionallity of both classes can can use MoviePlayer classes function by call the PdfReader as the constructor 
'''
from speak import speak
from apiKey import extension
import os,sys,re,PyPDF2,pyttsx3 # pip install PyPDF2 pyttsx3
from rapidfuzz import fuzz # pip install fuzzywuzzy
from browser import Browser
from config import load_or_create_config

engine = pyttsx3.init()

config = load_or_create_config()
movie_directory = config.get('movie_directory', "D:\\movies")
pdf_directory = config.get('pdf_directory', "D:\\documents")
class MoviePlayer:
    def get_user_choice(self,prompt, options):
        speak(prompt)
        for i, option in enumerate(options, 1):print(f"{i}. {option}")
        try:
            choice = int(input(f"Enter your choice (1-{len(options)}): ")) - 1
            if 0 <= choice < len(options):return options[choice]
        except ValueError:speak(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
        return None

    # Function to get the file number from the input string
    def extract_number(self,input_string):
        match = re.search(r'\d+', input_string)
        return int(match.group()) if match else None

    # Function to clean and normalize the user input
    def clean_input(self,user_input):
        normalized = user_input.lower().replace("ep", "episode").strip()
        return normalized

    # Function to scan directory and find media files with similarity
    def scan_directory(self,root_dir, base_file_name):
        media_files = []
        extensions = extension
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.lower().startswith(base_file_name.lower()) and filename.lower().endswith(extensions):media_files.append(os.path.join(dirpath, filename))
                else:
                    similarity = fuzz.partial_ratio(base_file_name.lower(), filename.lower())
                    if 75 <= similarity <= 100:media_files.append(os.path.join(dirpath, filename))
        return media_files

    # Function to play the selected media file
    def play_media(self,file_path):
        try:
            os.startfile(file_path)
            speak(f"Playing {os.path.basename(file_path)} for you")
        except Exception as e:speak(f"An error occurred while trying to play the file: {e}")

    # Main function to handle movie search and play
    def play_movie(self,user_input):
        root_dir = movie_directory # Specify the directory where media files are located'
        if not os.path.isdir(root_dir):
            speak(f"The directory {root_dir} does not exist or is not accessible.")
            sys.exit()
        
        cleaned_input = self.clean_input(user_input)
        media_files = self.scan_directory(root_dir, cleaned_input)
        if not media_files:
            speak("No media files found matching the base file name with enough similarity. finding on browser")
            brow = Browser()
            brow.google_search(user_input+ " full movie ")
            return

        # Extract the number from user input if available
        user_number = self.extract_number(user_input)
        if user_number:
            # Filter files based on the number
            matching_files = [file for file in media_files if str(user_number) in os.path.basename(file)]
            if matching_files:
                if len(matching_files) == 1:
                    self.play_media(matching_files[0])
                    return
                else:
                    # Handle multiple matches
                    best_match = max(matching_files, key=lambda file: fuzz.partial_ratio(cleaned_input, os.path.basename(file).lower()))
                    self.play_media(best_match)
                    return
        
        # If no specific number match is found, handle normally
        if len(media_files) == 1:self.play_media(media_files[0])
        
        else:
            # Look for the closest match based on similarity score
            best_match = max(media_files, key=lambda file: fuzz.partial_ratio(cleaned_input, os.path.basename(file).lower()))
            similarity = fuzz.partial_ratio(cleaned_input, os.path.basename(best_match).lower())
            
            # If the best match is similar enough, play it directly
            if similarity >= 80:self.play_media(best_match)
            else:
                # Show the list of similar matches to the user
                choices = [os.path.basename(file) for file in media_files]
                choice = self.get_user_choice("Select a file to play from similar matches:", choices)
                if choice:
                    file_to_play = media_files[choices.index(choice)]
                    self.play_media(file_to_play)
                else:speak("No valid choice made.")

class PdfReader(MoviePlayer):
    def open_pdf(self,file_path):
        try:
            os.startfile(file_path, 'open')
            speak(f"Opening {os.path.basename(file_path)} for you")
        except Exception as e:speak(f"An error occurred while trying to open the file: {e}")

    def open_document(self,base_file_name):
        root_dir = pdf_directory  # Specify the directory where PDF files are located
        if not os.path.isdir(root_dir):
            speak(f"The directory {root_dir} does not exist or is not accessible.")
            sys.exit()
        
        pdf_files = self.scan_directory(root_dir, base_file_name)
        if not pdf_files:
            speak("No PDF files found matching the base file name.")
            return

        if len(pdf_files) == 1:return pdf_files[0]
        else:
            choice = self.get_user_choice("Select a file to open:", pdf_files)
            if choice:self.open_pdf(choice)
            else:speak("No valid choice made.")
                
    def get_pdf_text(self,pdf_reader, start_page, end_page):
        full_text = ""
        for page_num in range(start_page, end_page + 1):
            page = pdf_reader.pages[page_num]
            text = page.extract_text().replace('\n', ' ')
            full_text += text + " "
        return full_text
        
    def pdf_reader(self,filename):
        file_path = self.open_document(filename)
        if not file_path:
            brow = Browser()
            brow.google_search(filename + "pdf")
            return
        with open(file_path, 'rb') as book:
            pdfReader = PyPDF2.PdfReader(book)
            num_pages = len(pdfReader.pages)
            speak(f'There are {num_pages} pages in this book.')
            speak('Please enter the starting page number:')
            start_page = int(input('Start page number: '))
            start_page = max(0, min(start_page, num_pages - 1))  # Clamp start page number within valid range
            speak('Please enter the ending page number:')
            end_page = int(input('End page number: '))
            end_page = max(start_page, min(end_page, num_pages - 1))  # Clamp end page number within valid range
            # Initialize playback controls
            while True:
                speak('Enter "start" to start reading, "pause" to pause, "resume" to resume, "stop" to stop reading.')
                command = input('Command: ').lower()
                if command == 'start':
                    full_text = self.get_pdf_text(pdfReader, start_page, end_page)
                    engine.say(full_text)
                    engine.runAndWait()
                
                elif command == 'pause':
                    engine.stop()
                    speak('Playback paused. Enter "resume" to continue or "stop" to stop.')
                
                elif command == 'resume':engine.runAndWait()
                    
                elif command == 'stop':
                    engine.stop()
                    speak('Playback stopped.')
                    break