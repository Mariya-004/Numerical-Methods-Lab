def binarySearch():
    LB=0
    l=[]
    n=int(input("Enter the number of elements in the list:"))
    UB=n-1
    for i in range(n):
        a=int(input("Enter the element:"))
        l.append(a)
    print("The list is: ", l)
    key=int(input("Enter the element to search for:"))
    while LB<=UB:
        mid=(LB+UB)//2
        if l[mid]==key:
            return mid
        elif l[mid]<key:
            LB=mid+1
        else:
            UB=mid-1 
   
    return -1
r=binarySearch()
if r!=-1:
    print("Element found at:",r)
else:
    print("Element not found")
