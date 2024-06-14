emails = ["true@", "firstgmail.com", "second@gmail.com"]


def email_validator(my_email):
    if "@" not in my_email:
        raise ValueError("The email must contain @")
    print(my_email)


index = 0
while index < len(emails):
    try:
        email_validator(emails[index])
    except ValueError as e:
        print(f"Caught an exception {emails[index]} {e}")
    index = index + 1
