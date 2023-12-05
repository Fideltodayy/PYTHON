#

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#clear tuple
del thistuple

#
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 
del thistuple

#

tuple1 = ("abc", 34, True, 40, "male") 
print(tuple1)
del tuple1

#
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1]) 
print(thistuple[2:5]) 
print(thistuple[:4]) 
print(thistuple[2:]) 
print(thistuple[-4:-1]) 
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#
#changing the values of a tuple by changing it to an list and modifyng it then convert it back to a tuple

x = (1,2,4,5,7,9,23)
print(x)
y = list(x)
y[3] = 45
y.append(654)
x = tuple(y)
print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#unpacking

fruits = ("apple","banana","cherry")
(green,white,black) = fruits
print(green)
print(black)
print(white)


#
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

#
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 