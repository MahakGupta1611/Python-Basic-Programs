# set of key value pairs
'''properties of dictionary'''
# unordered
# mutable
# indexed
# cannot contain duplicate values
dict={
    "fast":"in a quick manner", 
    "subject":"computer science",
    "marks": [1,5,8],
    "nestdict": {"name":"mahak"},
    1:2
}
print(dict['fast'])
print(dict['subject'])
dict['marks']=[56,78]
print(dict['marks'])
print(dict['nestdict'])
print(dict.keys())
print(type(dict))
print(dict.values())
print(dict.items())
print(dict)
updatedict={
    "coder":"lovy"
}
print(updatedict)
print(dict.get("marks1")) #it return none if key is not present in dictionary
# print(dict["marks1"]) it returns error if key is no present in dictionary

# empty dictionary
a={}
print(type(a))


# WAP to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up
dictionary={
    "pani":"water",
    "aag":"fire",
    "hawa":"air"
}
print("options are",dictionary.keys())
b=input("Enter hindi word\n")
#print(dictionary[b]) this throws error if word is not present so we use .get method
print(dictionary.get(b))