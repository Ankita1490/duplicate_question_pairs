import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format = '[%(asctime)s]: %(message)s:')
file_list=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/constants/__init__.py",
    "src/entity/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for file_path in file_list:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory {file_dir} for the file: {file_name}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} is already present")
