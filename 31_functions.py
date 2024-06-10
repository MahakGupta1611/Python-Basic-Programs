# Function is group of statement performing a pecific task.
# It can be reused by programmer in a given program.

# normal method to print sum
marks1=[23,56,78,13]
percentage1=(sum(marks1)/400)*100

marks2=[29,78,90,40]
percentage2=(sum(marks2)/400)*100

print(percentage1, percentage2)

# to print sum by the help of function
def function(marks):
    p=(sum(marks)/400)*100
    return p

marks1=[23,56,78,13]
percentage1=function(marks1)

marks2=[29,78,90,40]
percentage2=function(marks2)

print(percentage1, percentage2)

# WAP to greet a user with "GOOD DAY" usimg function

def function(a):
    print("hello, " +a)
function("mahak")            #function call

# Types of function
# 1) Built in : len(), print(), range(), sum()etc
#  2) User defined: 

# Function with arguments
def func(sum1,sum2):
    return sum1+sum2
function("mahak")
s=func(2,3)
print(s)

# default parameter value
def function(name="defalut"):
    print("Hello" +name)
function()    