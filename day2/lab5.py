# A school decided to replace the desks in three classrooms. Each desk sits two students.
# # Given the number of students in each class, print the smallest possible number of desks
# that can be purchased
a = int(input("enter first group students :"))
b = int(input("enter second group students :"))
c = int(input("enter third group students :"))
desk = (a//2+b//2+c//2+a%2+b%2+c%2)
print(f" total no. of benches we need:{desk} ")