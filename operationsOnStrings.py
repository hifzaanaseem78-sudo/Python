#operations on strings
#arithmatic operations
#addition---concatenation
c = "hello"
print(c + " " + "world")

#multiplication
print("*" * 10)

#relational operations
print("hello" == "world")
print("hello" != "world")

#lexiographically--acc to the dictionary
print("Sargodha" > "Islamabad")
print("Karachi" < "Sargodha")
print("Sargodha" > "sargodha")


#logical operations
print("hello" and "")
print("hello" and "world")

print("hello" or "")
print("" or "")

print(not "hello")
print(not "")

#loops
c = "hello world"
for i in c:
    print(i)

for i in c[:11:2]:
    print(i)

#membership
print("h" in c)
print("k" in c)