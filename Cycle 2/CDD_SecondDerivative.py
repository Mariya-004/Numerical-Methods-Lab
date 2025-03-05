#Write a function that computes the second derivative of any given function using the central difference method
import math

def f(x):
  return math.sin(x)

def CDD(x,stepSize):
  fdd=(f(x+stepSize)+f(x-stepSize)-(2*f(x)))/(stepSize**2)
  print("The derivative using central divided difference:",fdd)

CDD(math.pi/4,0.05)
