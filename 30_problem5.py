# WAP to calculate the factorial of a given number using for loop
# n!=1*2*3*4*5

a=int(input("Enter any number "))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
    print(f"{factorial}")