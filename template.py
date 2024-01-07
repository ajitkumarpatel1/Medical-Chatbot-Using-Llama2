import os                          # Accesing the operating system
from pathlib import Path           # Handling the path object (linux/ to windows\)
import logging                     # Logging the activity of code

# Loging the information 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",             # This files helps to make Src as a local package
    "src/helper.py",               # This contain all the code related to "Data injection" component
    "src/prompt.py",               # This contain the Promtemplate for instruction LLM model.
    ".env",                        # This file contain all the Crediential (uid, password)
    "setup.py",                    # This file trigger the requirements.txt and make src file as a local packages 
    "research/trials.ipynb",       # This file contain all the R&D notebook and files
    "app.py",                      # This file contain all the code related to "Flask" for web-ui development
    "store_index.py",              # This file contain all the code for Push the embeding vector to Vector DB
    "static/style.css",             # This file contail the css code web app
    "templates/chat.html"          # This file contain the HTML for web app

]

# Creating the the upper folder stracture
for filepath in list_of_files:
    filepath = Path(filepath)                             # Converting into a windows path object
    filedir, filename = os.path.split(filepath)           # Separating Folder and files prent inside the list

    # If filedir is not empty then then create else noting to do. and log the info.
    if filedir !="":                                       
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    # If filedir is not present or the filedir size is 0 then create the file. and log the info.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    # if the file is already exist loging the info.
    else:
        logging.info(f"{filename} is already created")