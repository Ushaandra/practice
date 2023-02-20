#places all the zeros in the array at the last
k=list(map(int,input().split()))
s=[]
for i in range(len(k)):
    if k[i]!=0:
        s.append(k[i])
for i in range(len(s),len(k)):
    s.append(0)
print("Output:")
for i in s:
    print(i,end=" ")
    