"""Silver service taxi class derived from Taxi class."""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""

    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flag fall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Get the current fare including flag fall."""
        return self.flag_fall + super().get_fare()
