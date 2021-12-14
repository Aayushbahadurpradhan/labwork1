#Write a program to find the factorial of a number
nu = int(input("Enter an number?? "))
factorial = 1
if nu < 0:
   print("Sorry the factorial does not exist for negative numbers given")
elif nu == 0:
   print("factorial of 0 is 1")
else:
   for i in range(1,nu + 1):
       factorial = factorial*i
   print("The factorial of",nu,"is",factorial)