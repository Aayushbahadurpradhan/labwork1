num = 20
sum = 0;

for i in range(1, num + 1):

    if(not (i % 2) == 0):
        sum += i;

print("\n The Sum of odd numbers from 1 to", num, "is :", sum)