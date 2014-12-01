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
        '''
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
        '''
        day = int(strftime("%d"))
        year = int(strftime("%Y"))
        month = int(strftime("%m"))
        Label(self.root, text="SKIP DAY").place(x = 475, y = 55)
        Spinbox(self.root, from_=day, to=31).place(x = 535, y = 55, width = 40)
        Spinbox(self.root, from_=year, to=3000).place(x = 615, y = 55, width = 40)
        Spinbox(self.root, from_=month, to=12).place(x = 575, y = 55, width = 40)
##        Button(self.root, text="v", command=onClick_Decreaseday, fg="yellow", bg = "black").place(x = 500, y = 65, width = 12, height = 12)
##        Button(self.root, text="^", command=onClick_Increaseday, fg="yellow", bg = "black").place(x = 500, y = 54, width = 12, height = 12)
##        Button(self.root, text="v", command=onClick_Decreasemonth, fg="yellow", bg = "black").place(x = 550, y = 65, width = 12, height = 12)
##        Button(self.root, text="^", command=onClick_Increasemonth, fg="yellow", bg = "black").place(x = 550, y = 54, width = 12, height = 12)
##        Button(self.root, text="v", command=onClick_Decreaseyear, fg="yellow", bg = "black").place(x = 600, y = 65, width = 12, height = 12)
##        Button(self.root, text="^", command=onClick_Increaseyear, fg="yellow", bg = "black").place(x = 600, y = 54, width = 12, height = 12)

        number = []
        for i in xrange(1, 61):
            number.append(str(i))
        time = localtime()    
        block = 0
        right = 0
        down = 65
        for i in xrange(6):
            box = number[block]
            down += 80
            right = 0
            for j in xrange(10):
                button_value = Button(self.root, text = block+1, command = lambda block=block : self.clickBox(block+1))
                button_value.place(x = right, y = down, width = 80, height = 80)
                right += 80
                block += 1

        self.root.mainloop()
        
    def clickBox(self, number):
        print number
        Box(number)

class Box(object):
    def __init__(self, value):
        self.box = Tk()
        self.box.geometry("400x230")
        self.box.resizable(width=FALSE, height=FALSE)
        self.box.title("Box Locker : " + str(value))
        Label(self.box, text = "Box : " + str(value)).place(x = 200, y = 35, anchor = CENTER)
        self.box.mainloop()

#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
