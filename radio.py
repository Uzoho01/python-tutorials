#creating a radio button
from tkinter import*
from PIL import ImageTk,Image
master = Tk()

master.title("learn to create icons")
mage = PhotoImage(file = "ring.png")
master.iconphoto(False,mage)
#defining a twinker variable
#u = IntVar()
#u.set("2")
#second way of creating radio button
#first create a list,then tuple
PIZZA =[
    ("cheese","cheese"),
    ("beef","beef"),
    ("mushroom","mushrrom"),
    ("chicken","chickens"),
    

]
stuffing = StringVar()
stuffing.set("cheese")
#loop through all these things and put them on the screen
for text, pizza in PIZZA:
    Radiobutton(master,text=text,variable=stuffing,value=pizza).pack(anchor=W)
#creating a function 
def creating(value):
    mylabel =Label(master,text=value)
    mylabel.pack()

#creating a radio button
#assigning a variablle to the button so that when u click on the button the
#variable assigned to it will work.
#Radiobutton(master,text="Option 1",variable=u,value=1,command=lambda:creating(u.get())).pack()
#Radiobutton(master,text="Option 2",variable=u,value=2,command=lambda:creating(u.get())).pack()

#creating a quick label
#mylabel =Label(master,text=stuffing.get())
#mylabel.pack()
mybutton=Button(master,text="click me !",command=lambda:creating(stuffing.get()))
mybutton.pack()
master.mainloop()