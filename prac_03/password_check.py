"""
Dallas Marshall
"""
MIN_LENGTH = 5
password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    password = input("Enter a password: ")
print("{}".format(len(password) * '*'))
