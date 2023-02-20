p=int(input("principle:"))
c=float(input("Compound interest:"))
k=int(input("Duration in months:"))
n=k/12
r=(pow((c+p)/p,1/(n*4))-1)*400
print(round(r))