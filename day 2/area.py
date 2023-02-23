import sympy as sy
def f(x,a,b,c):
    return a*(x**2)+b*x+c
x=sy.Symbol("x")
a,b,c=map(int,input("enter a,b,c:").split())
print(sy.integrate(f(x,a,b,c),(x,-5,5)))