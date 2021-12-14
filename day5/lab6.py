# write a Python program to count the number of even and odd numbers from a series of numbers.
r = [33,5,89,2,6,50, 21, 4, 45, 66, 93, 1,11,31,56]
even, odd= 0, 0
for a in r:
    if a % 2 == 0:
        even += 1
    else:
        odd+= 1
print("Even numbers are : ", even)
print("Odd numbers are : ", odd)