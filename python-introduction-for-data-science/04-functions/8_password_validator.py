def validate_password(password:str):
    errors = []

    # Rule 1: Length check
    if not 6 <= len(password) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    # Rule 2: Only letters and digits
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    # Rule 3: At least 2 digits
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        errors.append("Password must have at least 2 digits")

    # Output
    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


# Read input and call function
my_password = input()
validate_password(my_password)