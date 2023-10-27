import pandas as pd
name = ["red", "big","tasty"]

print(type(name))
name[0] = "Fidel"
print(name[0])
lat_lon = (14.03, 35.462)
print(type(lat_lon))
print(lat_lon[1])
name.append("Anne")
print(name)
fruits = {"apple", "banana", "cherry"}
print(type(fruits))
fruits.add("Maembe")
fruits.pop()
print(fruits)

items = { "name": ["Martin","Owino"], "higscore" : [34.54,35,96]}
print(items)
print(type(items))

df = pd.DataFrame(items)
print(df)