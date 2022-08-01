#adding frames to your program
from tkinter import *


from PIL import ImageTk,Image

master = Tk()
master.title("learn to create icons")
mage = PhotoImage(file = "ring.png")
master.iconphoto(False,mage)
#created a widget here
frame = LabelFrame(master,text="This is my frame...",padx=50,pady=50)
#put it on the screen
frame.pack(padx=10,pady=10)
#creating a button widget
button = Button(frame,text="dont click here!..")
button2=Button(frame,text="or here.....")
button.grid(row=0,column=0)
button2.grid(row=1,column=1)

master.mainloop()



