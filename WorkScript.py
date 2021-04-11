import os
import subprocess, sys

print('hello, what project do you want to work on?')
# here i will input what project I Want to open
# VV this will loop through dir and list all of the projects with their associated number
i = 1
for file in os.listdir(r'C:\Users\ibuta\Desktop\Code'):
    if(file != '.git'):
        print(f'{i} : {file}')
        i += 1

# user will select which file they want opened
number = input('Project Number: ')

folder = os.listdir(r'C:\Users\ibuta\Desktop\Code')[int(number)]
# run npm start for the selected file
subprocess.Popen(['powershell.exe', fr'npm start --prefix C:\Users\ibuta\Desktop\Code\{folder}'])
# this will open up the IDE
subprocess.Popen(['powershell.exe', fr'code .\Code\{folder}'])
# # # this will open up windows terminal
path = fr'C:\Users\ibuta\Desktop\Code\{folder}'
subprocess.Popen(['wt', '-d', path])

os.startfile(r"C:\Users\ibuta\Desktop\uncap.exe")