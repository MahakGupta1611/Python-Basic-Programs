# list indexing
a= [1,2,3,56,78, 6, 8 , 90, 123 ] #index value started at '0'
print(a)
print(type(a))
print(a[8])     #access using index using a[0], a[1] etc
a[0]=789        #list can be updated or changed
print(a)      

# we can create a list with items of different types
a=[45, "hello", 78.9, 0, 'bye']
print(a)
print(type(a))

# list slicing
b=["viv","div","fig","gig",89,"love"]
print(b[0:6])
print(b[0:6:1])
print(b[0:6:2])
print(b[-2:])  #print till last from -2 i.e gig 

#WAP to store 7 fruits in a list entered by the user.
fr1=input("Enter the fr1 Name")
fr2=input("Enter the fr2 Name")
fr3=input("Enter the fr3 Name")
fr4=input("Enter the fr4 Name")
fr5=input("Enter the fr5 Name")
fr6=input("Enter the fr6 Name")
fr7=input("Enter the fr7 Name")
fruitlist=[fr1,fr2,fr3,fr4,fr5,fr6,fr7]
print(fruitlist)

# WAP to accept marks of 6 students and display them in a sorted manner
st1=int(input("Enter marks of st1"))
st2=int(input("Enter marks of st2"))
st3=int(input("Enter marks of st3"))
st4=int(input("Enter marks of st4"))
st5=int(input("Enter marks of st5"))
st6=int(input("Enter marks of st6"))
markslist=[st1,st2,st3,st4,st5,st6]
markslist.sort()
print(markslist)

#WAP to sum a list with 4 numbers.
a=[3,5,6,7]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a)) #alternative method to sum the numbers
