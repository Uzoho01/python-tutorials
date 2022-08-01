from tkinter import *
# r = tk.Tk()
# r.title("timer")
# button = tk.Button(r,text = "stop",width = 25 ,command = r.destroy)
# button.pack()
# r.mainloop()

#first import tkinter to import everythim]ng u use ur * 




# #in tkinter everthing is a widget
# #first create a root window
# #fist thing u have to do
root = Tk()
# #we are creating a simple window and run it 
#we are using mylabel widget
# to create anything in tkinter is a two steps things firstly:define the thing u created 
# secondly :put what we created on a screen
# we created a label 
#since python is an object oriented program it can be done like these
# mylabe1 = Label(root,text = "Hello World!!!").grid(row=0,column=0)
# mylabe2 = Label(root,text = "Firstname:").grid(row=1,column=0)
# mylabe3 = Label(root,text = "lastname:").grid(row=2,column=0)
# mylabe4 = Label(root,text = "Date of birth:").grid(row=3,column=0)
# mylabe5 = Label(root,text = "year of study:").grid(row=4,column=0)
#using pack to shovel the text into the screen it will be the size it is
# mylabe1.grid(row=0,column=0)
# mylabe2.grid(row=1,column=0)
# mylabe3.grid(row=2,column=0)
# mylabe4.grid(row=3,column=0)
# mylabe5.grid(row=4,column=0)
# mylabe1.pack()
# create an event loop that is continous looping 
# root.mainloop()
#the x button stop the loop and automatically destroys the loops and close it
#postioning with tkinters Grid system
#grids have colums up and down rowsleft and right
#we deal with the grid system using numbers
# #creating buttons
# #these is called entey widget
#creating an  with entry widget
root.title("simple calculator")
#entry serves as an input
a = Entry(root,width=35,borderwidth=5)
a.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# a.insert(1,"Enter Your Firstname :")
# mybutton = Button(root,text="save me", state = "disabled").if u dont want urtext to click use yhe disabled
# def mySave():
#     hello = "Hello "  + a.get()
#     mylabel =Label(root,text = hello  )
#     mylabel.pack()
    #fff is white colour 0000 is balck clour
def button_click(number):
    # a.delete(0,END)to make it print more than one 
    current = a.get()
    a.delete(0,END)
    a.insert(0,str(current) + str(number))

def button_clear():
    a.delete(0,END)

def button_addition():
    first_number = a.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    a.delete(0,END)
    
def button_equal():
    second_number = a.get()
    a.delete(0,END)

    if math == "addition":
       a.insert(0,f_num + int(second_number))
    if math == "division":
       a.insert(0,f_num / int(second_number))
    if math == "multiplication":
       a.insert(0,f_num * int(second_number))
    if math == "subtraction":
       a.insert(0,f_num - int(second_number))
  

def button_division():
    first_number = a.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    a.delete(0,END)


    

def button_multiplication():
    first_number = a.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    a.delete(0,END)
    
    

def button_subtraction():
    first_number = a.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    a.delete(0,END)
    
    





#define button
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=90,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=90,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=90,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_addition =Button(root,text="+",padx=40,pady=20,command=button_addition)
button_equal =Button(root,text=  " =",padx=91,pady=20,command= button_equal)
button_clear =Button(root,text= "c",padx=90,pady=20,command=button_clear)
button_division = Button(root,text= "/",padx=40,pady=20,command=button_division)
button_multiplication = Button(root,text= "*",padx=40,pady=20,command=button_multiplication)
button_subtraction = Button(root,text="-",padx=40,pady=20,command =button_subtraction)

#put buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2,columnspan=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2,columnspan=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2,columnspan=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=5,column=2,columnspan=2)
button_addition.grid(row=4,column=1)
button_equal.grid(row=4,column=2,columnspan=2)
button_division.grid(row=5,column=0)
button_multiplication.grid(row=5,column=1)
button_subtraction.grid(row=6,column=0)

# mybutton = Button(root,text="Enter your username",command = mySave,fg="yellow",bg = "green")

# root.mainloop()
# #build a simple calculator program
# root = Tk()
# root.title("simple calculator")


a = Entry(root,width = 35, borderwidth= 5)
a.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_Add():
    hello = "Hello" +a.get()
    mylabel = Label(root,text = hello)
    mylabel.pack()


button_1 = Button(root,text="0",padx=40,pady=20,command=button_Add)

root.mainloop()


