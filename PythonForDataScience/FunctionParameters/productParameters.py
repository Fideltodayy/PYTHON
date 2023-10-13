#Author: Fideltodayy
#Created: 05/10/2023
#This is an example to illustrate how parameters can be used for arithmetics in a function

print("Welcome to python for Data Science")
print("Products of the parameters are: ")

#Variables and operators
x=int(input("enter the value of x :"))
y=int(input("enter the value of y :"))
z=int(input("enter the value of z :"))
# print("Given x=2, y=4 and z=6")
a = x + y
b = z - y
print("x + y = " + str(a))
print("z - y = " + str(b))
print("z / y = " + str(z/y))

#function definition
def myfunc(u,v):
    print("u and v are parameters whose values corespond to x and y")
    print("u + v = " + str(u + v))

myfunc(x,y)

def paramProduct(a,b,c):
    print("Product is :" + str(a*b*c))

paramProduct(x,y,z)