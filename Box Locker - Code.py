''' Box Locker '''
from Tkinter import *
from time import *
import sys

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
        
    def box1(self):
        Box1()

    def box2(self):
        Box1()

    def box3(self):
        Box1()

    def box4(self):
        Box1()

    def box5(self):
        Box1()

    def box6(self):
        Box1()

class Box1(object):
    def __init__(self):
        self.box = Tk()
        self.box.geometry("400x230")
        self.box.resizable(width=FALSE, height=FALSE)
        self.box.title("Box Locker")

#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
