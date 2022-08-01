#understanding lamdab function
add_numbers_and_five = lambda number1, number2 : number1+number2+5
print(add_numbers_and_five(number1=3,number2=4))
#lambada maps :it takes two argument the function and the list

list1 = [6,45,3,2,32]
print(list1)
def add_five(number):
   return number +5

new_list = list(map(add_five, list1))
print(new_list)


list2 = [43,45,24,67]
print(list2)

new_list = list(map(lambda x :x+5, list2))
print(new_list)
#lambda reduce is use to tally up the sum, multiplication
from functools import reduce
numbers = [10,20,30,40]
print(numbers)

results = reduce(lambda a, b: a + b, numbers)
print (results)







my_score = 1000
message = "I scored %s points"
print = (message % my_score)