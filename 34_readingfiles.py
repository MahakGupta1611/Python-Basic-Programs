# A python prog can talk to the file by readingcontent from and writing content to it.
# 2 types of file
# Text file: (.txt, .c)
# binary file: (.jpg,.dat)

# opening a file by open() function: It takes 2 parameters, filename and mode
#  open("this.txt","r")

# Reading the file
f=open("sample.txt")       #by default the mode is r
f=open("sample.txt","r") 
a=f.read()
print(a)
f.close()

# file reading methods
a=f.read(5)                 #it will read only first 5 characters
a=f.readline()               # read only first line

#modes of opening a file
# reading(r), writing(w), appending(a), updating(+)
# read in binary mode(rb), read in text mode(rt)


