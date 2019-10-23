"""Test taxi exercise for prac_08."""
from prac_08.taxi import Taxi


def main():
    """Test code for taxi.py."""
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40km
    taxi.drive(40)

    # Print the taxi's details and the current fare
    print(taxi)
    print(taxi.get_fare())

    # Restart the meter (start a new fare) and then drive the car 100km
    taxi.start_fare()
    taxi.drive(100)

    # Print the details and the current fare
    print(taxi)
    print(taxi.get_fare())


main()
