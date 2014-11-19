''' Box Locker '''
from Tkinter import *
import sys

root = Tk()
root.geometry("800x630")
root.resizable(width=FALSE, height=FALSE)
root.title("Box Locker")
#------------------------------------------------------------------------------------------------------#
''' Zone LOGO PROGRAM '''
photo = PhotoImage(file = "logo.gif")
label = Label(image = photo)
label.image = photo # keep a reference!
label.place(x = 350, y = 5)


#------------------------------------------------------------------------------------------------------#
''' Zone Menu '''




#------------------------------------------------------------------------------------------------------#
''' Button Skip '''
counter = IntVar()
def onClick_Increase(event=None):
    counter.set(counter.get() + 1)

def onClick_Decrease(event=None):
    if counter.get() >= 1:
        counter.set(counter.get() - 1)

Label(root, textvariable=counter).place(x = 645, y = 55)
Button(root, text="<- ", command=onClick_Decrease, fg="red", bg = "black").place(x = 625, y = 80)
Button(root, text=" ->", command=onClick_Increase, fg="red", bg = "black").place(x = 650, y = 80)

#------------------------------------------------------------------------------------------------------#
''' Zone Blocks '''
block = 1
right = 0
down = 65
for i in xrange(6):
    down += 80
    right = 0
    for j in xrange(10):
        Button(root, text = block).place(x = right, y = down, width = 80, height = 80)
        right += 80
        block += 1
#------------------------------------------------------------------------------------------------------#
root.mainloop()
