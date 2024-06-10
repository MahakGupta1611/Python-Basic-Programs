a="good"
b="morning"
# concatenating two strings
c=a+b
print(c)

a="Mahak Gupta"
print(a[0])
print(a[7])   #doesnt count spaces
print(a[0:4]) #string slicing
print(a[:4]) #assume automatically 0 indices same as [0:4]
print(a[0:]) # same as [0:10] here 10 ia the length of the string
print(a[1:4])
print(a[2:4])
print(a[-1])
print(a[-4:-1]) 

# string slicing with skip value
a="mahak"
print(a[0:4:1])
print(a[0:4:2])
print(a[0:4:3])  #here it print 'm' and then skip two values and the print 'a' again.