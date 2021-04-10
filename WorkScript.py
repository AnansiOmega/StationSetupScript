import os
import subprocess, sys
from subprocess import PIPE
import time

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
# subprocess.Popen(['powershell.exe', fr'npm start --prefix C:\Users\ibuta\Desktop\Code\{folder}'], stdout=sys.stdout)
# this will open up the IDE
subprocess.Popen(['powershell.exe', fr'code .\Code\{folder}'], stdout=sys.stdout)
# this will open up windows terminal
x = subprocess.Popen(['wt.exe'], stdin=PIPE, stdout=PIPE)
x.stdout.readline()
line = fr'cd C:\Users\ibuta\Desktop\Code\{folder}'
arr = bytes(line, 'utf-8')
x.stdin.write(line)
time.sleep(19)
# os runs npm start in dir


# User should be able to tab through the files within the folder


# os.startfile(r"C:\Users\ibuta\Desktop\Code\uncap.exe")
