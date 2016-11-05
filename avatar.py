from Tkinter import *

root = Tk()

def page1():
    #functions to select the avatar
    def headphones():
        print "headphones"
        #to next page

    def hiVis():
        print "hiVis"
        #to next page

    def phone():
        print "phone"
        #to next page

    def hoodie():
        print "hoodie"
        #to next page

    def cap():
        print "cap"
        #to next page

    def elderly():
        print "elderly"
        #to next page


    canvas = Canvas(root, width = 1000, height = 300)
    canvas.pack()

    choiceL = Label(text = "Choose your avatar: ", font = "comic")
    choiceL.pack(anchor = N)

    #avatars to click on
    b1 = Button(root,command = headphones)
    b1.pack(side=LEFT)
    photoHP = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\headphones.gif",width = 150,height = 300)
    b1.config(image = photoHP,compound = CENTER)

    b2 = Button(root,command = hiVis)
    b2.pack(side = LEFT)
    photoHV = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\hiVis.gif",width = 150,height = 300)
    b2.config(image = photoHV,compound = CENTER)

    b3 = Button(root,command = phone)
    b3.pack(side = LEFT)
    photoP = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\phone.gif",width = 150,height = 300)
    b3.config(image = photoP,compound = CENTER)

    b4 = Button(root,command = hoodie)
    b4.pack(side = LEFT)
    photoH = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\hoodie.gif",width = 150,height = 300)
    b4.config(image = photoH,compound = CENTER)

    b5 = Button(root,command = cap)
    b5.pack(side = LEFT)
    photoC = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\cap.gif",width = 150,height = 300)
    b5.config(image = photoC,compound = CENTER)

    b6 = Button(root,command = elderly)
    b6.pack(side = LEFT)
    photoE = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\elderly.gif",width = 150,height = 300)
    b6.config(image = photoE,compound = CENTER)

    bExit = Button(text = "Next")
    bExit.pack(side=LEFT)



    root.minsize(width=1000,height = 300)

    root.title("Brake road safety")






    #brake logos
    photo1 = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\brake.gif")
    canvas.create_image(0,0, anchor = NW, image = photo1)

    photo2 = PhotoImage(file="C:\\Users\\andyj\\Documents\\tkinter\\brake.gif")
    canvas.create_image(800,0, anchor = NW, image = photo2)


    root.mainloop()
#page1()
