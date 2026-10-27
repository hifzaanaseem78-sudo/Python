#correct email - campusx@gmail.com
#correct password - 1234

email = input("Enter your email: ")
if '@' in email:
    password = input("Enter your password: ")

    if email == "campusx@gmail.com" and password == "1234": 
        print("Welcome")
    elif email == "campusx@gmail.com" and password != "1234":
        print("Password incorrect")
        password = input("Enter your password again: ")
        if password == "1234":
            print("Finally correct")
        else:
            print("still incorrect")
    else:
        print("Incorrect Credentials")    
else:
    print("Email incorrect")
