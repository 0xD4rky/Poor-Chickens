## i will be using this to create folders ##

import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "CNN Classifier"

## i will now define the list of files required for my project

list_of_files = [                     
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # to install my project on local interpreter
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dcv.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)  # i am doing this since windows uses backward slash and i gave foward slashes
    file_dir,file_name = os.path.split(filepath)
    
    if file_dir !="":
        os.makedirs(file_dir,exist_ok = True)
        logging.info(f"Creating directory; {file_dir} for the file {file_name}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    
    else: 
        logging.info(f"{file_name}  already exists")
        
        