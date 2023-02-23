k=input()
i=1
while(i*i<len(k)):
    i+=1
x=i
if i*i!=len(k):
    for i in range(len(k),i*i):
        k=k+'a'
arr2=[]
y=0
for a in range(x):
    arr1=[]
    for b in range(x):
        arr1.append(k[y])
        y+=1
    arr2.append(arr1)
for i in range(x):
    for j in range(x):
        print(arr2[j][i],end=" ")