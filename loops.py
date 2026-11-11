#LOOPS
#while LOOP
# num = int(input("Enter the number:"))

# i = 1

# while i<=10:
#     print(num,"*",i,"=",num * i)
#     i+=1


#for loop
#range function(built in function used to generate integers in a given range)
# print(list(range(0,11))) #first nmber included,last is not included
# print(list(range(5)))
# print(list(range(0,10,1)))
# print(list(range(0,10,2)))
# print(list(range(10,0,-1)))

#Sequence
#string
# for i in "Karachi":
#     print(i)
# for i in ["karachi", "Lahore", "Sargodha"]:
#     print(i)
# for i in ("karachi", "Lahore", "Sargodha"):
#     print(i)
# for i in range(1,11,2):
#     print(i)

#Break,continue,pass
#Break--breaks or terminates the loop when paticular break condition meets
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)


#continue--skips that particular iteration and move to the next
for i in range(1,11):
    if i==5:
        continue
    print(i)


#pass--is a filler,like when you write a loop but don't sure what will be the inner logic.so you use pass so that error will not be shown and you can write the logic later
# for i in range(1,11):
#     pass