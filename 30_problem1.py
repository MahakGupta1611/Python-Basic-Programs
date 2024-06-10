# WAP to print multiplication table of a given number using for loop and while loop

a=int(input("Enter the number"))
for i in range(1,11):
    print(f"{a}X{i}={a*i}")

a=int(input("enter any no."))
i=1
while(i<=10):
    print(f"{a}X{i}={a*i}")
    i=i+1    

