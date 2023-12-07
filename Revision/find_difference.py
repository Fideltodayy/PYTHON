def find_difference(a,b):
    """
    Custom function to find the difference between two objects.
    Ensures the objects are numeric
    """
    if isinstance(a, (int,float)) and isinstance(b, (int,float)):
        return abs(a-b)
    else:
        raise TypeError("a and b must be numeric")

num1 = False
num2 = 34

try:
    result = find_difference(num1,num2)
    print("The difference is: {}".format(result))
except TypeError as e:
    print(f"Error: {e}")