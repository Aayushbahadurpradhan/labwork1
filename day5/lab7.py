# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for c in range(6):
    if (c == 3 or c==6):
        continue
    print(c,end=' ')
print("\n")