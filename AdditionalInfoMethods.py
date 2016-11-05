from Tkinter import *

def walkInfo():
    root = Tk()
    text = Text(root)
    def exit():
        root.destroy()
    button = Button(text = "Back to Game",command = exit )
    text.insert(INSERT, " Hello! So your thinking of walking to school? \n did you know that walking to School is not only super good for the environment \n as it removes cars from the road. \n \n It is also great for your health and fitness.")
    text.insert(INSERT, "\n However you have to make sure to stay safe when walking in order to keep safe \n from traffic.")
    text.insert(END, "\n Choose walking to protect the environment and to keep yourself fit and healthy")
    text.pack()
    button.pack()
    root.mainloop()


walkInfo()


def driveInfo ():
    root= Tk ()
    text = Text(root)
    def exit():
        root.destroy()
    button = Button(text = "Back to Game",command = exit )
    text.insert(INSERT," Hello! So your thinking of driving to school? \n \n While driving can be fast and comfotable it has some disadvantages. ")
    text.insert(INSERT,"Driving is \n very bad for the enviromnet as it produces harmful CO2 gasses.\n Rather than driving consider taking the bus?")
    text.insert(INSERT,"Taking the bus produces 6-8 times \n less CO2. \n \n If you still want to travel by car why not consider car sharing?")
    text.insert(INSERT," This reduces \n the amount of cars on the road and is also better for the environment.")
    text.insert(INSERT," \n \n When traveling by car do your best not to distract the driver and always wear \n your seatbelt to keep yourself safe.")
    text.insert(END,"\n \n Try to reduce the amout you travel by car to help protect the environment.")
    text.pack()
    button.pack()
    root.mainloop()

driveInfo ()


def CycleInfo ():
    root = Tk ()
    text = Text(root)

    def exit():
        root.destroy()
    button = Button(text = "Back to Game",command = exit )
    text.insert (INSERT, " Hello! so you'd like to cycle to school? \n \n Cycleing is a great way to get around quickly while not harming the environment")
    text.insert (INSERT, "\n and keeping yourself hit and healthy. \n \n However make sure you are confortable with the cycleing route before you set \n off.")
    text.insert (END, " \n \n It is also best to avoid major roads and remember to ALWAYS wear a helmet!")
    text.pack()
    button.pack()
    root.mainloop()
    

CycleInfo()









