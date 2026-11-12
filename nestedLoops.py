#nested loop
# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end="")
#     print("")


# for i in range(5,8):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
#         print("")

for i in range(1,4):
    for j in range(1,4):
        print("*","",end="")
    print("")


for i in range(1,4):
    for j in range(1,4):
        print(j,"",end="")
    print("")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,"",end="")
    print("")

for i in range(2,5):
    for j in range(1,6):
        print(i,"*",j,"=",i*j)
    print("")


for i in range(1,6):
    for j in range(0,i):
        print(i,end=" ")
    print("")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


for i in range(6,1,-1):
    for j in range(1,i+1):
        for k in range(1,i-1):
                    print(" ")
        print("*")
    print()