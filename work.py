user1 = 500
user2 = 400
user3 = 300
user4 = 200
user5 = 100

user1 = 500
 
amount = 300

if amount == 400:
    print (True)

elif amount == 500:
    print ("f{amount} == 500")

elif amount == 100:
    print ("f{amount} == 100") 
elif amount == 200:
    print ("f{amount} == 200")
elif amount == 300:
    print ("f{amount} == 300")

else:
    print ("cannot be borrowed")











    #second
users = ["user1","user2","user3","user4","user5"]
user = input("enter a user")
if user in users:
    print
else:
    print ("f{user}is not part of our customers")


amount1 = 500
amount2 = 400
amount3 = 300
amount4 = 200
amount5 = 100

main_amount = int (input("enter your amount:"))

if main_amount >= amount2 or main_amount == amount1:
    print("f{user} your amount {main_amount}you can borrow")
if main_amount > amount4 or amount4 > main_amount:
    print("f{user} your amount {main_amount}you can borrow")

if main_amount < amount3 or main_amount <= amount3:
    print ("f{user }youramount {main_amount}you can borrow")
elif main_amount >= amount3 or main_amount > amount2:
    print("f{user}your amount {main_amount}you can borrow")




