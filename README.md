# My-Story-Lab
Using `pyenv` & `virtualenv`, I set up a virtual env named `it4063c-3-10-4`.
It's advisable that you create a new virtual env. for every assignment you work on to avoid dependency conflicts.

to get started on this project, in your virtual env. install the project dependencies
install poetry 
```bash 
pip install poetry
```
then run 
```bash 
poetry install
```

OR 

using 
```bash
pip install -r requirements.txt
```

to run the automated tests 
```bash 
pytest --capture=sys
```

## Project Structure
```
.
├── .git                1️⃣  
├── .vscode             2️⃣  
│   ├── extensions.json 
│   └── settings.json   
├── .gitignore          3️⃣  
├── my_story.ipynb      4️⃣  
├── notebook_test.py    5️⃣  
├── README.md           6️⃣  
└── requirements.txt    7️⃣  
```
1️⃣ DO NOT TOUCH THIS DIRECTORY. This is what makes your folder a git repo.
2️⃣ This directory contains some supporting files for helpful extensions, and VSCode settings 
3️⃣ Another git related files. This tells git not to track certain files and folders that you don't want being uploaded
4️⃣ That's where the party is. You'll only be working in this file.
5️⃣ Some automated tests and checks
6️⃣ The README file (this right here)
7️⃣ The dependencies needed for this project. Actually deps and deps of deps, ...etc.