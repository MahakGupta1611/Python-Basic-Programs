# case 1:  create an empty dictionary.
#       Allow 4 friends to enter their favourite language as values and use keys as their names. 
#       Assume that names are unique.

# case 2: if names of 2 friends are same. what will happen to the program
# ans: it will remove one key value value pair which is same, 

# case 3:  if languages of 2 friends are same. What will happen to the program.
# ans: it doesnt affect, values may be vary, values may be same but keys always different 

dict={}
fav1=input("Enter your fav language John")
fav2=input("Enter your fav language Max")
fav3=input("Enter your fav language Shino")
fav4=input("Enter your fav language Ryan")

dict['john']=fav1
dict['max']=fav2
dict['shino']=fav3
dict['ryan']=fav4

print(dict)