#vowel eater 


userWords = "a" ,"e","i","o","u"
userWord = input("enter a word : ")
if userWord in userWords:
    print 
    userWord = input("enter a word : ")
uneaten_vowel = "b\n" "c\n" "d\n" "f\n" "g\n"


userWord = userWord.upper()
print (userWord)
for lettter in userWord:
    if "A" == userWord:
        break
    elif "E" == userWord:
        break
    elif "I" == userWord:
        break
    elif "O" == userWord:
        break
    elif "U" == userWord:
        break
    if lettter in userWords :
        continue
else:
        print (f"they are part of \n {uneaten_vowel}") 

#second task

# plant = input("enter a plant : ")
# if plant == "spathiphyllum":
#     print ("yes!!!! spathiphyllum is the best plant ever ")
#     if plant == "spathiphyllum":
#         print ("no!!!!, i want a big spathiphyllum")
# if plant == "pelargonium":
#         print ("spathiphyllum! not pelargonnium!")

# else:
#     print ("spathphyllum! not [input]!")









        
        



