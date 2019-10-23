"""SilverServiceTaxi class test code."""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test code for SilverServiceTaxi."""
    my_taxi = SilverServiceTaxi("Silver Service Taxi!", 99, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(my_taxi.get_fare())


main()
