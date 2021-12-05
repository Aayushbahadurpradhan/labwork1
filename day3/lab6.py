# Given an integer number, print its last digit.
number = int(input(" Enter any number: "))
lastdigit = number % 10
print("The last digit in a given number %d = %d  " %(number, lastdigit))