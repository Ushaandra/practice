for i in range(1,4):
    print('*'*(i),end="")
    for j in range((3-i)*2):
        print(" ",end="")
    print("***********"+"*"*(2*i),end="")
    for j in range((3-i)*2):
        print(" ",end="")
    print('*'*(i),end="")
    print("")
for i in range(2,0,-1):
    print('*'*(i),end="")
    for j in range((3-i)*2):
        print(" ",end="")
    print("***********"+"*"*(2*i),end="")
    for j in range((3-i)*2):
        print(" ",end="")
    print('*'*(i),end="")
    print("")
