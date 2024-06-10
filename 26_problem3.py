# A spam comment is defined as a test containing following kywords:
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

a=input("Enter the text below:\n")

text=[("make a lot of money"),("buy now"),("subscribe this"),("click this")]

if(a) in text:
    print("this text is spam")
else:
    print("this text is not spam")