# WAP to calculate the grade of a student from his marks from the scheme
# 90-100: Excellent
# 80-90: A
# 70-80:B
# 60-70:C
# 50-60:D
# <50:F

a=int(input("Enter your marks"))
if(a>=90):
    grade="Excellent"
elif(a>=80):
    grade="A"
elif(a>=70):
    grade="B"
elif(a>=60):
    grade="C"  
elif(a>=50):
    grade="D"            
else:
    grade="F"

print("your grade is: "+grade)    

