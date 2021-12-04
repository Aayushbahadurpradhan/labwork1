# Given the integer N - the number of minutes that is passed since midnight - how many
# hours and minutes are displayed on the 24h digital clock?
INT = int(input("enter integer:"))
hours = INT // 60
minutes = INT % 60
print(hours,minutes)