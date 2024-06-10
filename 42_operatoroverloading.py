# using dunder method
# n1+n2.......... n1__add__n2
# n1-n2.......... n1__sub__n2
# n1*n2.......... n1__mul__n2
# n1/n2.......... n1__truediv__n2
# n1//n2.......... n1__floordiv__n2

class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num
    
n1=number(2)
n2=number(5)
sum=n1 + n2
print(sum)

# other dunder/magic operators
# __str__(): used to set what gets dsplayed upon calling str(obj)
# __len__(): used to set what gets displayed upon calling len(obj)