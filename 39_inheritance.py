# it is a way of creating a new class from existing class
# override the method of parent class
#single,multiple(2 parent and 1 child),multi level inheritance(one parent and 2 child)

# single inheritance
class parent():
    company="google"
    def name(self):
        print("this is parent class")

class child(parent):   
    language="python"
    def language(self):
        print("this is language")

p=parent()
p.name()
c=child()
c.name()
print(p.company)

# mutiple inhertance
class one():
    company="google"
    name="ma"
class two():
    company="you tube"
    name="ha"
class three(one,two): #write one first so that this class method have highest priority
    name="mahak"

t=three()
print(t.company)    #depend on which class inherit first

# multi level inheritance
# super method is used to access the methods of a super class in the derived class(run both super class as well as base class method)
class foo():
    country="india"
    name="mahak"
    code="901"
class hoo(foo):
    country="australia"
    name="max"
    code="405"
class too(hoo):
    country="singapore"
    
    code="102"

t=too()
print(t.country)
print(t.code)
print(t.name)



    