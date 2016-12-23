from tkinter import *


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        #creating a Menu
        menu = Menu(self.master)
        self.master.config(menu = menu)

        #create a menu
        file = Menu(menu)
        #add Edit option
        file.add_command(label='Settings')
        #add Exit Option
        file.add_command(label='Exit', command=self.client_exit)
        

        #add the submenu to menu
        menu.add_cascade(label='File', menu = file)


        #add another undo menu
        edit = Menu(menu)
        edit.add_command(label='Undo')

        menu.add_cascade(label='Edit', menu=edit)

        
        #cleare complete Button
        completeButton = Button(self, text = "Complete", command = self.client_exit)
        completeButton.place(x = 10, y = 10)

    
    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()