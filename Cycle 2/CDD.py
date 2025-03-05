#Implement the central difference method to estimate the derivative of  f(x)=sin(x) at x=π/4 with h=0.05.
import math

def f(x):
  return math.sin(x)

def CDD(x,stepSize):
  cdd=(f(x+stepSize)-f(x-stepSize))/(2*stepSize)
  print("The derivative using central divided difference:",cdd)

CDD(math.pi/4,0.05)
