def Prime(n,i=2):
    if n==i or n==1:
        return True
    elif n%i==0:
        return False
    return Prime(n,i+1)
    
n=int(input())
if Prime(n):
    print("Prime")
else:
    print("Not a prime")
