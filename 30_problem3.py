# WAP to find whether a given number is prime or not.

a=int(input("enter any nmber "))
for i in range(2,a):
    if(a%i==0):
        print("This number is prime", +a)
