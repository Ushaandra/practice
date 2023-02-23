def Armstrong(n):
    s=str(n)
    l=len(s)
    count=0
    for i in s:
        count=count+(int(i)**len(s))
    if n==count:
        print("Armstrong")
    else:
        print("Not an Armstrong")
def Perfect(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    if n==c:
        print("Perfect")
    else:
        print("Not Perfect number")
def Strong(n):
    s=str(n)
    z=0
    for i in s:
        k=int(i)
        c=1
        for j in range(1,k+1):
            c*=j
        z+=c
    if n==z:
        print("Strong")
    else:
        print("Not Strong")
n=int(input())
Armstrong(n)
Perfect(n)
Strong(n)
            