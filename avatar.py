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


    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack(expand=YES, fill=BOTH)
    image = PhotoImage(file='backgroundwithlogo.gif')
    canvas.create_image(0,0,image=image,anchor=NW)
    canvas.create_text(800/2, 150, text = "Choose your avatar: ", font = ("Berlin Sans FB",20))
    #choiceL.pack(anchor = N)

    #avatars to click on
    b1 = Button(root,command = headphones)
    b1.place(x=20,y=200)
    #b1.pack(side=LEFT)
    photoHP = PhotoImage(file="headphones.gif",width = 130,height = 300)
    b1.config(image = photoHP,compound = CENTER)

    b2 = Button(root,command = hiVis)
    b2.place(x=150, y=200)
    #b2.pack(side = LEFT)
    photoHV = PhotoImage(file="hiVis.gif",width = 130,height = 300)
    b2.config(image = photoHV,compound = CENTER)

    b3 = Button(root,command = phone)
    b3.place(x=280, y=200) 
    #b3.pack(side = LEFT)
    photoP = PhotoImage(file="phone.gif",width = 130,height = 300)
    b3.config(image = photoP,compound = CENTER)

    b4 = Button(root,command = hoodie)
    b4.place(x=410, y=200)
    #b4.pack(side = LEFT)
    photoH = PhotoImage(file="hoodie.gif",width = 130,height = 300)
    b4.config(image = photoH,compound = CENTER)

    b5 = Button(root,command = cap)
    b5.place(x=540, y=200)
    #b5.pack(side = LEFT)
    photoC = PhotoImage(file="cap.gif",width = 130,height = 300)
    b5.config(image = photoC,compound = CENTER)

    b6 = Button(root,command = elderly)
    b6.place(x=670, y=200)
    #b6.pack(side = LEFT)
    photoE = PhotoImage(file="elderly.gif",width = 130,height = 300)
    b6.config(image = photoE,compound = CENTER)

    bExit = Button(text = "Next")
    bExit.place(x=700, y=550)
    #bExit.pack(side=LEFT)



    #root.minsize(width=1000,height = 300)

    #root.title("Brake road safety")






    #brake logos
    #photo1 = PhotoImage(file="brake.gif")
    #canvas.create_image(0,0, anchor = NW, image = photo1)

    #photo2 = PhotoImage(file="brake.gif")
    #canvas.create_image(800,0, anchor = NW, image = photo2)


    root.mainloop()
page1()
