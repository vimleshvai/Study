
#A dictionary is a collectio which is unordered, changeable and indexed.

thisdict = {
        "brand" : "Ford",
        "model" : "Mustang",
        "Year"  : 1964
        }

print(thisdict)

#ACCESSING ITEMS

x = thisdict["model"]
print(x)

#we can use get method for the above same result

x = thisdict.get("Year")
print(x)

#change values

thisdict["Year"] = 2020

print(thisdict)

#Loop through a dictionary for loop

for x in thisdict:
    print(x)
    print(thisdict[x])

print(len(thisdict))

#Adding items
thisdict["color"] = "red"

print(thisdict)

