#using icon and images and existv buttons
# from tkinter import *
# root = Tk()
# root.title("tkinter course")







# root.mainloop()

#importing tkinter module

from tkinter import *
from tkinter .ttk import *

from PIL import ImageTk,Image
#we install with using pip ins
#creating master Tkinter module

master = Tk()
#creating object of photo image class
#image should be in the same folder
#in which script is saved
mage = PhotoImage(file = "/lndex.png")
#setting icon of master window
master.iconphoto(False,mage)

#creating button
a = Button(master,text = "click me")
a.pack(side = TOP)

#infinte loop can be terminated
#keyboard or mouse can be interruped
#or by predefined functio
mainloop()