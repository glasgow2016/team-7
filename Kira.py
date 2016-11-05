from Tkinter import *

root = Tk()
root.geometry("800x600")
background_image = PhotoImage(file='background.gif')
background_label = Label(image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#frame1 = Frame(root, width=800, height=600)
#theLabel = Label(root, text="Name")
#theLabel2 = Label(root, text="Password")
#entry_1 = Entry(root)
#entry_2 = Entry(root)
#theLabel.grid(row=0, sticky=E)
#theLabel2.grid(row=1, sticky=E)
#entry_1.grid(row=0,column=1)
#entry_2.grid(row=1,column=1)
#frame1.pack()
root.resizable(width=False, height=False)
#root.geometry('{}x{}'.format((800,600))

#topFrame = Frame(root)
#topFrame.pack()
#buttomFrame = Frame(root)
#buttomFrame.pack()

#button1 = Button(topFrame, text="Button 1", fg="red")
#button2 = Button(topFrame, text="Button 2", fg="green")

#button1.pack(side=LEFT)
#button2.pack(side=RIGHT)
# on default pack() stack them vertically,
# else put parameters in
root.mainloop()
# continuously display the window

