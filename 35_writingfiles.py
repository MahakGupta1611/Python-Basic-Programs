# Writing the file(open in write or in append mode)
f=open("write.txt","w")
f.write("By default write.txt made by just written")
f.write("Again writing, it show the previous content also")
f.close()

# with statement (it shows the output which was written in sample.txt file)
# best way to open and close file by with statement
with open("sample.txt","r") as f:
    a=f.read()
    print(a)
    f.write("")   #wipes all the content
