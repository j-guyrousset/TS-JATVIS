import os
import subprocess as sp

paths = {
    'notepad':r"C:\Windows\System32\notepad.exe",
    'calculator': r"C:\Windows\System32\calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell = True)


def open_notepad():
    os.startfile(paths['notepad'])

def open_calc():
    os.startfile(paths['calculator'])


def open_cmd():
    os.system('start cmd')


def print_in_notepad(text):
    file = open(r'C:\Users\Jean-Guy\Documents\python_tony_starks_jarvis\log.txt','a')
    file.write(text)
    file.close()
    os.startfile(r'C:\Users\Jean-Guy\Documents\python_tony_starks_jarvis\log.txt')
