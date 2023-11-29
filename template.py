import os 
from pathlib import Path
import logging

#logging string 
logging.basicConfig(level = logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name ='cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) #actually in windows in path backward slash are used but here above we have used forwards after folders like project_name/
    filedir, filename = os.path.split(filepath) #splitting the folders from files--filedir stores folder while filename stores files

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)#exist_ok--if folder is already created then it wont be creating
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        #if this file is not present in my directory of this file size is 0 then create
        with open(filepath,"w") as f :
            pass
            logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"{filename} already exists")
