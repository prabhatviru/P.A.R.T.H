# config.py

import os
import json
from speak import speak

config_file_path = 'config.json'

def load_or_create_config():
    """
    # //This function loads the configuration from the config file.
    #//If the file doesn't exist, it prompts the user for input, saves it to the config file,
    #//and returns the directory paths for movies and PDFs.
    """
    if os.path.exists(config_file_path):
        # Load existing configuration
        with open(config_file_path, 'r') as config_file:
            return json.load(config_file)
    else:
        # Prompt the user for directory paths if config file doesn't exist
        speak("Configuration file not found. Let's set up the directories.")
        movie_dir = input("Enter the default directory for movies: ")
        pdf_dir = input("Enter the default directory for PDFs: ")
        
        # Save the user input to the configuration file
        config = {
            'movie_directory': movie_dir,
            'pdf_directory': pdf_dir 
        }
        
        with open(config_file_path, 'w') as config_file:
            json.dump(config, config_file)
        
        speak("Configuration saved successfully.")
        return config
