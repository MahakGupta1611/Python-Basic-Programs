# WAP to read the text from a given file and find out whether it contains the word Twinkle

f=open("sample.txt","r")
a=f.read()
if "twinkle" in a:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()

# all other examples in you tube
