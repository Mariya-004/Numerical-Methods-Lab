#Simpsons rule

def f(x):
  return (2/(1+x**3))

def simpsons(a,b):
  h=(b-a)/n
  sum=f(a)+f(b)
  for i in range(1,n):
    if i%2==0:
      sum+=2*f(a+i*h)
    else:
      sum+=4*f(a+i*h)
  sum=sum*h/3
  return sum

a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
n=int(input("Enter the n:"))
print("The integral is:",simpsons(a,b))

