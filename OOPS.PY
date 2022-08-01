# # creating a class oops
# class PersonClass():
#     def persons_name(self):
#         print("anita")
#     # def person_age(self):
#     #     p = PersonClass
#     #     p.persons_name()

# p = PersonClass()
# p.persons_name()





# string ="hello"
# print (string .upper())


# class Dog:
#     def bark(self):
#         print("bark")

# d = Dog()
# d.bark()


# class DOg:
#     def __init__ (self,name):
#         self.name =name
# d = DOg ("bumba")
# print (d.name)




#another method of learning oops
#creating my class first
# class Item:
#     def calculate_total_price(self):

#second step is creating an instance of a class#remerber method are function inside a class
# item1 = Item()
#next assigning some attirbutes to the instance of a class we assign attirbutes using .
# item1.name = "phone"
# item1.name = 100
# item1.quanitity = 5
#how to creat method and execute them on our instances in our class






# class Dog:


#     #class attribute
#     attrl = "mammal"


#     #instance attribute
#     def __init__(self, name) :
#         self.name = name
        
#         #driver code
#         #object instantiation 
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
# #accessing class attributes
# #accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attrl))
# print("Tommy is also a {}".format(Tommy.__class__.attrl))

# #accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))



class Personal_details:
    attr1 = "human"
    def __init__(self,first_name,last_name,age,gender,complextion):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.complextion = complextion

Anita = Personal_details("Anita","uzoho",10,"female","fair")

print("Anita is a {}".format(Anita.__class__.attr1))
print("Her first_name is {}".format(Anita.first_name))
print("Her last_name is {}".format(Anita.last_name))
print("she is {} years old".format(Anita.age))
print("she is  {}".format(Anita.gender))
print("she is {} in complextion".format(Anita.complextion))

    
        







