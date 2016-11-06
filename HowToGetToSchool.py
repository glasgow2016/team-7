from Tkinter import *

root = Tk()

def page2():
    #functions to select the avatar
    def car():
        print "By car"
        #to next page

    def bike():
        print "Cycling"
        #to next page

    def walk():
        print "Walking"
        #to next page



    canvas = Canvas(root, width = 1000, height = 300)
    canvas.pack()

    choiceL = Label(text = "How would you like to get to school?", font = "comic")
    choiceL.pack(anchor = N)

    #avatars to click on
    b1 = Button(root,command = car)
    b1.pack(side=LEFT)
    photoCAR = PhotoImage(file="car.gif",width = 300,height = 300)
    b1.config(image = photoCAR,compound = CENTER)

    b2 = Button(root,command = bike)
    b2.pack(side = LEFT)
    photoBIKE = PhotoImage(file="bicycle.gif",width = 300,height = 300)
    b2.config(image = photoBIKE,compound = CENTER)

    b3 = Button(root,command = walk)
    b3.pack(side = LEFT)
    photoWALK = PhotoImage(file="walk.gif",width = 300,height = 300)
    b3.config(image = photoWALK,compound = CENTER)

    

    bExit = Button(text = "Next")
    bExit.pack(side=LEFT)



    root.minsize(width=1000,height = 300)

    root.title("Brake road safety")






    #brake logos
    photo1 = PhotoImage(file="brake.gif")
    canvas.create_image(0,0, anchor = NW, image = photo1)

    photo2 = PhotoImage(file="brake.gif")
    canvas.create_image(800,0, anchor = NW, image = photo2)


    root.mainloop()
page2()
