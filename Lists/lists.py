#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Ordered
#Changeable
#Allow Duplicates

#Create a List:
thislist = ["apple","cherry", "banana", "cherry"]
print(thislist)
print(type(thislist))
#List Length
print(len(thislist))
#access list items
print(thislist[1])

#
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("This is the extended list",thislist)
thislist.remove("banana")

print(thislist) 
thislist.pop(1)
print(thislist)

insertLIst = ["apple", "banana", "cherry"]
insertLIst.insert(2,"Watermelon")
insertLIst.append("orange")
print("This is the appended list",insertLIst)
print("\n")

for x in insertLIst:
    print(x)
print("\n")

#looping through a list using the list comprehension
[print(x) for x in insertLIst]

#looping through a list with a while loop
i = 0
while i < len(insertLIst):
    print(insertLIst[i])
    i = i + 1
print("\n")

thislist.sort()
print(thislist)
thislistand = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislistand.extend(thistuple)
print("This is the extended list with a tuple",thislistand)
#clear list
thislistand.clear()
print(thislistand)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
(one,two,three) = list2
print(one)
print(two)
print(three)
for x in list1:
    list2.append(x)
print(list2)


