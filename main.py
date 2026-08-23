#---Imports---
from customtkinter import *
from bot import *

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
        self.textcontainer = CTkFrame(master=self.app, height=340, fg_color="transparent")
        self.textcontainer.pack(fill=BOTH, side=BOTTOM, padx=20, pady=10)
    
        self.musicfield = CTkTextbox(self.textcontainer, width=200, height=300, font=("Consolas", 20, 'bold'), undo=True, maxundo=15)
        self.musicfield.pack(side=BOTTOM, fill=BOTH)
        
        #---ButtonsContainer---
        self.buttoncontrainer = CTkFrame(master=self.app, height=160, fg_color="transparent")
        self.buttoncontrainer.pack(fill=BOTH, side=TOP)
        
        self.SpeedText = CTkLabel(self.buttoncontrainer, text=f'Speed: {Speed}x', fg_color="transparent", font=("Consolas", 19, 'bold'))
        self.SpeedText.pack(side=TOP, padx=(350, 0), pady=(10, 0))
        
        # self.savechang = CTkOptionMenu(self.buttoncontrainer, values=["megolav", 'tripitopi'])
        # self.savechang.pack(anchor=NW, pady=(0,45), padx=(0, 10))
        
        self.SpeedSlider = CTkSlider(self.buttoncontrainer, number_of_steps=6, width=140)
        self.SpeedSlider.pack(side=TOP, padx=(350, 0), pady=(10, 0))
        
        self.butStart = CTkButton(self.buttoncontrainer,
                                  text="▶ START",
                                  font=("Segoe UI", 15, "bold"),
                                  height=45, width=160, corner_radius=7,
                                  command=lambda: Start(self.app, self.butStart, self.butStop, self.musicfield))
        self.butStart.pack(side=LEFT, pady=(45, 0), padx=(25, 0))
        
        self.butStop = CTkButton(self.buttoncontrainer, text="⏹ STOP", font=("Segoe UI", 15, "bold"), height=45, width=160, corner_radius=7, state=DISABLED)
        self.butStop.pack(side=LEFT, pady=(45, 0), padx=(10, 0))
        
        self.butChange = CTkButton(self.buttoncontrainer, text="Change HotKey", font=("Segoe UI", 15, "bold"), height=45, width=160, corner_radius=7)
        self.butChange.pack(side=LEFT, pady=(45, 0), padx=(60, 0))
        
        
        #---ProgressBarContainer---
        self.progbarcont = CTkFrame(master=self.app, height=13, fg_color="transparent")
        self.progbarcont.pack(fill=BOTH, side=BOTTOM)
        
        self.progbar = CTkProgressBar(self.progbarcont, height=13)
        self.progbar.pack(fill=BOTH, padx=20)


        self.app.mainloop()


#--------------run--------------
if __name__ == "__main__":
    app = App()