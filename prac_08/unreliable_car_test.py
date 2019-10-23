"""UnreliableCar class test code."""
from prac_08.unreliable_car import UnreliableCar


def main():
    """Test code for UnreliableCar."""
    reliable_car = UnreliableCar("reliable", 600, 95)
    un_reliable_car = UnreliableCar("unreliable", 600, 15)
    for i in range(10, 101, 10):
        print("Attempt to drive {}km's:".format(i))
        print("{:15} drove {:3}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:15} drove {:3}km\n".format(un_reliable_car.name, un_reliable_car.drive(i)))
    print(reliable_car)
    print(un_reliable_car)


main()
