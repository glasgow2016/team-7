from Tkinter import *

def walkInfo():
   
    root = Tk()
    text = Text(root)
    text.insert(INSERT, "Hello! So your thinking of walking to school? \n did you know that walking to School is not only super good for the environment \n as it removes cars from the road. \n \n It is also great for your health and fitness.")
    text.insert(INSERT, "\n However you have to make sure to stay safe when walking in order to keep safe \n from traffic.")
    text.insert(END, "\n Choose walking to protect the environment and to keep yourself fit and healthy")
    text.pack()

walkInfo()
walkInfo()


def driveInfo ():
    root= Tk ()
    text = Text(root)
    text.insert(INSERT,"Hello! So your thinkinking of driving to school? \n While driving can be fast and comfotable it has some disadvantages.")
    text.insert(END,"Driving is very bad for the enviromnet as it produces harmful CO2 gasses.\n Rather than driving consider taking the bus?")
    #text.insert(INSERT,"Taking the bus produces 6-8 times less CO2. \n \n If you still want to travel by car why not consider car sharing?")
    #text.insert(INSERT,"This reduces the amount of cars on the road and is also better for the environment."
    #text.insert(INSERT," \n \n When traveling by car do your best not to distract the driver and always wear your seatbelt to keep yourself safe.")
    text.pack()

driveInfo()

#root.mainloop()
