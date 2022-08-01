# #ceating a base
# class Base:
#     def __init__(self):
#         self.a = "Victor"
#         self._c = "Victor"


# #crearind a derived class
# class Derived(Base):
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         print("calling private member of the base class")
# obj1 = Base()
# print(obj1.a)
# # print(obj1._c)
# #python program to demonstrate protected memeber


#creating another base
class Base:
    def __init__(self):
        #proctected member
        self._a = 2
        
        #creating a derived class
class Derived(Base):
    def __init__(self):
        #calling constructor of base class
        Base.__init__(self)
        print("calling protected member",self._a)
#modify the protected variable
        self._a = 3
        print("calling the modified class",self._a)







