#---Import---
import keyboard
import threading
import time
from tkinter.messagebox import showwarning
from config import *

#---Var---
cache = ''
cacheOn = False

#---Func---
def BotPlay(text, pb):
    global cacheOn, Sleep, cache, IsRun
    text = text.get('0.0', 'end')
    numofsteps = len(text)
    progVal = 1/numofsteps
    stepVal = 0
    Sleeptime=Sleep
    print('text get')
    if IsRun==True:
        for i in text:
            if not IsRun:
                break
            print(i)
            stepVal+=progVal
            pb.set(stepVal)
            if i in [' ', '[', ']', '{', '}', '-', '—', '–']:
                match i:
                    case ' ':
                        time.sleep(Sleeptime/Speed)
                    case '[':
                        cacheOn=True
                    case ']':
                        cacheOn=False
                        print(cache)
                        cash_press(cache)
                        cache=''
                        time.sleep(Sleeptime/Speed)
                    case '{':
                        Sleeptime-=0.15
                    case '}':
                        Sleeptime=Sleep
                    case '-':
                        time.sleep(0.5/Speed)
                    case '—':
                        time.sleep(0.6/Speed)
                    case '–':
                        time.sleep(0.55/Speed)
            else:
                if cacheOn==True:
                    cache+=i
                else:
                    if i.isupper():
                        keyboard.send(f'shift+{i.lower()}')
                    else:      
                        keyboard.send(i)
                    time.sleep(Sleeptime/Speed)
    IsRun = False
    
def cash_press(cache):
    for i in cache:
        if i.isupper():
            keyboard.send(f'shift+{i.lower()}')
        else:      
            keyboard.send(i)

def Wait(app, buts, butp, text, pb):
    global IsRun
    if HotBut!='':
        if keyboard.is_pressed(HotBut) and NotRecord:
            print("nazhata")
            if IsRun == False:
                print("Startw")
                StartBut(buts, text, pb)
            else:
                print('StopW')
                StopBut(buts, butp)
    else:
        showwarning(title='Warning', message='Set HotKey for proper operation')
        return
    app.after(30, lambda: Wait(app, buts, butp, text, pb))
    
def Start(app, buts, butp, text, pb):
    buts.configure(state='disabled')
    buts.configure(text=f'Press {HotBut} to playing')
    butp.configure(state='normal')
    Wait(app, buts, butp, text, pb)
    
def Stop(buts, butp):
    buts.configure(state='normal')
    buts.configure(text='▶ START')
    butp.configure(state='disabled')
                
def StopBut(buts, butp):
    global IsRun, cacheOn, cache, Sleep
    cache = ''
    cacheOn = False
    Sleep=0.417
    print("Stop")
    buts.configure(text=f'Press {HotBut} to playing')
    IsRun=False
    while keyboard.is_pressed(HotBut):
        time.sleep(0.01)
    
def StartBut(buts, text, pb):
    global IsRun
    print("Start")
    pb.set(0)
    IsRun=True
    buts.configure(text=f'Press {HotBut} to stop')
    while keyboard.is_pressed(HotBut):
        time.sleep(0.01)
    threading.Thread(target=BotPlay, args=(text,pb, ), daemon=True).start()