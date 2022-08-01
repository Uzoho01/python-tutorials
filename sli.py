from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

master = Tk()
master.title("learn to create slider")
mage = PhotoImage(file = "ring.png")
master.iconphoto(False,mage)
# we can define how big we want our original window to be
master.geometry("400x400")

#how to creat a slider
# we will use the scale widget

vertical = Scale(master,from_=0,to=200)
vertical.pack()
horizontal = Scale(master,from_=0,to=200,orient=HORIZONTAL,command=slide)
horizontal.pack()
my_label = Label(master,text=horizontal.get()).pack()
def slide():
    my_label = Label(master,text=horizontal.get()).pack()
    master.geometry(str(horizontal.get()) + "400x400")
button = Button(master,text="click me!",command=slide).pack()


master.mainloop()