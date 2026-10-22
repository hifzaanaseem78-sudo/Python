print("Hello World",end=' ')
print(6)

print("Pakistan","India",6,True,sep="-")

#interger
print(4)

#float
print(4.5)

#boolean
print(False)

#complex
print(4+5j)

#string
print("Heyy!Hifza here!")

#list
print([1,2,3,4,5])

#tuple
print((1,2,3,4,5))

#sets
print({1,2,3,4,5})

#dictionary
print({"Name":"Hifza","Age":"22"})

#comments(piece of code not executed by compiler or interpreter,used for code readability)


#no variable declaration in python-->Dynamic typing
#Dynamic typing(python automatically detects data type,no need to declare the data type)
#Static typing(need to declare the data type)
#Dynamic Binding(aik variable multiple data types store kr paye)
#variable is not binded to specific data type
# name = "Hifza"
# print(name)

#special syntax
# a =5;b=6;c=7
# print(a)
# print(b)
# print(c)

# a,b,c = 4,5,6
# print(a)
# print(b)
# print(c)

# a = b = c =6
# print(a)
# print(b)
# print(c)


#keywords-->words reserved by program and have special meaning
# import keyword
# print(keyword.kwlist)

#identifiers-->names used to identify a variable,function,class,modulw or other objects


#taking user input
# name = input("Enter your name: ")
# print("Your name is:", name)

# first_num = input("Enter first number: ")
# second_num = input("Enter second number: ")
# sum_nums = first_num + second_num
# print(sum_nums)

#type
# a = 5
# print(type(a))

#Type conversion
#implicit->python converts data types by itself
# print(4 + 5.5)
# print(2 + 3+5j)
# print(3.5 + 2+6j)

#explicit->programmers have to tell to about type conversion
# first_num = 5
# second_num = 10
# print(first_num + second_num)

# print(int(5.4))

# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))
# sum_nums = first_num + second_num
# print(sum_nums)


#Literals
#Numeric literals
a = 0b1010 #Binary literal
b = 100 #decimal literal
c = 0o310 #Octal literal
d =0x12c #Hexadecimal literal
print(a, b, c, d)

#Float Literal
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3
print(float_1, float_2, float_3)

#Complex Literal
x = 3.14j
print(x, x.imag, x.real)

import sys
sys.stdout.reconfigure(encoding='utf-8')

#STRING LITERALS
unicode = u"\U0001f600"
print(unicode)


raw_str = r"string"
print(raw_str)

#BOOLEAN LITERAL
a = True + 1;
print(a)

#SPECIAL LITERAL-> used when we just want to declare a variable
k = None
print(k)

#operators 
#arithematic 
x = 4
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)

#comparison 
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

#Logical operators
x = True
y = False

print("logical OR",x or y)
print("logical AND",x and y)
print("logical NOT",not x)

#Bitwise
x = 2
y = 3
print ("bitwise AND",x & y)
print ("bitwise OR",x | y)
print ("bitwise right shift",x >> 2)
print ("bitwise left shift",y << 3)
print ("bitwise one's complement",~x)
