# WAP to find out whether a student is pass or fail, 
# if it requires total 40% and atleast 33%, in each subjec to passs.
# Assume 3 subjcts and take marks as an iput from the user.

a=int(input("Enter 1st subject marks"))
b=int(input("Enter 2nd subject marks"))
c=int(input("Enter 3rd subject marks"))

if(a<33 or b<33 or c<33):
    print("you are fail becuas less than 33% in one of the subjects")
elif(a+b+c)/3 <40:
    print("Yor are fail due to total percentage less than 40")
else:
    print("you are pass")    

   



