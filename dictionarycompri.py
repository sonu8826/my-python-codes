users = [
    (0,"bob","password"),
    (1,"rolf","bob123"),
    (2,"joe","12345")
]
username_mapping = {user[1]: user for user in users}
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
_, username, password = username_mapping[username_input]
if password_input == password:
    print("your details are correct!")
else:
    print("incorrect")