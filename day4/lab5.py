# A student will not be allowed to sit in exam if his/her attendance is less than 75%
a = int(input("Number of classes held:"))
b = int(input("Number of classes attended:"))
percentage = b/a*100
if percentage >= 75:
        print("The student is allowed to sit in the exam hall")
else:
     print("The student is not allowed to sit in the exam hall")