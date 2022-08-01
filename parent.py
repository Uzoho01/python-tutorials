# # # #parent class



# # # from tkinter import Y


# # # class Person(object):

# # #  #__init __is known as the constructor
# # #  def __init__(self,name,idnumber):
# # #         self.name = name
# # #         self.idnumber = idnumber




# # #  def display(self):
# # #       print(self.name)
# # #       print(self.idnumber)


# # # # def display(self):
# # # #     print(self.name)
# # # #     print(self.idnumber)

# # # def details(self):
# # #     # print("My name is {}".format(self.name))
# # #     print(f"My name is {self.name}")
# # #     print ("idnumber:{}".format (self.idnumber))


# # #     #childclass
# # # class Employee(Person):
# # #     def __init__(self,name,idnumber,salary,post):
# # #         self.salary = salary
# # #         self.post = post

# # #     #invoking the __init__ of the parent class
# # #         Person.__init__(self,name,idnumber)


# # #     def details(self):
# # #         print("My name is {}".format(self.name))
# # #         print("idnumber:{}".format(self.idnumber))
# # #         print("post:{}".format(self.post))


# # # #creation of an object variable or an instance
# # # y = "i want to make somethindklfiitykyhkgkfifof"
# # # a = Employee("Anny",908764,300000,y)

# # # #calling a function of the class person using #its instance
# # # a.display()
# # # a.details()

# # #parent class
# # class Student:
# #     def __int__(self,teacher,subject):
# #         self.teacher = teacher
# #         self.subject = subject

# #     def show(self):
# #         print(self.teacher)
# #         print(self.subject)
    

# #     def display(self):
# #         print("My class teachers name is {}".format(self.teacher))
# #         print("I offer these subject {}".format(self.subject))
        


# # #child class
# # class One(Student):
# #     def __init__(self,teacher,subject,number):
# #         self.number = number

# #         Student.__init__(self,teacher,subject)

# #     def display(self):
# #         print("My class teachers name is {}".format(self.teacher))
# #         print("I offer these subject {}".format(self.subject))
        
# #         print("number_students:{}".format(self.number))

# # y = One("Treasure","english",76)
# # y.show()
# # y.display()


# #assignmemt
# class Student():
#     def __init__(self,teacher,subject):
#         self.teacher = teacher
#         self.subject = subject
#     def display(self):
#         print("teacher",self.teacher)
#         print("subject",self.subject)
#     def show(self):
#         print("My class teacher name is: {}".format(self.teacher))
#         print("We offer these subject: {}".format(self.subject))

# #class that have the same teacher but offer different subject
# teachers_name = "Treasure"
# class Primary1(Student):
#     def __init__(self,teacher,subject):
#         Student.__init__(self,teacher,subject)
# y = Primary1(teachers_name,"english")
# y.show()


# class Primary2(Student):
#     def __init__(self,teacher,subject):
#         Student.__init__(self,teacher,subject)
# y = Primary2(teachers_name,"mathematics")
# y.show()

# class Primary3(Student):
#     def __init__(self,teacher,subject):
#         Student.__init__(self,teacher,subject)
# y = Primary3(teachers_name,"biology")
# y.show()

# #classses that offer the same suject but different teachers
# subject_name = "Mathematics"
# class Primary3(Student):
#     def __init__(self,teacher,subject):
#         Student.__init__(self,teacher,subject)
# y = Primary3("Grace",subject_name)
# y.show()

# class Primary3(Student):
#     def __init__(self,teacher,subject):
#         Student.__init__(self,teacher,subject)
# y = Primary3("Peter",subject_name)
# y.show()






    
i = 1
while i < 20:
  print(i)
#   i +=2

# fruits = ["apple", "banana", "cherry"]
# for a in fruits:
#   if a != "cherry":
#     continue
#   print(a)  

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# for a in range(5):
#       print(a)
    

