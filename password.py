password = ""
newpassword = ""
l = 0
while l not in range(3, 50):
    password = input("\nenter your password: ")
    l = len(password)
    if 3 > l or 50 < l:
        print("Password must be between 3 to 50 characters!")
    else:
        print(f"\n\nPASSWORD: {password}\nPassword looks good!\n")
    q = input("Do you want to change your password?\nYES or NO\n(y/n)")
    while q == "y":
        newpassword = input("\nenter your new password: ")
        l = len(newpassword)
        if 3 > l or 50 < l:
            print("Password must be between 3 to 50 characters!")
        elif newpassword == password:
            print("new password cannot be your old one!")
        else:
            print(f"\n\nnew PASSWORD: {newpassword}\nPassword looks good!\n")
            q = input("Do you want to change your password?\nYES or NO\n(y/n)")
