# Given three integers, print the smallest one. (Three integers should be user input)
x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))
if x < y and x < z:
    print(f"x is smallest.")
elif y < x and y < z:
    print(f"y is smallest.")
else:
    print(f"z is smallest")