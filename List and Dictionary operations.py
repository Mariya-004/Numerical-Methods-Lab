
print("List Operations")

#creating a list

print("Creating a list")
l=[1, 2, 3]
print("The list is:",l)
print()

#Inserting into a list using append

print("Inserting into list using append method")
n=int(input("Enter the number of elements to insert:"))
for i in range(n):
    a=int(input("Enter the element:"))
    l.append(a)
print("The list is:", l)
print()

#Accessing elements from the list

#using indexing

print("Accessing elements from the list")
print("The first element of the list is:", l[0])
print("The second element of the list is:",l[1])

#slicing

print("Slicing")
print(l[0:n])

#using negative indexing

print("Negative indexing: helps accessing list from the back")
print("l[-1] prints the last element in the list:",l[-1])
print()

#modifying lists

print("Modifying lists")
print("Using index")
a=int(input("Enter the position of the element:"))
b=int(input("Enter the element:"))
l[a]=b
print("The list is:",l)
print()
#inserting an element at specific position

print("Inserting at a specific position")
c=int(input("Enter the element:"))
d=int(input("Enter the position:"))
l.insert(d, c)
print("The list is:",l)
print()
#extending using another list

print("Extend Method")
ex=[]
no=int(input("Enter the number of elements to extend:"))
for i in range(no):
    a=int(input("Enter the element:"))
    l.append(a)
print("Extended list:",l)
print()

#sorting

print("Sorting a list")
l.sort()
print("Sorted list:",end=" ")
print(l)
print()

#Reversing a list

print("Reversing a list")
l.reverse()
print("Reversed list:",end=" ")
print(l)
print()

#List operations

print("To find the length of the list ")
print("The length of the list is:", len(l))
print()


#removing from list

#pop

print ("Popping an element using index (by default the index is set as -1)")
f=int(input("Enter the index:"))
g=l.pop(f)
print("List after popping is:",l)
print("popped element is", g)
print() 

#remove

print("Removing from list")
q=int(input("Enter the element to remove:"))
l.remove(q)
print("The list is:", l)
print()

#clear
print("Clearing all emements from the list")
l.clear()
print(l)


print("Dictionary Operations")

#creating a dictionary

print("Creating a dictionary")
dict={"Name":"John", "Age":25, "City":"New York"}
print("The dictionary is:", dict)
print()

#Accessing values

print("Accessing values from a dictionary")
print("Using keys")
a=input("Enter the key:")
print(dict[a])
print("Using get method")
dict.get(a)
print()

#Modifying Dictionaries

print("Adding a new key-value pair")
i=int(input("Enter the numbe rof key value pairs:"))
for k in range(i):
    b=input("Enter the key:")
    c=input("Enter the value:")
    dict[b]=c
print("The dictionary is:", dict)
print("Modifying existing key-value pairs")
d=input("Enter the key to modify the value:")
e=input("Enter the value:")
dict[d]=e
print()

#Removing values from a dictionary
f=input("Enter the key of the key-value pair to be removed")
del dict[f]
print("The dictionary is:",dict)
print("Using Pop")
h=input("Enter the key of the key-value pair to be removed")
g=dict.pop(h)
print("The dictionary is:",dict)
print("The popped element is:",g)
print()

#print list of keys and values
print("The list of keys:",dict.keys())
print("The list of values:", dict.values())
print("The list of key-value pairs:", dict.items())
