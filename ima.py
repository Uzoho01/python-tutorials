from tkinter import *

#to import pillow
#we install with using pip install

from PIL import ImageTk,Image

#created my window
master = Tk()

#created my title
master.title("learn to create icons")
#location of the
mage = PhotoImage(file = "ring.png")

master.iconphoto(False,mage)
#we are creating an variable called my image
#then accesed the libary called imageTk and accesed the photoIMage from inside image
#then opened the image .we defined the image 
#we put the image inside somethind else
#we define the somethindg else
#creating image viewer app


my_img1 = ImageTk.PhotoImage(Image.open("pictures/index.png"))
my_img2 = ImageTk.PhotoImage(Image.open("pictures/pics.png"))
my_img3 = ImageTk.PhotoImage(Image.open("pictures/ring.png"))
image_list= [my_img1,my_img2,my_img3]

#adding status bar
status = Label(master,text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
#what he did was to create a new files and copied all those file
#anchor is used to put the  staus bar  in the direction of your choice



#creating a widget
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

#creating the functionality of each button
def forward(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num -1])
    # button_forward = Button(master,text=">>",command=lambad:forward())
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward = Button(master,text=">>",command=lambda:forward(image_num+1))
    button_back = Button(master,text="<<",command= lambda:back(image_num-1))
    if image_num ==3:
        button_forward =Button(master,text=">>",state=DISABLED)
    button_back.grid(row=1,column=0)
    button_forward =Button(master,text=">>",command=lambda:forward(2))
    status = Label(master,text="Image " + str(image_num)   + "of"  + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
      

def back(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    # button_forward = Button(master,text=">>",command=lambad:forward())
    button_forward = Button(master,text=">>",command=lambda:forward(image_num+1))
    button_back = Button(master,text="<<",command= lambda:back(image_num-1))
    if image_num ==1:
       button_back =Button(master,text=">>",state=DISABLED)
    button_back.grid(row=1,column=0)
    button_forward =Button(master,text=">>",command=lambda:forward(2))
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward =Button(master,text=">>",command=lambda:forward(2))
    #update stautus bar
    status = Label(master,text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
#creating buttons
button_back =Button(master,text="<<",command=back)
button_exist =Button(master,text="EXIST PROGRAM",command=master.quit)
button_forward =Button(master,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exist.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
#sticky is use as a navigational system,it is used to strech in any direction

#using images
#piilow is used to importing image libaries




#creating an exist  button
button_exist = Button(master,text= "Exit program",command=master.quit)
# button_exist.pack()



master.mainloop()






# from tkinter import *
# from PIL import ImageTk,image

# master = Tk()
# master.title("creating icons ,images and exist button")
# mage = PhotoImage(file = "ring.png")
# master.iconphoto(False,mage)

# my_img = ImageTk.PhotoImage(Image.)

# button_exist = Button(master,text= "Exit program",command=master.quit)
# button_exist.pack()
# master.mainloop()
