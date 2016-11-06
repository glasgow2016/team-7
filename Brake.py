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
        w.delete("setname")
        w.delete("name")
        w.delete("button2")
    
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

