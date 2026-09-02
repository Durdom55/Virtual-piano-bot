#   Python 3.14.7
#   keyboard==0.13.5
#   customtkinter==6.0.0

#---Imports---
from customtkinter import * #*
from utils import config, Start, Stop, PreListening, clear, Save, load, ToDefault, NewSong
import re

#---Toplevel2 (Advanced Settings)---
class AdvLevel(CTkToplevel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.geometry('200x320')
        self.resizable(False, False)
        self.attributes('-topmost', 1)
        
        CTkLabel(master=self, text='Delay (sec)', font=('Consolas', 16)).pack(pady=(5, 0))
        
        self.sleepframe = CTkFrame(master=self, fg_color='transparent')
        self.sleepframe.pack(fill=X, pady=5, padx=7)
        
        CTkLabel(self.sleepframe, text='Sleeptime', font=('Consolas', 14)).pack(side=LEFT)
        
        def valid_positive(new_value):
            return bool(re.fullmatch(r'\d*\.?\d*', new_value))
        
        def valid_negative(new_value):
            return bool(re.fullmatch(r'-\d*\.?\d*', new_value))
        
        self.sleepen = CTkEntry(self.sleepframe, width=90, font=('Arial', 14), validate='key', validatecommand=(self.register(valid_positive), '%P'))
        self.sleepen.pack(side=RIGHT, padx=(5,0))
        self.sleepen.set(config.Sleep)
        
        CTkLabel(self, text='Delay offset (sec)', font=('Consolas', 16)).pack(pady=(8, 0))
        
        self.frame1 = CTkFrame(self, fg_color='transparent')
        self.frame1.pack(fill=X, pady=(5,0), padx=40)
        CTkLabel(self.frame1, text= '-', font=('Consolas', 14, 'bold')).pack(side=LEFT)
        self.dEn = CTkEntry(self.frame1, width=90, font=('Arial', 14), validate='key', validatecommand=(self.register(valid_positive), '%P'))
        self.dEn.pack(side=RIGHT, padx=(5, 0))
        self.dEn.set(config.dash)
        
        self.frame2 = CTkFrame(self, fg_color='transparent')
        self.frame2.pack(fill=X, pady=(5,0), padx=40)
        CTkLabel(self.frame2, text= '–', font=('Consolas', 14, 'bold')).pack(side=LEFT)
        self.middEn = CTkEntry(self.frame2, width=90, font=('Arial', 14), validate='key', validatecommand=(self.register(valid_positive), '%P'))
        self.middEn.pack(side=RIGHT, padx=(5, 0))
        self.middEn.set(config.middash)
        
        self.frame3 = CTkFrame(self, fg_color='transparent')
        self.frame3.pack(fill=X, pady=(5,0), padx=40)
        CTkLabel(self.frame3, text= '—', font=('Consolas', 14, 'bold')).pack(side=LEFT)
        self.bigdEn = CTkEntry(self.frame3, width=90, font=('Arial', 14), validate='key', validatecommand=(self.register(valid_positive), '%P'))
        self.bigdEn.pack(side=RIGHT, padx=(5, 0))
        self.bigdEn.set(config.bigdash)
        
        self.frame4 = CTkFrame(self, fg_color='transparent')
        self.frame4.pack(fill=X, pady=(5,0), padx=40)
        CTkLabel(self.frame4, text= '{}', font=('Consolas', 14, 'bold')).pack(side=LEFT)
        self.par = CTkEntry(self.frame4, width=90, font=('Arial', 14), validate='key', validatecommand=(self.register(valid_negative), '%P'))
        self.par.pack(side=RIGHT, padx=(5, 0))
        self.par.set(config.parenthesis)
        
        self.butframe1 = CTkFrame(self, fg_color='transparent')
        self.butframe1.pack(fill=X, pady=(15, 5))
        
        self.sabut = CTkButton(self.butframe1,
                               text='💾 Save',
                               font=('Segoe UI', 14),
                               width=80,
                               fg_color="#4CAF50",
                               hover_color="#388E3C",
                               command=Save)
        self.sabut.pack(side=LEFT, padx=(15, 0))
        
        self.canbut = CTkButton(self.butframe1,
                                text='❌ Cancel',
                                font=('Segoe UI', 14),
                                width=80,
                                fg_color="#F44336",
                                hover_color="#D32F2F",
                                command=self.destroy)
        self.canbut.pack(side=RIGHT, padx=(0, 15))
        
        self.butframe1 = CTkFrame(self, fg_color='transparent')
        self.butframe1.pack(fill=X)
        
        self.defbut = CTkButton(self.butframe1, text='Set to Default', font=('Segoe UI', 13),
                                command=lambda: ToDefault(self))
        self.defbut.pack(side=BOTTOM)
        
        #--Change--
        def changes(event, entry, name):
            text = entry.get().strip()
            
            if text != '' and text[0] == "-":
                if text in ('', '-'):
                    entry.configure(validate='none')
                    entry.set(config.default_parenthesis)
                    entry.configure(validate='key')
                    return
                config.parenthesis = float(self.par.get())
                return
            if text in (''):
                entry.configure(validate='none')
                match name:
                    case 'Sleep':
                        entry.set(config.default_Sleep)
                    case 'dash':
                        entry.set(config.default_dash)
                    case 'middash':
                        entry.set(config.default_middash)
                    case 'bigdash':
                        entry.set(config.default_bigdash)
                entry.configure(validate='key')
                return
            match name:
                case 'Sleep':
                    config.Sleep = float(entry.get())
                case 'dash':
                    config.dash = float(entry.get())
                case 'middash':
                    config.middash = float(entry.get())
                case 'bigdash':
                    config.bigdash = float(entry.get())
            return
        
        #--Bind--
        self.sleepen.bind('<FocusOut>', lambda e: changes(e, self.sleepen, 'Sleep'))
        self.dEn.bind('<FocusOut>', lambda e: changes(e, self.dEn, 'dash'))
        self.middEn.bind('<FocusOut>', lambda e: changes(e, self.middEn, 'middash'))
        self.bigdEn.bind('<FocusOut>', lambda e: changes(e, self.bigdEn, 'bigdash'))
        self.par.bind('<FocusOut>', lambda e: changes(e, self.par, ''))
        
        self.grab_set()
        self.transient(self.app)
        

#---TopLevel (HotKey)---
class Toplevel(CTkToplevel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.geometry('320x200')
        self.attributes('-topmost', 1)
        self.resizable(False, False)     
        CTkLabel(self, text='HotKey settings',
                 font=("Consolas", 22, 'bold')).pack(pady=(20, 10), padx=20)
        self.inputButton = CTkButton(self,
                                     text='Click to Set Hotkey',
                                     font=(("Arial", 17, "bold")),
                                     height=60,
                                     fg_color='#413f41',
                                     hover_color="#3a383a",
                                     border_color="#5a575a",
                                     border_width=2,
                                     command=lambda: PreListening(self, self.app.toplevel_window))
        if config.HotBut != '':
            self.inputButton.configure(text=f'{config.HotBut}')
        self.inputButton.pack(fill=X, pady=10, padx=20)
        
        #---ControlFrame---
        self.conframe = CTkFrame(self, fg_color='transparent')
        self.conframe.pack(fill=X, side=BOTTOM, padx=20, pady=(10, 20))
        
        self.clearbut = CTkButton(self.conframe,
                                  text='🗑️ Clear',
                                  font=("Segoe UI", 15, "bold"),
                                  width=80, command=lambda: clear(self))
        self.clearbut.pack(side=LEFT, padx=5)
        self.cancelbut = CTkButton(self.conframe,
                                   text='❌ Cancel', 
                                   font=("Segoe UI", 15, "bold"),
                                   width=80,
                                   fg_color="#F44336",
                                   hover_color="#D32F2F",
                                   command=self.destroy)
        self.cancelbut.pack(side=RIGHT, padx=5)
        self.savebut = CTkButton(self.conframe,
                                 text='💾 Save',
                                 font=("Segoe UI", 15, "bold"),
                                 width=80,
                                 fg_color="#4CAF50",
                                 hover_color="#388E3C",
                                 command=Save)
        self.savebut.pack(side=RIGHT, padx=5)
        
        self.grab_set()
        self.transient(self.app)
        
#---AppGui---
class App(CTk):
    #--ctor--
    def __init__(self): 
        super().__init__() 
        set_default_color_theme('dark-blue')
        self.title("Virtual Piano Bot")
        self.geometry('600x500')
        self.attributes('-topmost', True)
        self.resizable(False, False)
        
        #---TextContainer---
        self.textcontainer = CTkFrame(master=self, height=340, fg_color="transparent")
        self.textcontainer.pack(fill=BOTH, side=BOTTOM, padx=20, pady=10)
        
        def select_all(event):
            self.musicfield.tag_add('sel', '1.0', 'end-1c')
            return 'break'
    
        self.musicfield = CTkTextbox(self.textcontainer, width=200, height=300, font=("Consolas", 20, 'bold'), undo=True, maxundo=15)
        self.musicfield.pack(side=BOTTOM, fill=BOTH)
        
        self.musicfield.bind('<Control-a>', select_all)
        
        #---OtherContainer
        self.othercontainer = CTkFrame(master=self, fg_color='transparent', height=65)
        self.othercontainer.pack(fill=X, side=TOP)
        self.othercontainer.pack_propagate(False)
        
        self.saveSong = CTkButton(self.othercontainer, text='Save Song', width=80, height=30)
        self.saveSong.pack(side=LEFT, padx=(10, 0))
        
        self.plussong = CTkButton(self.othercontainer, text="+", width=30, command=lambda: NewSong(self))
        self.plussong.pack(side=LEFT, padx=(5, 0))
        
        self.allsongs = CTkComboBox(self.othercontainer, width=200, values=config.songs)
        self.allsongs.pack(side=LEFT, padx=(15, 0))
        
        #--RightFrame--
        rightframe = CTkFrame(self.othercontainer, fg_color='transparent')
        rightframe.pack(side=RIGHT, anchor=E, padx=(0, 20), pady=5)
        
        #-TopLine-
        topline = CTkFrame(rightframe, fg_color='transparent')
        topline.pack(side=TOP, anchor=E)
        
        self.Advbut = CTkButton(topline,
                                text='⚙️',
                                font=('Segoe UI', 23),
                                height=27, width=30,
                                fg_color='#565c63',
                                hover_color='#5d5d5d',
                                command=self.opadvlevel)
        self.Advbut.pack(side=RIGHT, padx=(5, 0))
        
        self.SpeedText = CTkLabel(topline, text=f'Speed: {config.Speed}x', fg_color="transparent", font=("Consolas", 19, 'bold'))
        self.SpeedText.pack(side=RIGHT, padx=(0, 10))
        
        def on_slider_release(event):
            val = round(self.SpeedSlider.get(), 2)
            config.Speed=val
            Save()
            self.SpeedText.configure(text=f'Speed: {config.Speed}x') 
        
        self.SpeedSlider = CTkSlider(rightframe,
                                     number_of_steps=7, width=140,
                                     from_=0.25, to=2)
        self.SpeedSlider.pack(side=TOP, anchor=E, pady=(0, 0), padx=(0, 37))
        self.SpeedSlider.set(config.Speed)
        self.SpeedSlider.bind('<ButtonRelease-1>', on_slider_release)
        
        self.advset_win = None
        
        #---ButtonsContainer---
        self.buttoncontrainer = CTkFrame(master=self, height=160, fg_color="transparent")
        self.buttoncontrainer.pack(fill=BOTH, side=TOP)
        
        
        self.butStart = CTkButton(self.buttoncontrainer,
                                  text="▶ START",
                                  font=("Segoe UI", 15, "bold"),
                                  height=45, width=160, corner_radius=7,
                                  command=lambda: Start(self))
        #self, self.butStart, self.butStop, self.musicfield, self.progbar
        self.butStart.pack(side=LEFT, pady=(45, 0), padx=(25, 0))
        
        self.butStop = CTkButton(self.buttoncontrainer,
                                 text="⏹ STOP",
                                 font=("Segoe UI", 15, "bold"),
                                 height=45, width=160,
                                 corner_radius=7,
                                 state=DISABLED,
                                 command=lambda: Stop(self))
        self.butStop.pack(side=LEFT, pady=(45, 0), padx=(10, 0))
        
        self.butHK = CTkButton(self.buttoncontrainer,
                               text="Change HotKey",
                               font=("Segoe UI", 15, "bold"),
                               height=45, width=160, corner_radius=7,
                               command=self.opentoplevel)
        self.butHK.pack(side=LEFT, pady=(45, 0), padx=(60, 0))
        
        self.toplevel_window = None
        
        #---ProgressBarContainer---
        self.progbarcont = CTkFrame(master=self, height=13, fg_color="transparent")
        self.progbarcont.pack(fill=BOTH, side=BOTTOM)
        
        self.progbar = CTkProgressBar(self.progbarcont, height=13)
        self.progbar.pack(fill=BOTH, padx=20)
        self.progbar.set(0)
        
        
    #---OpenTopLevel---
    def opentoplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            if not config.Iswait:          
                self.toplevel_window = Toplevel(self)
        else:
            self.toplevel_window.focus()
    
    def opadvlevel(self):
        if self.advset_win is None or not self.advset_win.winfo_exists():
            if not config.Iswait:          
                self.advset_win = AdvLevel(self)
        else:
            self.advset_win.focus()
        


#--------------run--------------
if __name__ == "__main__":
    load()
    app = App()
    app.mainloop()