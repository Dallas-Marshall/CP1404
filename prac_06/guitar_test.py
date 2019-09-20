""""Client code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson", 1922, 16035.40)
    another_guitar = Guitar("Yamaha", 2012, 1000)

    print("{}, Expected 97 got - {}".format(gibson.name, gibson.get_age()))
    print("{}, Expected 7 got - {}".format(another_guitar.name, another_guitar.get_age()))
    print("{}, Expected True got - {}".format(gibson.name, gibson.is_vintage()))
    print("{}, Expected True got - {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
