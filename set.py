# # num = (1,2,3,4,5,6,7,8,9,10)
# # nums = [1,2,3,4,5,6,7,8,9,10]

# # yes = frozenset(nums)
# # print(yes)
# # yes.append[90]
# # print(yes)




# # ashpot = {"gender":"male","name":"joy","age":67

# # }
# # # uo = frozenset(ashpot)
# # # print(ashpot)

# # okl = (ashpot.values(),frozenset())
# # print(okl)

# # your = {"mango","apple","udara"}
# # print(your[4])
# tr = {1,2,3,4}
# ca = {8,7,1,2,4}
# pa = {5,10,11,12}

# # print(tr.union(ca))
# # print(tr.union(pa))

# # # print(tr.intersection(ca,pa))
# # print(pa.difference(ca))
# print(tr.symmetric_difference(ca))

#note on set
#in python frozensetia the same as set expect expect the frozen set are immutable,
#which means that the element fron the frozenset cannot be added or removed once created,
#this function takes input as an iterable object and coverts them into immutable object'
#the order of the elements is not guareentedto be preserved


#python program to understand frozenset()function in python
#tuples and lists of numbers



# tuple = (1,2,3,4,5,6,7,8,9)
# lists = [1,2,3,4,5,6,7,8,9]

# #coverting tuples and lists to frozenset
# ftu = frozenset(tuple)
# flis = frozenset(lists)

# # printing details
# print("frozenset object is :",ftu)
# print("frozenset object :",flis)

#python program to understand the use of frozenset function


# #creating a dictionary

# from typing import FrozenSet


# course_mate = {"Name":"victor" ,"Age": 65,"Sex":"male", "College":"uturu",}
# #making keys of dictionary as a frozenset
# mate = frozenset(course_mate)

# #printing keys details
# print ("The frozenset is",mate)
# print(course_mate)

#sets
# sets are used to store multiple item in a variable.
#set is one of 4 built in data types in python used to store collections of data,
#the other 3 are: list,tuple and dictionary,all with different qualities and usages
#a set is a collection which is unordered, unchangeable, and unindexed

# aset = {"cashew","orange","apple"}
# print(aset)
#set items
#set items are unordered ,unchangeable,and do not allow duplicate values,
#unordere meansthat the item in a set do not have defined order
#set items can appear can appear in a diffferent order anytime you use them,
#and cannot be referred to by index or key
#unchangeable means that itemscammot be changed after the set has been created
# aset = {"cashew","orange","apple"}
# print(aset)
#the set constructor
#it is also also possible to use the set() constuctor to make set
# aset = (("apple","orange","guava","cherry"))
# print(aset)
# a = set(("apple","banana","orange"))
# a2 = set("apple")
# print(a)
# print(a2)

# sets = {"man","man","woman"}
# length = len(sets)
# print(sets)
# print(length)



# lists = list(("man","man","woman"))
# # print(type(lists))
# dics = dict({"man":"human","woman":"femalebeing"})
# print(type(dics))
# name = {"amaka","victor"}
# lists = ({"man","man","woman"})
# lists.append("promise")
# print(lists)
# b = set(lists)
# print(b)
# print(type(b))

# sets = {"man","woman","girl"}
#print(type(sets))
#lists = ("man","man","woman")
# b = frozenset(lists)
# print(lists)

# A = {1,2,3,4}
# B = {2,4,5,6}
# C = {7,8,9,10}


# # print(tr.union(ca))
# # print(tr.union(pa))

# # # print(tr.intersection(ca,pa))
# # print(pa.difference(ca))
# print(tr.symmetric_difference(ca))




# frozenset
# initilaize A and B
# A  = fozenset([1,2,3,4])
# B = frozenset([4,2,5,7,])
# copying A frozenset
#c = A.copy()#output:frozenset({1,2,3,4})
#print(c)
#assignment

Animals = {"dog","elephant","rabbit","goat"}
for A in Animals:
    print(A)
Animals.add("cow")
print("Animals include:", Animals)

Animals .remove("elephant")
print("Animals include all expect the one i removed:", Animals)