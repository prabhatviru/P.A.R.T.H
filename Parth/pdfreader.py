# from speak import speak
# import PyPDF2,pyttsx3 # pip install PyPDF2 pyttsx3
# import os,sys

# engine = pyttsx3.init()

# class PdfReader():
#     def get_user_choice(self,prompt, options):
#         speak(prompt)
#         for i, option in enumerate(options, 1):
#             print(f"{i}. {option}")
#         try:
#             choice = int(input(f"Enter your choice (1-{len(options)}): ")) - 1
#             if 0 <= choice < len(options):
#                 return options[choice]
#         except ValueError:
#             speak(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
#         return None

#     def scan_directory(self,root_dir, base_file_name):
#         pdf_files = []
#         extension = ('.pdf',".docx")
#         for dirpath, _, filenames in os.walk(root_dir):
#             for filename in filenames:
#                 if filename.lower().startswith(base_file_name.lower()) and filename.lower().endswith(extension):
#                     pdf_files.append(os.path.join(dirpath, filename))
#         return pdf_files

#     def open_pdf(self,file_path):
#         try:
#             os.startfile(file_path, 'open')
#             speak(f"Opening {os.path.basename(file_path)} for you")
#         except Exception as e:
#             speak(f"An error occurred while trying to open the file: {e}")

#     def open_document(self,base_file_name):
#         root_dir = 'D:\\documents'  # Specify the directory where PDF files are located
#         if not os.path.isdir(root_dir):
#             speak(f"The directory {root_dir} does not exist or is not accessible.")
#             sys.exit()
        
#         pdf_files = self.scan_directory(root_dir, base_file_name)
        
#         if not pdf_files:
#             speak("No PDF files found matching the base file name.")
#             return

#         if len(pdf_files) == 1:
#             return pdf_files[0]
#         else:
#             choice = self.get_user_choice("Select a file to open:", pdf_files)
#             if choice:
#                 self.open_pdf(choice)
#             else:
#                 speak("No valid choice made.")
                
#     def get_pdf_text(self,pdf_reader, start_page, end_page):
#         full_text = ""
#         for page_num in range(start_page, end_page + 1):
#             page = pdf_reader.pages[page_num]
#             text = page.extract_text().replace('\n', ' ')
#             full_text += text + " "
#         return full_text
        
#     def pdf_reader(self,filename):
#         file_path = self.open_document(filename)
#         if not file_path:
#             return
#         with open(file_path, 'rb') as book:
#             pdfReader = PyPDF2.PdfReader(book)
#             num_pages = len(pdfReader.pages)
#             speak(f'There are {num_pages} pages in this book.')
#             speak('Please enter the starting page number:')
#             start_page = int(input('Start page number: '))
#             start_page = max(0, min(start_page, num_pages - 1))  # Clamp start page number within valid range
#             speak('Please enter the ending page number:')
#             end_page = int(input('End page number: '))
#             end_page = max(start_page, min(end_page, num_pages - 1))  # Clamp end page number within valid range
#             # Initialize playback controls
#             while True:
#                 speak('Enter "start" to start reading, "pause" to pause, "resume" to resume, "stop" to stop reading.')
#                 command = input('Command: ').lower()
#                 if command == 'start':
#                     full_text = self.get_pdf_text(pdfReader, start_page, end_page)
#                     engine.say(full_text)
#                     engine.runAndWait()
                
#                 elif command == 'pause':
#                     engine.stop()
#                     speak('Playback paused. Enter "resume" to continue or "stop" to stop.')
                
#                 elif command == 'resume':
#                     engine.runAndWait()
                    
#                 elif command == 'stop':
#                     engine.stop()
#                     speak('Playback stopped.')
#                     break
