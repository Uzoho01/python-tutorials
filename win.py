#creating a new window
from tkinter import *
from PIL import ImageTk,Image


master = Tk()
master.title("learn to create icons")
mage = PhotoImage(file = "ring.png")
master.iconphoto(False,mage)
#how to control what pop up on your screen
button =Button(master,text="open second window",command=open)
#start by defining top
def open():
    global my_img
    top = Toplevel()
    top.title("my second window")
    mage = PhotoImage(file = "ring.png")
    top.iconphoto(False,mage)
#label =Label(top,text="Hello world").pack()
    my_img = ImageTk.PhotoImage(Image.open("pictures/index.png"))
    my_label = Label(top,image=my_img).pack()

#how to control what pop up on your screen
    
    button = Button(master,text="close window",command=top.destroy).pack()
#why the image didnt load is because it is 
#a local variable we need to create a global variable
#python since it as garbage
button2 =Button(master,text="open second window",command=open).pack
mainloop()