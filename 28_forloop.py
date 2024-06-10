# for loops is used to iterate or traverse a sequence like list, tuple or string.
# WAP to print the contents of a list using while loop
a=['apple','banana','grapes','peach']
for item in a:
    print(item)


# for with else(if the code is to be executed when the loop exhausts)
for i in range(10): 
    print(i)
else:
    print("when loop is exhausted then else loop run") 

#break st (to come out of the loop)
for i in range(7):
    print(i)
    if i==5: 
        break
    
#continue st( to stop the current iteration of the loop and continue with the next one)

for i in range(10):
    if i==6:    #it skip 6 st and continue with next one
        continue 
    print(i)

# pass statement( null statement, "Do nothing")

i=4

def fun(a,b):
     pass   #by using pass we can blank the statement so that program will run
if(i>0):
    pass #indentation error can be removed by pass
print("without pass it throw an error") 

