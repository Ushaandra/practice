l=list(map(int,input().split()))
k=l
k.remove(max(k))
k.remove(max(k))
print(max(k))