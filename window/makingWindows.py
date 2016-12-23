from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()
    
    #init the with button
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text = "Complete")
        quitButton.place(x = 10, y = 10)
    

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()