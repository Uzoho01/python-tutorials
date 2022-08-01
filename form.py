from tkinter import *



master = Tk()
# add vgeometry properties to give width and height
master.geometry("500x300")
def getvals():
    print("Accepted")
# heading
Label(master,text="PYTHON REGISTRATION FORM",font="arial 15 bold").grid(row=0,column=3)
# field name
name = Label(master,text="Name")
phone = Label(master,text="Phone")
gender = Label(master,text="Gender")
emergency = Label(master,text="Emergency")
paymentmood = Label(master,text="Payment Mood")
# packing field with grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

# variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar
# creating entry field
nameentry = Entry(master,textvariable=namevalue)
phoneentry = Entry(master,textvariable=phonevalue)
genderentry = Entry(master,textvariable=gendervalue)
emergencyentry = Entry(master,textvariable=emergencyvalue)
paymentmoodentry = Entry(master,textvariable=paymentmoodvalue)
# packing entry field with grid
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmoodentry.grid(row=5,column=3)
# making checkboxes
checkbut = Checkbutton(text="remember me?",variable=checkvalue)
checkbut.grid(row=6,column=3)
# creating a summit button
Button(text="Submit",command=getvals).grid(row=7,column=3)

master.mainloop()