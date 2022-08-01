#creating message boxes
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

master = Tk()
master.title("learn to create icons")
mage = PhotoImage(file = "ring.png")
master.iconphoto(False,mage)
#types of message boxes we can create
#showinfo,#showwarning,#showerror,#askquestion,#askokcancel,#askyesorno
def popup():
    #how to deal with the buttons
#creating a variable
   view = messagebox.showerror("This is my popup","Hello world")
   Label(master,text="response").pack()
  # if response == response:
  #    Label(master,text="You clicked yes!").pack()
#   else:
    #    Label(master,text="You clicked no!").pack()


    
#message boxe is like a pop up 
Button(master,text="popup",command=popup).pack()



master.mainloop()