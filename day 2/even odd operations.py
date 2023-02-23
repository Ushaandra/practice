n=int(input())
count=0
while(n!=1):
    if n%2!=0:
        n=n*3+1
        count+=1
    else:
        n/=2
        count+=1
print(count)