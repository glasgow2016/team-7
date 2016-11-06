from Tkinter import *

root = Tk()
root.geometry("800x600")
def setBackgroundImage():
    root.geometry("800x600")
    background_image = PhotoImage(file='backgroundwithlogo.gif')
    background_label = Label(image=background_image)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    root.resizable(width=False, height=False)
    
root.resizable(width=False, height=False)
#setBackgroundImage()

canvas_width = 800
canvas_height = 600
w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack(expand=YES, fill=BOTH)    
image = PhotoImage(file='backgroundwithlogo.gif')
w.create_image(0,0,image=image,anchor=NW)
button_next = PhotoImage(file='next_button.gif')
button = Button(w, image=button_next)
character_name = ""
stage = 0
def runMain():
    print "run main"
    print move_to_next_page
    if(move_to_next_page):
        print "next page"
        loadCharNamePage()

def onObjectClick(event):
    global stage
    stage += 1
    print "value of stage ", stage 
    w.delete("title")
    print "we should move to next stage!"
    if(stage == 1):
        loadCharNamePage()
        print "Your character name is ", character_name
    if(stage == 2):
        print "we move to choosing avatar"
        w.delete("setname")
        w.delete("name")
        w.delete(ALL)
        c_width = 800
        c_height = 600
        canvas = Canvas(root, width = c_width, height = c_height)
        canvas.pack(expand=YES, fill=BOTH)    
        image = PhotoImage(file='backgroundwithlogo.gif')
        canvas.create_image(0,0,image=image,anchor=NW)
        page2(canvas)
    
def loadMainPage():
    w.create_text(canvas_width/2, (canvas_height-50)/2, text="Brake Road to Safety",font=("Berlin Sans FB",35), tag="title")
    #button = Button(w, image=button_next)
    button.place(x=570, y=430, width=150)
    button.bind('<Button-1>', onObjectClick)
    
    #button.tag_bind(button, '<Button-1>', onObjectClick)
    

def loadCharNamePage():
    print "char name page"
    w.create_text(canvas_width/2, (canvas_height-50)/2, text="Don't forget to give your character a name!", tag="setname", font=("Berlin Sans FB",20))
    type_name = Entry(w, font=("Berlin Sans FB",20), fg="slate gray")
    type_name.pack()
    type_name.place(x=250, y=400, width=300)
    entryVar = StringVar("")
    global character_name
    character_name = entryVar.get()
    button.pack()
    type_name.grid_forget()
    #button = Button(w, image=button_next, tag="button2")
    button.place(x=570, y=430, width=150)
    button.bind('<Button-1>', onObjectClick)
    
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
        c = Canvas(root1, width=800, height=600)

        text = Text(root1)
        def exit():
            root1.destroy()
        text.insert(INSERT," Hello! So your thinking of getting a lift to school? \n \n While driving can be fast and comfotable it has some disadvantages. ")
        text.insert(INSERT,"Driving is \n very bad for the enviromnet as it produces harmful CO2 gasses.\n Rather than driving consider taking the bus?")
        text.insert(INSERT,"Taking the bus produces 6-8 times \n less CO2. \n \n If you still want to travel by car why not consider car sharing?")
        text.insert(INSERT," This reduces \n the amount of cars on the road and is also better for the environment.")
        text.insert(INSERT," \n \n When traveling by car do your best not to distract the driver and always wear \n your seatbelt to keep yourself safe.")
        text.insert(END,"\n \n Try to reduce the amout you travel by car to help protect the environment.")
        text.config(font=("Berlin Sans FB",15), fg="slate gray")
        text.pack()
        
        button = Button(root1, text = "Back to Game",command = exit )
        button.pack()
        root1.mainloop()

    def cycleInfo ():
        root1 = Tk ()
        c = Canvas(root1, width=800, height=600)
        text = Text(root1)
        def exit():
            root1.destroy()
        button = Button(root1,text = "Back to Game",command = exit )
        text.insert (INSERT, " Hello! So you'd like to cycle to school? \n \n Cycling is a great way to get around quickly while not harming the environment")
        text.insert (INSERT, "\n and keeping yourself hit and healthy. \n \n However make sure you are confortable with the cycling route before you set \n off.")
        text.insert (END, " \n \n It is also best to avoid major roads and remember to ALWAYS wear a helmet!")
        text.config(font=("Berlin Sans FB",15), fg="slate gray")
        text.place(x=400,y=300)
        text.pack()
        button.pack()
        root1.mainloop()

    def walkInfo():
        root1 = Tk()
        c = Canvas(root1, width=800, height=600)
        text = Text(root1)
        def exit():
            root1.destroy()
        button = Button(root1,text = "Back to Game",command = exit )
        text.insert(INSERT, " Hello! So your thinking of walking to school? \n did you know that walking to School is not only super good for the environment \n as it removes cars from the road. \n \n It is also great for your health and fitness.")
        text.insert(INSERT, "\n However you have to make sure to stay safe when walking in order to keep safe \n from traffic.")
        text.insert(END, "\n Choose walking to protect the environment and to keep yourself fit and healthy")
        text.config(font=("Berlin Sans FB",15), fg="slate gray")
        text.pack()
        button.pack()
        root1.mainloop()
        
    
    
    

    canvas.create_text(c_width/2, 150, text = "How would you like to get to school?", tag="choiceq", font = ("Berlin Sans FB",20))
    #choiceL.pack(anchor = N)

    #avatars to click on
    b1 = Button(root,command = car)
    b1.place(x=50,y=200)
    #b1.pack(side=LEFT)
    photoCAR = PhotoImage(file="car.gif", width=200, height=200)
    b1.config(image = photoCAR,compound = CENTER)

    b2 = Button(root,command = bike)
    b2.place(x=300,y=200)
    #b2.pack(side = LEFT)
    photoBIKE = PhotoImage(file="bicycle.gif", width=200, height=200)
    b2.config(image = photoBIKE,compound = CENTER)

    b3 = Button(root,command = walk)
    b3.place(x=550,y=200)
    #b3.pack(side = LEFT)
    photoWALK = PhotoImage(file="walk.gif", width=200, height=200)
    b3.config(image = photoWALK,compound = CENTER)

    bc = Button(root, text = "More info on travelling by car", command = driveInfo,font=("Berlin Sans FB",12), fg="slate gray")
    bc.place(x= 50, y=450)
    #bc.pack()
   
    bb = Button(root,text = "More info on cycling",command = cycleInfo, font=("Berlin Sans FB",12), fg="slate gray")
    bb.place(x=330, y=450)
    #bb.pack()

    bw = Button(root,text = "More info on walking",command = walkInfo,font=("Berlin Sans FB",12), fg="slate gray")
    bw.place(x=570, y=450)
    #bw.pack()

    bExit = Button(text = "Next")
    bExit.place(x=700, y=500)
    #bExit.pack(side=LEFT)



    root.title("Brake road safety-What is your choice?")

    #brake logos
    #photo1 = PhotoImage(file="brake.gif")
    #canvas.create_image(0,0, anchor = NW, image = photo1)

    #photo2 = PhotoImage(file="brake.gif")
    #canvas.create_image(800,0, anchor = NW, image = photo2)

    canvas.pack()
    root.mainloop()
loadMainPage()
#button = Button(w, image=button_next)
#button.place(x=570, y=430, width=150)

w.pack()
    
#w.create_window(window=type_name, x=1,y=1)
#w.update()
mainloop()
#w.update()
#label.pack()
#label.place(x=150, y=180)
#type_name.grid(row=600, column=300)
button = Button(w,font=("Berlin Sans FB",20), fg="slate gray")

root.mainloop()

