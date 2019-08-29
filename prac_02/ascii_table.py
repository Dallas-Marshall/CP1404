MENU = """Choose an option;\n(1) - Convert from character to ascii.\n(2) - Convert from ascii to character."""
print(MENU)
user_choice = input(">>> ")
IS_VALID_LENGTH = False
IS_VALID_SELECTION = False
while not IS_VALID_LENGTH and not IS_VALID_SELECTION:
    if len(user_choice) == 1:
        IS_VALID_LENGTH = True
    elif user_choice == '1':
        print("ascii")
        IS_VALID_SELECTION = True
    elif user_choice == '2':
        print("Character")
        IS_VALID_SELECTION = True
    else:
        print("Please select a valid option;")
        user_choice = input(">>> ")
