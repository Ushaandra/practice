def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
        
n=int(input("enter value of n:"))
print("Enter values from x2:")
l=list(map(int,input().strip().split()))[:n-1]

s=1 
for i in range(n-1):
    s+=l[i]/fact(i+2)
print(s)