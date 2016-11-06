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

    

    def driveInfo ():
        root1= Tk ()
        text = Text(root1)
        def exit():
            root1.destroy()
        text.insert(INSERT," Hello! So your thinking of getting a lift to school? \n \n While driving can be fast and comfotable it has some disadvantages. ")
        text.insert(INSERT,"Driving is \n very bad for the enviromnet as it produces harmful CO2 gasses.\n Rather than driving consider taking the bus?")
        text.insert(INSERT,"Taking the bus produces 6-8 times \n less CO2. \n \n If you still want to travel by car why not consider car sharing?")
        text.insert(INSERT," This reduces \n the amount of cars on the road and is also better for the environment.")
        text.insert(INSERT," \n \n When traveling by car do your best not to distract the driver and always wear \n your seatbelt to keep yourself safe.")
        text.insert(END,"\n \n Try to reduce the amout you travel by car to help protect the environment.")
        text.pack()
        button = Button(text = "Back to Game",command = exit )
        button.pack()
        root1.mainloop()

    def cycleInfo ():
        root1 = Tk ()
        text = Text(root1)

        def exit():
            root1.destroy()
        button = Button(text = "Back to Game",command = exit )
        text.insert (INSERT, " Hello! So you'd like to cycle to school? \n \n Cycling is a great way to get around quickly while not harming the environment")
        text.insert (INSERT, "\n and keeping yourself hit and healthy. \n \n However make sure you are confortable with the cycling route before you set \n off.")
        text.insert (END, " \n \n It is also best to avoid major roads and remember to ALWAYS wear a helmet!")
        text.pack()
        button.pack()
        root1.mainloop()

    def walkInfo():
        root1 = Tk()
        text = Text(root1)
        def exit():
            root1.destroy()
        button = Button(text = "Back to Game",command = exit )
        text.insert(INSERT, " Hello! So your thinking of walking to school? \n did you know that walking to School is not only super good for the environment \n as it removes cars from the road. \n \n It is also great for your health and fitness.")
        text.insert(INSERT, "\n However you have to make sure to stay safe when walking in order to keep safe \n from traffic.")
        text.insert(END, "\n Choose walking to protect the environment and to keep yourself fit and healthy")
        text.pack()
        button.pack()
        root1.mainloop()
        
    bc = Button(root, text = "More info on travelling by car", command = driveInfo)
    bc.pack(side=BOTTOM)
   
    bb = Button(root,text = "More info on cycling",command = cycleInfo)
    bb.pack(side=BOTTOM)

    bw = Button(root,text = "More info on walking",command = walkInfo)
    bw.pack(side=BOTTOM)
    

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
