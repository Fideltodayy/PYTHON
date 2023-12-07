#THe map function is used to apply a function to each element in a list.
numbers = [1, 2, 3, 4, 5,5,]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
