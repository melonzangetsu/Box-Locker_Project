''' Box Locker '''
import Tkinter
import sys

root = Tkinter.Tk()
root.geometry("800x600")
root.title("Box Locker")

counter = Tkinter.IntVar()

def onClick_Increase(event=None):
    counter.set(counter.get() + 1)

def onClick_Decrease(event=None):
    counter.set(counter.get() - 1)

Tkinter.Label(root, textvariable=counter).pack()
Tkinter.Button(root, text="Increase", command=onClick_Increase, fg="dark green", bg = "white").pack()
Tkinter.Button(root, text="Decrease", command=onClick_Decrease, fg="dark green", bg = "white").pack()

    



root.mainloop()
