#  Write a Python program to find those numbers which are divisible by 7 and
# multiple of 5, between 1500 and 2700 (both included).
def mul_div():
     n = list(range(1500,2700))
for n in list(range(1500,2700)):
  if n%7 == 0 and n%5 == 0:
     print((n))