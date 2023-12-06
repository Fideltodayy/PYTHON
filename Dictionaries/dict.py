#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
    "brand": "BMW",
    "model": "M4 competition",
    "year": 2020,
}
print("\n")
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
x = thisdict.get("model")
y = thisdict.items()

print(x)
print(y)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 


thisdict.popitem()
print(thisdict) 


for x in thisdict:
  print(thisdict[x])

for x, y in thisdict.items():
  print(x, y) 