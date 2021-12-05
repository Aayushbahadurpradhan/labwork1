#  N students take K apples and distribute them among each other evenly. The remaining
# (the indivisible) part remains in the basket. How many apples will each single student
# get? How many apples will remain in the basket? The program reads the numbers N and

ns = int(input("number of students"))
ap = int(input("number of apples?"))
b = ap // ns
c = ap % ns
print(f"Apple each students will get or have :{b} ")
print(f"Apple remain in the basket are :{c} ")