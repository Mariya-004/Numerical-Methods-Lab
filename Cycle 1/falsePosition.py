def f(x):
    return (x**3)-(4*x)-9 

def interval():
    i=0
    if f(i)==0:
        print("The root is:",i)
        return i
    else:
        while (f(i)*f(i+1))>=0:
            i=i+1
            if f(i)==0:
                print("The root is:",i)
                break
        interval_values=[]
        if f(i)<f(i+1):
            interval_values=[i,i+1]
        else:
            interval_values=[i+1,i]
    return interval_values

def falsePosition(a, b, tolerance):
    iter=0
    x1=(a*(f(b)))-(b*(f(a)))/(f(b)-f(a))
    while abs(f(x1))>tolerance:
        iter+=1
        if f(a)*f(x1)<0:
            b=x1
        else:
            a=x1
        x1=((a*f(b))-(b*f(a)))/(f(b)-f(a))
        print(f"Iteration {iter}: x1 = {x1}, f(x1) = {f(x1)}")
    return x1
a, b = interval()  # Get the interval [a, b] where the root lies
# Set a tolerance for the root approximation
tolerance = 1e-6
# Call the False Position method
root = falsePosition(a, b, tolerance)
print("Root is:",root)
# Now call interval() and print the result
interval_result = interval()  # Find the interval where the function changes sign
print("Interval:", interval_result)




