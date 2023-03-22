# Dictionary Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict.get("model")
print(x)
thisdict["colour"] = "Red"
print(thisdict)
thisdict["colour"] = "Blue"
print(thisdict)
xy = thisdict.keys()
print(xy)
yz = thisdict.values()
print(yz)
for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])

thisdict.items()
for x,y in thisdict.items():
  print(x,y)

if "mode" in thisdict:
  print("yes, this is correct")
else:
  print("No, This is false")
print(thisdict)
print(len(thisdict))

thisdict.pop("colour")
print(thisdict)
thisdict["colour"] = "Red"
print(thisdict)

thisdict.popitem()
print(thisdict)
thisdict["colour"] = "Red"
print(thisdict)

del thisdict["colour"]
print(thisdict)
thisdict["colour"] = "Red"
print(thisdict)

dict2 = thisdict.copy()
print(dict2)

dict3 = dict(thisdict)
print(dict2)

myfamily = {"child1" : {"name" : "Emil", "year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}
print(myfamily)
child = myfamily["child2"]
print(child)

child1 = {"name" : "Emil","year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}
childsum1 = {"child1":child1,"child2":child2,"child3":child3}
print(childsum1)
