n=int(input())
flag=0
if n==1:
    print("Not a prime")
else:
    for i in range(2,n//2):
        if n%i==0:
            flag=1
            print("Not a prime")
            break
    if flag==0:
        print("Prime")
        
