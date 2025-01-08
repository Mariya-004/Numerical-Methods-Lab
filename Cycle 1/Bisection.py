def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("The function must have different signs at the endpoints a and b.")
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c 
        else:
            a = c 
        iter_count += 1 
    return (a + b) / 2
if __name__ == "__main__":
    def func(x):
        return x**2- 4  
    a = 0
    b = 3
    root = bisection_method(func, a, b)
    print(f"The approximate root is: {root}")
