"""guitar class for prac_06 intermediate exercises."""

CURRENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of Guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if guitar is vintage.

        vintage: if guitar age is >= VINTAGE_AGE
        """
        return self.get_age() >= VINTAGE_AGE
