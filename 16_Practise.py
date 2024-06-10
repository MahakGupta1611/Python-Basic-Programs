# WAP to display a user entered name followed by Good Afternnon using input() function,
# a=input("enter your name")
# print("good afternoon " +a)

# WAP to fill in a letter template given below with name and date.
# letter='''Dear </NAME/>
#           You are Selected!
#           </DATE/>'''

letter='''Dear <|name|>,
You are Selected
Date: <|Date|>'''
name=input("Enter your name\n")
Date=input("Enter Date")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|Date|>", Date) 
print(letter)

