import math

def f(x):
  return math.exp(x)

def BDD(x,stepSize):
  bdd=(f(x)-f(x-stepSize))/stepSize
  print("The derivative using backward divided difference:",bdd)

a=float(input("Enter the value of x:"))
b=float(input("Enter the step size:"))
BDD(a,b)
