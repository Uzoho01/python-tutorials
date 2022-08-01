# # employee = {"name":"anita","age":43,"company":"ashpot", 'list': ["Apple", 1]}
# # # print(employee)
# # print(employee.get("age"))

# words = { "man":"a man is a male human being",
# "woman":"a woman can be said to be a female woman being",
# "animal":"animals are not human"
# }

# # meaning = input("please search here:\n")
# # if meaning == "man":
# #     print(words.get("man"))
# # elif meaning == "woman":
# #     print(words.get("woman"))
# # elif "animal" in meaning:
# #     print(words.get("animal"))

# # # print(words.keys())

# # # python program to demostrate working
# # #of a dictionarycopy
# # dic = {1: "chealsea",2:"Machester",3:"Arsenal"}
# # print("original:",dic)
# # #accessing value for key
# # print(dic.get(1))
# # #accessing keys for the dictionary
# # print(dic.keys())
# # #accessing keys for the dictionary
# # print(dic.values())
# # #popping keys for the dictionary
# # print(dic.pop())
# #printing all the items of the dictionary
# print(dic.items())




#assignment
words = {"Vital":"performing an essential function in the living body",
"Create":"to bring something into existence",
"Creamy":"containing a lot of cream",
"Gorgeous":"very attractive",
"Anita":"A herbew name meaning Grace and Favour",
"Victor":"A latin name meaning winner or conqueror",
"Personality":"Qualities that form an individual distinctive character",
"Similar":"Having resemblance in apperance",
"Name":"A word or set of words by which a person or thing is known or addresed to",
"Black":"co;our owing to the absence of light",
"Python":"A large snake that kills animals it eats by wrapping itself around them",
"Dream":"A series of thought and sensation occuring in a person mind during sleep",
"Learning":"The acquisition of skills through study or being taught",
"Github":"A web_based hosting service for software development project",
"Nature":"A basic qualities of something",
"Basic":"Forming an essential foundation or starting point",
"Essential":"Absolutely necessary ",
"Medicine":"Practice of the treatment aand prevention of disease",
"Disease":"A disorder of function in a human ,animal, or plant",
"Numbers":"An arithmetic value,expressed by a word ,symbol,or figure"

}
meaning = input("please search here/n:")
if "Vital" in meaning or "value".capitalize() or "value".upper():
    print(words.get("Vital"))
elif "Create" == meaning:
    print(words.get("Create"))
elif "Creamy" == meaning:
    print(words.get("Creamy"))
elif "Gorgeous" == meaning:
    print(words.get("Gorgeous"))
elif "Anita" == meaning:
    print(words.get("Anita"))
elif "Victor" == meaning:
    print(words.get("Victor"))
elif "Personality" == meaning:
    print(words.get("Personality"))
elif "Similar" == meaning:
    print(words.get("Similar"))
elif "Name" == meaning:
    print(words.get("Name")) 
elif "Black" == meaning:
    print(words.get("Black"))  
elif "Python" == meaning:
    print(words.get("Python"))
elif "Dream" == meaning:
     print(words.get("Dream"))
elif "Learning" == meaning:
    print(words.get("Learning"))
elif "Github" == meaning:
    print(words.get("Github"))
elif "Nature" == meaning:
    print(words.get("Nature"))
elif "Basic" == meaning:
    print(words.get("Basic"))
elif "Essential" == meaning:
    print(words.get("Essential"))
elif "Medicine" == meaning:
    print(words.get("Medicine"))
elif "Numbers" == meaning:
    print(words.get("Numbers"))
else:
    print(f"{meaning} is not in my dictionary :")




# #assignment 2 making a simple calculator 
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number : "))
# total = print(num1+num2)
# total = print (num1*num2)
# total = print (num1-num2)
# total = print (num1%num2)
# total = print (num1/num2)
# total = print (num1^num2)
# total = print (num1**num2)