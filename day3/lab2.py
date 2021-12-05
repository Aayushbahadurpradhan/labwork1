# WAP which accepts marks of four subjects and display total marks, percentage and grade
a = int(input("enter the marks of algorithm:"))
b = int(input("enter the marks of software:"))
c = int(input("enter the marks of math:"))
d = int(input("enter the marks of gets:"))
total =(a+b+c+d)
percentage = total/4
if percentage >= 70:
    print("Distinction")
elif percentage >= 60:
    print("first Division")
elif percentage >=40:
    print("passed the exam")
elif percentage < 40:
    print("failed the exam")