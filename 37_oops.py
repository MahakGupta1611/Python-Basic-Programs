# oops focus on reusable code(implement DRY principle)(class,object,abstraction,encapsulation)
# blank form(blue print)(class), filled form(application)(object)
# class name written in PascalCase
# class contain methods and variables

# object is an instantiation of class.Memory is allocated only after object instantiation

class RailForm:
    formType="RailForm"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

appform=RailForm()
appform.name="mahak"
appform.train="Rajdhani"
appform.printdata()  
     
# class attribute:(An attribute that belongs to the class rather than a particular object)
class Employee:
    company="Google"
mahak=Employee()
print(mahak.company)
# now we want to change the company so we write this code
Employee.company="You tube"             #changing classs attribute
print(mahak.company)

# instance attribute (an attribute that belongs to instance(object) like name, sal,employee code are different)
class Employee:
    company="Google"
    salary=100
mahak=Employee()
vikas=Employee()
# creating instance attribute
mahak.salary=500
vikas.salary=600
print(mahak.company)
print(mahak.salary)
print(vikas.company)
print(vikas.salary)

# self parameter(self refers instance of the class)(it is automatically passed with a function call from an object)
class Employee:
    company="Google"
    def getSalary(self):
      print("salary is 100k")

mahak=Employee() 
mahak.getSalary()   #this converts into Emploee.getSalary(mahak), here mahak is passeda s argument thts why self is passed as argument in function

# static method(sometimes we need a functio that doesnt use self paramter). we define static method like thsi
class Employee:
    company="Google"
    def getSalary(self):
      print("salary is 100k")
    @staticmethod
    def greet():                #doesnt require pass self parameter
      print("Good Morning")

mahak=Employee()
mahak.getSalary()       #this converts into Emploee.getSalary(mahak) 
mahak.greet()           #this converts into Employee.greet()

# _ _ init _ _ constructor (special method which is first run as soon as the object is created)
# it takes self argument and can also take further argument
class Employee:
    company="Google"

    def __init__(self, name, salary):                 #init automatically run (self)
       self.name=name
       self.salary=salary
       print("Employee is created")

    def details(self):
       print(self.name)   
       print(self.salary)

mahak=Employee("mahak","10000")
mahak.details()


