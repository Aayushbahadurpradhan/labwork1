# Take username and password from user and check it again for the three times whether the user has entered the right
# username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
# for consecutive 3 times and if the limit exceeds than print "Attempt finished".
username=input("enter your username:")
password=input("enter your password:")
for a in range (0,3):
    print("enter your credentials")
    username1=input("enter your username:")
    password1=input("enter your password:")
    if username==username1 and password==password1:
        print("you are successfully logged.")
        break
    else:
        if(username!=username1 or password!=password1):
            print("invalid credentials")
else:
    print("3attemt fnished")