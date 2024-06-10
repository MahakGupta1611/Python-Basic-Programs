#WAP using function to find greatest of three numbers
def max(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c 
m= max(3,6,9)
print(m)   

# print in one line
print("hello", end="")
print("Good Morning")

# strip function(Removes extra spaces)
a="      mahak    "
print(a)
print(a.strip())

# wAP to print table by the help of function
def mul(n):
    n=5
    for i in range(1,11):
        print(f"{n}*{i}={i*n}")
mul(5)
        

    