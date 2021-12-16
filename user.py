def user_age():
    user = int(input("Enter your age :"))
    age = user * 365 * 24 * 60 * 60
    print(f"your age in sec is {age}.")

    print("welcome to second program!")
    user_age()

