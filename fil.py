#how to use the dilogue box to open a file
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

master = Tk()
master.title("learn to create icons")
mage = PhotoImage(file = "ring.png")
master.iconphoto(False,mage)

master.filename = filedialog.askopenfilename(initialdir="/download/pictures/index.png")

mainloop()