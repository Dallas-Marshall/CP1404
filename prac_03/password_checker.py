"""
Dallas Marshall
"""
MIN_LENGTH = 5


def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    print("{}".format(len(password) * '*'))


def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        password = input("Enter a password: ")
    return password


main()
