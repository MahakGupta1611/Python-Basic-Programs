# class method(which is bound to the class and not the object of the class)
class employee():
    name="mahak"
    salary=200

@classmethod
def change(cls,sal):
    cls.salary=sal

e=employee()
print(e.salary)
e.change(900)
print(e.salary)   #now it will print new salary(chnage the class object)