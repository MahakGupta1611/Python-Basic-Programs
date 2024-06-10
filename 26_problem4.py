# WAP to find whether a given username contains less than 10 characters or not.

a=str(input("Enter the name "))
print(len(a))

if(len(a)<10):
    print("The length is less than 10 characters")
else:
    print("The length is greater than 10 characters")    
