 
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
  

thisset.add("orange")

print(thisset) 

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "apple"]

thisset.update(mylist)

print(thisset) 

set1 = {"a", "b" , "c",1, 5}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) 
