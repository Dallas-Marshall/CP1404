"""Taxi simulator from prac_08 Do It Yourself exercise."""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_06.car import Car

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program that uses your Taxi and SilverServiceTaxi classes."""
    bill_total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    user_menu_selection = input(">>> ").lower()
    while user_menu_selection != "q":
        if user_menu_selection == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif user_menu_selection == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            bill_total += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill_total))
        print(MENU)
        user_menu_selection = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(bill_total))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
