"""
Programming language class for prac_06 intermediate exercises.
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of ProgrammingLanguage instance."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"
