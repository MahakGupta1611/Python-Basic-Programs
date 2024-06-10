# WAP to find greatest of four numbers entered by the user.
a=int(input("Eneter the 1st number"))
b=int(input("Eneter the 2nd number"))
c=int(input("Eneter the 3rd number"))
d=int(input("Eneter the 4th number"))

if(a>b):
    f1=a
else:
    f1=b

if(c>d):
    f2=c
else:
    f2=d   

if(f1>f2):
    print(f1)
else:
    print(f2)         

