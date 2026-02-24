# Validate username and password

username = input().strip()
password = input().strip()

# Example valid credentials
valid_username = "admin"
valid_password = "12345"

if username == valid_username and password == valid_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")


#Output:
#Enter username: admin
#Enter password: 12345
#Login Successful
#Enter username: user
#Enter password: pass
#Invalid Username or Password

