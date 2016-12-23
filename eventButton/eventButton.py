from tkinter import *


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        
        #cleare complete Button
        completeButton = Button(self, text = "Complete", command = self.client_exit)
        completeButton.place(x = 10, y = 10)

    
    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()