''' Box Locker '''
from Tkinter import *
import sys
from time import *

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
Label(root, text=strftime('Today is %A %d %B %Y')).place(x = 100, y = 55)
Label(root, text=strftime('You open program at %H:%M')).place(x = 100, y = 75)
Label(root, text=strftime("Setting Time : ")).place(x = 390, y = 55)

#------------------------------------------------------------------------------------------------------#
''' Button Skip '''
#counter = IntVar()
#def onClick_Increase(event=None):
#    counter.set(counter.get() + 1)
#def onClick_Decrease(event=None):
#    if counter.get() >= 1:
#        counter.set(counter.get() - 1)

day = IntVar()
print type(day)
def onClick_Increaseday(event=None):
        day.set(day.get() + 1)

def onClick_Decreaseday(event=None):
    if day.get() > 1:
        day.set(day.get() - 1)

month = IntVar()
def onClick_Increasemonth(event=None):
        month.set(month.get() + 1)

def onClick_Decreasemonth(event=None):
    if month.get() > 1:
        month.set(month.get() - 1)

year = IntVar()
def onClick_Increaseyear(event=None):
        year.set(year.get() + 1)

def onClick_Decreaseyear(event=None):
        year.set(year.get() - 1)

Label(root, textvariable=day).place(x = 475, y = 55)
Label(root, textvariable=month).place(x = 525, y = 55)
Label(root, textvariable=year).place(x = 570, y = 55)
#Label(root, text=month).place(x = 30, y = 55)
#Label(root, text=year).place(x = 430, y = 55)
#Label(root, textvariable=counter).place(x = 645, y = 55)
#Button(root, text="<- ", command=onClick_Decrease, fg="red", bg = "black").place(x = 625, y = 80)
#Button(root, text=" ->", command=onClick_Increase, fg="red", bg = "black").place(x = 650, y = 80)
Button(root, text="v", command=onClick_Decreaseday).place(x = 500, y = 65, width = 13, height = 13)
Button(root, text="^", command=onClick_Increaseday).place(x = 500, y = 55, width = 13, height = 13)
Button(root, text="v", command=onClick_Decreasemonth).place(x = 550, y = 65, width = 13, height = 13)
Button(root, text="^", command=onClick_Increasemonth).place(x = 550, y = 55, width = 13, height = 13)
Button(root, text="v", command=onClick_Decreaseyear).place(x = 600, y = 65, width = 13, height = 13)
Button(root, text="^", command=onClick_Increaseyear).place(x = 600, y = 55, width = 13, height = 13)

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
