# Set is a collection of non-repeatitive elements
# properties of sets
# unordered
# unindexed
# no way to change items in sets
# cannot contain duplicate values
a={1,2,3,4,5,1}
print(type(a))
print(a)  

# create empty set
a=set()
print(type(a))

# adding value to empty set
a.add(5)
a.add(8)
a.add((5,7)) #add tuple to sets but not list and dictionary bcoz both are not hashable
print(a)

# methods
print(len(a))    #return length
a.remove(8)      #remove 8 from sets
print(a)
a.add(78)             # add 78 to sets
print(a)
print(a.pop())       #pop any arbitrary element 
print(a)             #print set after removing arbitrary element
print(a.clear())       #clear set and return none

# What will be the length of the following set
S=set()
S.add(20)
S.add(20.0)
S.add("20")
S={20,20.0,"20"}
print(S)
print(len(S))

# can we have a set with 18(int) and "18"(str)as a values in it? ans: yes
c={18,"18"}
print(type(c))
print(c)

# WAP to input six numbers from the user and display all the unique numbers(once)
no1=int(input("Enter 1st number"))
no2=int(input("Enter 2nd number"))
no3=int(input("Enter 3rd number"))
no4=int(input("Enter 4th number"))
no5=int(input("Enter 5th number"))
no6=int(input("Enter 6th number"))
set={no1,no2,no3,no4,no5,no6}
print(set)






