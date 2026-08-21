#---Imports---
from customtkinter import *


#---AppGui---
class App:
    #--ctor--
    def __init__(self):  
        self.app = CTk()
        set_default_color_theme('dark-blue')
        self.app.title("Virtual Piano Bot")
        self.app.geometry('600x500')
        self.app.attributes('-topmost', True)
        self.app.resizable(False, False)
        #---TextContainer---
        self.textcontainer = CTkFrame(master=self.app, height=340)
        self.textcontainer.pack(fill=BOTH, side=BOTTOM, padx=20, pady=10)
    
        self.musicfield = CTkTextbox(self.textcontainer, width=200, height=300, font=("Consolas", 20, 'bold'), undo=True, maxundo=15)
        self.musicfield.pack(side=BOTTOM, fill=BOTH)
        
        #---ButtonsContainer---
        self.buttoncontrainer = CTkFrame(master=self.app, height=160)
        self.buttoncontrainer.pack(fill=BOTH, side=TOP)
        
        self.butStart = CTkButton(self.buttoncontrainer, text="▶ START", font=("Segoe UI", 15, "bold"), height=45, width=160, corner_radius=7)
        self.butStart.pack(side=LEFT, pady=(110, 0), padx=25)
        
        self.butStop = CTkButton(self.buttoncontrainer, text="⏹ STOP", font=("Segoe UI", 15, "bold"), height=45, width=160, corner_radius=7)
        self.butStop.pack(side=LEFT, pady=(110, 0), padx=0)
        
        #---ProgressBarContainer---
        self.progbarcont = CTkFrame(master=self.app, height=13)
        self.progbarcont.pack(fill=BOTH, side=BOTTOM)
        
        self.progbar = CTkProgressBar(self.progbarcont, height=13)
        self.progbar.pack(fill=BOTH, padx=20)


        self.app.mainloop()


#--------------run--------------
if __name__ == "__main__":
    app = App()