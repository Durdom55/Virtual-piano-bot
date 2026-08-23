#---Import---
import keyboard
import threading
import time
from tkinter.messagebox import showwarning
from config import *

#---Var---
cache = ''
cacheOn = False
Sleep=0.4

#---Func---
def BotPlay(text):
    global cacheOn, Sleep, cache, IsRun
    text = text.get('0.0', 'end')
    print('text get')
    if IsRun==True:
        for i in text:
            print(i)
            if i in [' ', '[', ']', '{', '}', '-', '—', '–']:
                match i:
                    case ' ':
                        time.sleep(Sleep/Speed)
                    case '[':
                        cacheOn=True
                    case ']':
                        cacheOn=False
                        print(cache)
                        cash_press(cache)
                        cache=''
                        time.sleep(Sleep/Speed)
                    case '{':
                        Sleep-=0.15
                    case '}':
                        Sleep=0.4
                    case '-':
                        time.sleep(0.5)
                    case '—':
                        time.sleep(0.6)
                    case '–':
                        time.sleep(0.55)
            else:
                if cacheOn==True:
                    cache+=i
                else:
                    if i.isupper():
                        keyboard.send(f'shift+{i.lower()}')
                    else:      
                        keyboard.send(i)
                    time.sleep(Sleep/Speed)
    
def cash_press(cache):
    for i in cache:
        if i.isupper():
            keyboard.send(f'shift+{i.lower()}')
        else:      
            keyboard.send(i)

def Wait(app, buts, butp, text):
    global IsRun
    if HotBut!='':
        if keyboard.is_pressed(HotBut) and NotRecord:
            if IsRun == False:
                StartBut(buts, butp, text)
            else:
                StopBut(buts, butp)
    else:
        showwarning(title='Warning', message='Set HotKey for proper operation')
        return
    app.after(30, lambda: Wait(app, buts, butp, text))
    
def Start(app, buts, butp, text):
    buts.configure(state='disabled')
    buts.configure(text=f'Press {HotBut} to playing')
    butp.configure(state='enabled')
    Wait(app, buts, butp, text)
                
def StopBut(buts, butp):
    global IsRun, cacheOn, cache, Sleep
    cache = ''
    cacheOn = False
    Sleep=0.417
    print("Stop")
    IsRun=False
    buts.configure(state='enabled')
    butp.configure(state='disabled')
    while keyboard.is_pressed(HotBut):
        time.sleep(0.01)
    
def StartBut(buts, butp, text):
    global IsRun
    print("Start")
    IsRun=True
    while keyboard.is_pressed(HotBut):
        time.sleep(0.01)
    threading.Thread(target=BotPlay(text), daemon=True).start()