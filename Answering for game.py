from Tkinter import *

master = Tk()



def Button1B():
    
    def Button4B():
        label.config(text = "Wrong!")
        label.pack()

    def Button5B():
        label.config(text = "Correct!")
        label.pack()

    root = Tk()

    b4 = Button(root, text="Left", command=Button4B)

    b4.grid(row=0, column = 0)

    b4 = Button(root, text="Right", command=Button5B)

    b4.grid(row=0, column = 1)

    label = Label(root)
   
    root.mainloop()


    

b1 = Button(master, text="which way should you look \n first when crossing the road?", command=Button1B)
b1.config(height = 5, width = 30)
b1.grid(row=0, column = 0)









mainloop()
