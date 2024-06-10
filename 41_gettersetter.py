#method name with property decorator is getter method
# define a function +@name.setter decorator 

class employee:
    company="google"
    salary=500
    bonus=700

    @property                       #getter                      
    def total(self):
        return self.salary+self.bonus
    
    @total.setter                       
    def total(self, val):
        self.bonus= val-self.salary
    
e=employee()
print(e.total)  
e.total=1000
print(e.salary)
print(e.bonus)