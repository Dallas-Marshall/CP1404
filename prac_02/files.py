# output_file = open('name.txt', 'w')
# name = input("what is your name: ")
# print(name, file=output_file)
# output_file.close()
#
# input_file = open('name.txt', 'r')
# name = input_file.read()
# print("your name is: {}".format(name))
# input_file.close()
#
# input_file = open('numbers.txt', 'r')
# number_1 = input_file.readline()
# number_2 = input_file.readline()
# input_file.close()
# print(number_1 + number_2)

input_file = open('numbers.txt', 'r')
total = 0
for line in input_file:
    number = int(input_file.readline())
    total += number
print(total)

