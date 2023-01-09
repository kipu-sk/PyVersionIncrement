# PyVersionIncrement
## Problem Statement

When programming with languages like C++ or C#, code is compiled before each debugging action. With each compilation run, the version of the code can be incremented automatically. The most common format for a version number is as follows:

Major.Minor.Build.Revision,

e.g. 2023.1.6.42 .

The idea behind automatic version increment for Python code cannot be bound with compilation, since it does not take place. What can be done, is to connect version increment with git commit. Below is described a way to do it using the following three elements:

    * a Python script that reads a text file with version number data, increments the version, and saves the file;
    * git hook post-commit containing that script
    * git template that ensures that the post-commit hook will be automatically copied into the .git folder with each new git init.
    
 ## Pythn script
 PyVersionInc.py
 
 ### Additional explanations to the script
 The comments contained in the code explain it functioning and requirements; however, the following should be pointed to:

    The code should contain the 'shebang' in the first line, pointing to the Python executable used as the interpreter;
    The tomllib is built-in (at least in Python 3.11), the tomli_w library enables pretty writing of the toml document to a file must be installed (pip install tomli_w);
    The name of the file containing the version data is hard-coded (version.toml); its format is toml () source;
    The version name format is fixed:
        Major: current year,
        Minor: current month,
        Build: current day,
        Revision: old revision incremented by 1.
    The version.toml file is located in the folder containing the .git directory;
    If no version.toml is found in the folder containing the .git directory, a new one will be created with revision number 1;

## Git Hook

The above Python script is placed within a Git hook post-commit in the .git/hooks directory

## Git Template

In order to automatically copy the post-commit hook into each newly created repository, the following things must be done ( source).
### Create a Git Template Folder

Using Windows Explorer or Command Prompt, create a dedicated folder for the templates, e.g. ~/.git_template (~ is the 'home' directory of the user under Windows, e.g. if the user name is 'Monika', ~ corresponds to C:\Users\Monika)
### Create a Subfolder for Hooks

Within the templates folder (~/.git_template) create a subfolder hooks.
### Put the Hook Script into that folder

Copy your post-commit script into ~/.git_template/hooks.
### Register The template Folder with Git

To do that you will have to perform the following (using Command Prompt):

git config --global init.templatedir ~/.git_template

### Test the Installation

Create a new repository and perform a commit. If everything was OK, you will find a version.toml file in the folder.
    

