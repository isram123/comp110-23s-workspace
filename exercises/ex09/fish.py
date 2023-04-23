"""File to define Fish class."""
__author__ = "730463838"


class Fish:
    """Class Fish."""
    age: int

    def __init__(self):
        """Init."""
        self.age = 0 
        return None
    
    def one_day(self):
        """One Day."""
        self.age += 1
        return None