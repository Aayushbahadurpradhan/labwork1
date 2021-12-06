# Given a n-digit number. Find the sum of its digits.
n = int(input("Enter a number:"))
p = 0
while (n>0):
    dig = n % 10
    p = p + dig
    n = n // 10
print("The total sum of digits is:",p)