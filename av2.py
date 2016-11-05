from Tkinter import *

root = Tk()

b1 = Button(root)
b1.pack()

photoHP = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\headphones.gif")

b1.config(image = photoHP,compound = CENTER)

root.mainloop()
