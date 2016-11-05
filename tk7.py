from Tkinter import *

root = Tk()

def headphones():
    photoHP = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\headphones.gif")
    canvas.create_image(200,100, anchor = NW, image = photoHP)
    
def hiVis():
    photoHV = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\hiVis.gif")
    canvas.create_image(200,100, anchor = NW, image = photoHV)

def phone():
    photoP = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\phone.gif")
    canvas.create_image(200,100, anchor = NW, image = photoP)



root.configure(background = "white")

root.minsize(width=1000,height = 300)
root.title("Brake road safety")

choiceL = Label(text = "Choose your avatar: ")
choiceL.pack(anchor = CENTER)

canvas = Canvas(root, width = 1000, height = 300)
canvas.pack()

photo1 = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\brake.gif")
canvas.create_image(0,0, anchor = NW, image = photo1)

photo2 = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\brake.gif")
canvas.create_image(755,0, anchor = NW, image = photo2)


v = IntVar()

r1 = Radiobutton(root, text="Headphoned teenager", variable=v, value=1,command=headphones)
r2 = Radiobutton(root, text="Hi-vis jacket", variable=v, value=2,command=hiVis)
r3 = Radiobutton(root, text="Man looking at his phone", variable=v, value=3,command=phone)

r1.pack(anchor=S)
r2.pack(anchor=S)
r3.pack(anchor=S)



root.mainloop()
