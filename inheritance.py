#  # using the try and expect
# try:
#     num1 = int(input("Enter a number : "))
#     num2 = int(input("Enter a number : "))
#     total = num1 / num2
#     print(total)




# except ZeroDivisionError :
#     print(f"{num1} cannot be divided with {num2}")
#     print(F"Error")



#     if (a<3):
#         print("gfy")

def divide (x,y):
    try :
        result = x // y
        print("Yeah ! Your answer is :",result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("working")
    finally:
        print("executed")
    

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
divide(a,b)








