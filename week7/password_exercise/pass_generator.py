import random
import string


def generate_password(length):
    """
    Generate a random password of specified length containing
    uppercase, lowercase, digits, and special characters.

    Parameters:
    length (int): The length of the password to generate.

    Returns:
    str: The generated password.
    """
    if not isinstance(length, int) or length < 1:
        raise ValueError("Password length must be a positive integer.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    try:
        # Test the program with different password lengths
        for length in [8, 12, 16, 20]:
            password = generate_password(length)
            print(f"Generated password of length {length}: {password}")
    except ValueError as e:
        print(f"Error: {e}")
