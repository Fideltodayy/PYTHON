#THe map function is used to apply a function to each element in a list.
numbers = [1, 2, 3, 4, 5,5,]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]


#the isinstance() function returns True if the specified object is of the specified type, otherwise False.

num = "5"
if isinstance(num,str):
    print("Yes")
else:
    print("No")

#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

#The reduce() function is a little less obvious in its intent. This function reduces a list to a single value by combining elements via a supplied function. The reduce() function is defined in the functools module

from functools import reduce    
numbers = [1, 2, 3, 4, 5]
summed_numbers = reduce(lambda x,y: x + y, numbers) 
print(summed_numbers)   
# Output: 15

#THe round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
pi = 3.14159265359
rounded_pi = round(pi,2)
print(rounded_pi)


#The repr() function returns a printable/string representation of the given object.
my_dict = {'name': 'John', 'age': 25}
print(repr(my_dict))