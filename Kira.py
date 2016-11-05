from Tkinter import *

def setBackgroundImage():
    root = Tk()
    root.geometry("800x600")
    background_image = PhotoImage(file='backgroundwithlogo.gif')
    background_label = Label(image=background_image)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    root.resizable(width=False, height=False)
    root.mainloop()

setBackgroundImage()

