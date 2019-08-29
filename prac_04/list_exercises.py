# Question 1

numbers = []
for number in range(5):
    user_input = int(input("Number: "))
    numbers.append(user_input)
first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average_number = (sum(numbers)) / len(numbers)
print("The first number is {}".format(first_number))
print("The last number is {}".format(last_number))
print("The smallest number is {}".format(smallest_number))
print("The largest number is {}".format(largest_number))
print("The average of the numbers is {}".format(average_number))

# Question 2

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_to_validate = input("Username: ")
if username_to_validate in usernames:
    print("Access granted")
else:
    print("Access denied")
