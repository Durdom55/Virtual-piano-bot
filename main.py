#   Python 3.14.7
#   keyboard==0.13.5
#   customtkinter==6.0.0

#---Imports---
from customtkinter import * #*
from utils import Start, Stop, PreListening, clear, Save, load
from utils import config
import tkinter

#---TopLevel---
class Toplevel(CTkToplevel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.geometry('320x200')
        self.attributes('-topmost', 1)
        self.resizable(False, False)     
        icon = tkinter.PhotoImage(file='assets/iconapp.png')
        self.iconphoto(False, icon)
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
                                     command=lambda: PreListening(self, self.inputButton, self.app.toplevel_window))
        if config.HotBut != '':
            self.inputButton.configure(text=f'{config.HotBut}')
        self.inputButton.pack(fill=X, pady=10, padx=20)
        
        #---ControlFrame---
        self.conframe = CTkFrame(self, fg_color='transparent')
        self.conframe.pack(fill=X, side=BOTTOM, padx=20, pady=(10, 20))
        
        self.clearbut = CTkButton(self.conframe,
                                  text='🗑️ Clear',
                                  font=("Segoe UI", 15, "bold"),
                                  width=80, command=lambda: clear(self, self.inputButton))
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
                                 command=lambda: Save)
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
        iconM = tkinter.PhotoImage(file='assets/iconapp.png')
        self.iconphoto(False, iconM)
        
        #---TextContainer---
        self.textcontainer = CTkFrame(master=self, height=340, fg_color="transparent")
        self.textcontainer.pack(fill=BOTH, side=BOTTOM, padx=20, pady=10)
        
        def select_all(event):
            self.musicfield.tag_add('sel', '1.0', 'end-1c')
            return 'break'
    
        self.musicfield = CTkTextbox(self.textcontainer, width=200, height=300, font=("Consolas", 20, 'bold'), undo=True, maxundo=15)
        self.musicfield.pack(side=BOTTOM, fill=BOTH)
        
        self.musicfield.bind('<Control-a>', select_all)
        
        #---ButtonsContainer---
        self.buttoncontrainer = CTkFrame(master=self, height=160, fg_color="transparent")
        self.buttoncontrainer.pack(fill=BOTH, side=TOP)
        
        self.SpeedText = CTkLabel(self.buttoncontrainer, text=f'Speed: {config.Speed}x', fg_color="transparent", font=("Consolas", 19, 'bold'))
        self.SpeedText.pack(side=TOP, padx=(350, 0), pady=(10, 0))
        
        # self.savechang = CTkOptionMenu(self.buttoncontrainer, values=["megolav", 'tripitopi'])
        # self.savechang.pack(anchor=NW, pady=(0,45), padx=(0, 10))
        
        def on_slider_release(event):
            val = round(self.SpeedSlider.get(), 2)
            config.Speed=val
            Save()
            self.SpeedText.configure(text=f'Speed: {config.Speed}x') 
        
        self.SpeedSlider = CTkSlider(self.buttoncontrainer,
                                     number_of_steps=7, width=140,
                                     from_=0.25, to=2)
        self.SpeedSlider.pack(side=TOP, padx=(350, 0), pady=(10, 0))
        self.SpeedSlider.set(config.Speed)
        self.SpeedSlider.bind('<ButtonRelease-1>', on_slider_release)
        
        self.butStart = CTkButton(self.buttoncontrainer,
                                  text="▶ START",
                                  font=("Segoe UI", 15, "bold"),
                                  height=45, width=160, corner_radius=7,
                                  command=lambda: Start(self, self.butStart, self.butStop, self.musicfield, self.progbar))
        self.butStart.pack(side=LEFT, pady=(45, 0), padx=(25, 0))
        
        self.butStop = CTkButton(self.buttoncontrainer,
                                 text="⏹ STOP",
                                 font=("Segoe UI", 15, "bold"),
                                 height=45, width=160,
                                 corner_radius=7,
                                 state=DISABLED,
                                 command=lambda: Stop(self, self.butStart, self.butStop))
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
        


#--------------run--------------
if __name__ == "__main__":
    load()
    app = App()
    app.mainloop()