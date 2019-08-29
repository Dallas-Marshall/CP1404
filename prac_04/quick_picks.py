from random import randint

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6


def main():
    number_of_quick_pick = int(input("How many quick picks? "))
    for quick_pick in range(number_of_quick_pick):
        quick_pick_filled = quick_pick_generator()
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(quick_pick_filled[0], quick_pick_filled[1], quick_pick_filled[2],
                                                     quick_pick_filled[3], quick_pick_filled[4], quick_pick_filled[5]))


def quick_pick_generator():
    quick_pick_numbers = []
    for number_index in range(NUMBERS_PER_QUICK_PICK):
        number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick_numbers.append(number)
    return quick_pick_numbers


main()
