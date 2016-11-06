from Tkinter import * 

clicks = [0,0]
textList = ['sagsdfgsdfs','dfgsdgsdfg','sdfgdsfgsdfg','dsfg','sdfgsdfg','sdfg']
coordinates = [0,]*4

def onCanvasClick1(event):
    print 'Got canvas click', event.x, event.y, event.widget

clickCounter = 0


def onObjectClick(event):
    global clickCounter
    #line = canv.create_line (event.x, event.y,
    print 'Got object click', event.x, event.y, event.widget
    print event.widget.find_closest(event.x, event.y)
    #create a list of x and y co-ordinates for 1 click then add to list of clicks
    print clickCounter

    lineBoolean = False
    lineBoolean1 = False

    
    if clickCounter == 0:
        coordinates[clickCounter] = event.x
        coordinates[(clickCounter+1)] = event.y
        clicks[0] = coordinates
    if event.widget.find_closest(event.x, event.y) == (7,):
            lineBoolean1 = True

    print lineBoolean1        
    if clickCounter == 1:
        coordinates[clickCounter+2] = event.x
        coordinates[(clickCounter+1)] = event.y
        clicks[1] = coordinates
        if event.widget.find_closest(event.x, event.y) == (10,) and lineBoolean1 ==True:
            lineBoolean = True
        else:
            lineBoolean=False
    
    clickCounter = clickCounter +1
    print lineBoolean
    return lineBoolean
    

           
root = Tk()
    
canv = Canvas(root, width=1000, height=1000)
o1 = canv.create_oval(20, 20, 120, 100)
o2 = canv.create_oval(20, 110, 120, 190)
o3 = canv.create_oval(20, 200, 120, 280)
o4 = canv.create_oval(320, 20, 420, 100)
o5 = canv.create_oval(320, 110, 420, 190)
o6 = canv.create_oval(320, 200, 420, 280)

counter =0
x = 70
y = 55


while counter <3:
 
    textList[counter] = canv.create_text(x, y, text = textList[counter])
    y = y + 90
    counter = counter + 1
 
x = 370
y = 55

while counter <6:
    print counter
    textList[counter] = canv.create_text(x, y, text = textList[counter])
    y = y + 90
    counter = counter +1
print clickCounter

for i in range(6):   
    global clickCounter
    if clickCounter <6: 
        canv.tag_bind(textList[i], '<Button-1>', onObjectClick)
        

      #canv.bind('Button-1', onCanvasClick1)                
    #canv.tag_bind(o1, '<Double-1>', onObjectClick)      
    #canv.tag_bind(o2, '<Double-1>', onObjectClick)
    #canv.tag_bind(o3, '<Double-1>', onObjectClick)
    #canv.bind('<Double-1>', onCanvasClick2)                    
    #canv.tag_bind(o4, '<Double-1>', onObjectClick)
    #canv.tag_bind(o5, '<Double-1>', onObjectClick)      
    #canv.tag_bind(o6, '<Double-1>', onObjectClick)

print onObjectClick
if onObjectClick == True:
    line = canv.create_line(10,10,200,200)



canv.pack()
root.mainloop()




















