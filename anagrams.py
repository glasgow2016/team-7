from Tkinter import *

def anagram():

    master = Tk()
    e = Entry(master)
    e.pack()
    master.minsize(800,600)
    e.focus_set()

    

    anagram = "road safety"
    anagramMix = "doar sfyeta"
    flag = 0
    def callback():
        def exit():
            master.destroy()
        lowerInput = e.get()
        if (lowerInput.lower()) == anagram:
            print "good lad"
            choiceG = Label(text = " Good Job you won the game! ", font = "comic")
            choiceG.pack(anchor = S)
            button = Button(text = "Exit",command = exit )
        else :
            choiceG = Label(text = " Hint: Safety on roads is very important! ", font = "comic")
            choiceG.pack(anchor = S)
        button.pack()

    
 
                
    choiceL = Label(text = "\n Unjumble the words! \n \n doar sfyeta \n ", font = "comic")
    choiceL.pack(anchor = S)
         
    b = Button(master, text="solve", width=10, command=callback)
    b.pack()

    mainloop()
    e = Entry(master, width=800, height = 600)
    e.pack()

    text = e.get()



anagram()
