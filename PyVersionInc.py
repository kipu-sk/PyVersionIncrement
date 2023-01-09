'''
File:         PyVersionInc.py
Contents:     Module PyVersionInc
Author:       Stanislav Koncebovski (stanislav@pikkatech.eu)
Date:         2023-01-05 22:31
Version:      0.0
Copyright:    pikkatech.eu (www.pikkatech.eu)
'''

#!C:\Programs\Python\Python311/python

# The command above is the "shebang" of the interpreter.
# It causes the script below to be interpreted as a python script.
# The contents is the full path to the python.exe file (without the 'exe')
# Source: https://stackoverflow.com/questions/1547005/how-can-i-get-my-git-msysgit-on-windows-post-commit-script-to-invoke-my-python

# Import of tomllib is built-in, tomli_w not, so the latter must be installed (pip install tomli_w)
from datetime import datetime
import tomli_w
import tomllib

# the default name of the version file. The file is supposed to be placed into the same directory where .git is placed.
version_file_name = 'version.toml'

def increment_version():
    '''
    Tries to read the 'version.toml' file. Fills the document dictionary with the following values:
    "Major": current year,
    "Minor": current month,
    "Build": current day,
    "Revision": old revision incremented by 1.
    If no valid 'version.toml' is found, a new one is initialized with the value of revision 1.
    '''
    now = datetime.now()

    try:
        with open(version_file_name, 'rb') as file:
            doc = tomllib.load(file)

            if len(doc) == 0:
                doc = {'Version':{'Major':0, 'Minor':0, 'Build': 0, 'Revision': 0}}
    except Exception as e:
        print(f"Exception: {e}")
        doc = {'Version':{'Major':0, 'Minor':0, 'Build': 0, 'Revision': 0}}
        
    doc['Version']['Major']    = now.year
    doc['Version']['Minor']    = now.month
    doc['Version']['Build']    = now.day
    doc['Version']['Revision'] = doc['Version']['Revision'] + 1

    with open(version_file_name, 'wb') as file1:
        tomli_w.dump(doc, file1)

if __name__ == '__main__':
    increment_version()









