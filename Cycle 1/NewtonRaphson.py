import sympy as sp
x=sp.symbols('x')
f=x**3+2*x-2
def y(x):
    return x**3+2*x-2
def interval():
    i=0
    if y(i)==0:
        print("The root is:",i)
        return i
    else:
        while (y(i)*y(i+1))>=0:
            i=i+1
            if y(i)==0:
                print("The root is:",i)
                break
        interval_values=[]
        if y(i)<y(i+1):
            interval_values=[i,i+1]
        else:
            interval_values=[i+1,i]
    return interval_values
def newtonRaphson():
    a=interval()
    if abs(y(a[0]))>=abs(y(a[1])):
        x0=a[1]
    else:
        x0=a[0]
    tol=1e-6
    der=sp.diff(f,x)
    while True:
      derivativeValue=der.subs(x,x0)
      x1=x0-float((y(x0)/derivativeValue))
      if abs(x1-x0)<tol:
        break
      x0=x1
      print("The root is:",x1)
newtonRaphson()

    
    
