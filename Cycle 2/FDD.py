def f(x):
  return (x**3)+(2*(x**2))-(5*x)+7

def FDD(x,stepSize):
  fdd=(f(x+stepSize)-f(x))/stepSize
  print("The derivative using forward divided difference:",fdd)

a=float(input("Enter the value of x:"))
b=float(input("Enter the step size:"))
FDD(a,b)
