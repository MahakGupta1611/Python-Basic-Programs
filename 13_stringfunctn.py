b="mah gup"      #count spaces also
print(len(b))

a="once upon a time there is girl who seems to be very pretty"
print(len(a))    #return length 
print(a.endswith("y"))
print(a.endswith("pretty"))
print(a.endswith("s"))
print(a.count("i"))
print(a.capitalize())
print(a.find("time"))
print(a.replace("once","mahak"))

# WAP to detect double spaces in a string.(Return -1 if there is no double spaces)
st="This is a string which contain  spaces"
dbsp=st.find("  ")
print(dbsp)

# It replaces double spaces to single spaces(if it contain more than double spaces still it remove only single space)
st=st.replace("  "," ")
print(st)