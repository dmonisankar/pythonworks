def check_password(mypass):
    if len(mypass) >= 8 :
        return True
    else:
        return False

print(check_password("mylongpassword"))
