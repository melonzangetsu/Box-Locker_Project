''' Box Locker '''
from Tkinter import *
from time import *
import sys
from time import *

<<<<<<< HEAD
class Frame(object):
    def __init__(self):               
        self.root = Tk()
        self.root.geometry("800x630")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.title("Box Locker")
        self.photo = PhotoImage(file = "logo.gif")
        self.label = Label(image = self.photo)
        self.label.image = self.photo # keep a reference!
        self.label.place(x = 350, y = 5)
        Label(self.root, text=strftime('Today : %A %d %B %Y')).place(x = 100, y = 55)

        day = IntVar()
        month = IntVar()
        year = IntVar()
        
        def onClick_Increaseday(event=None):
                day.set(day.get() + 1)

        def onClick_Decreaseday(event=None):
            if day.get() > 0:
                day.set(day.get() - 1)

        def onClick_Increasemonth(event=None):
                month.set(month.get() + 1)

        def onClick_Decreasemonth(event=None):
            if month.get() > 0:
                month.set(month.get() - 1)

        def onClick_Increaseyear(event=None):
                year.set(year.get() + 1)

        def onClick_Decreaseyear(event=None):
            if year.get() > 0:
                year.set(year.get() - 1)

        Label(self.root, textvariable=day).place(x = 475, y = 55)
        Label(self.root, textvariable=month).place(x = 525, y = 55)
        Label(self.root, textvariable=year).place(x = 570, y = 55)
        Button(self.root, text="v", command=onClick_Decreaseday, fg="yellow", bg = "black").place(x = 500, y = 65, width = 12, height = 12)
        Button(self.root, text="^", command=onClick_Increaseday, fg="yellow", bg = "black").place(x = 500, y = 54, width = 12, height = 12)
        Button(self.root, text="v", command=onClick_Decreasemonth, fg="yellow", bg = "black").place(x = 550, y = 65, width = 12, height = 12)
        Button(self.root, text="^", command=onClick_Increasemonth, fg="yellow", bg = "black").place(x = 550, y = 54, width = 12, height = 12)
        Button(self.root, text="v", command=onClick_Decreaseyear, fg="yellow", bg = "black").place(x = 600, y = 65, width = 12, height = 12)
        Button(self.root, text="^", command=onClick_Increaseyear, fg="yellow", bg = "black").place(x = 600, y = 54, width = 12, height = 12)

        block = 1
        right = 0
        down = 65
        for i in xrange(6):
            down += 80
            right = 0
            for j in xrange(10):
                Button(self.root, text = block).place(x = right, y = down, width = 80, height = 80)
                right += 80
                block += 1

        self.root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
=======
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
Label(root, text=strftime('Today : %A %d %B %Y')).place(x = 100, y = 55)
Label(root, text=strftime("Setting Time : ")).place(x = 390, y = 55)

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = strftime("Now time : %H : %M : %S")
    # Update the timeText Label box with the current time
    time.config(text=current)
    # Call the update_timeText() function after 1 second
    root.after(1000, update_timeText)
# Create a timeText Label (a text box)
time = Label(root)
time.pack(anchor=W, pady=90, padx=100)
update_timeText()

#------------------------------------------------------------------------------------------------------#
''' Button Skip '''
day = IntVar()
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
Button(root, text="v", command=onClick_Decreaseday, fg="yellow", bg = "black").place(x = 500, y = 65, width = 12, height = 12)
Button(root, text="^", command=onClick_Increaseday, fg="yellow", bg = "black").place(x = 500, y = 54, width = 12, height = 12)
Button(root, text="v", command=onClick_Decreasemonth, fg="yellow", bg = "black").place(x = 550, y = 65, width = 12, height = 12)
Button(root, text="^", command=onClick_Increasemonth, fg="yellow", bg = "black").place(x = 550, y = 54, width = 12, height = 12)
Button(root, text="v", command=onClick_Decreaseyear, fg="yellow", bg = "black").place(x = 600, y = 65, width = 12, height = 12)
Button(root, text="^", command=onClick_Increaseyear, fg="yellow", bg = "black").place(x = 600, y = 54, width = 12, height = 12)

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
>>>>>>> 5d10c3d10ef7e42233fb9743b9b7cc952fb44c7a
