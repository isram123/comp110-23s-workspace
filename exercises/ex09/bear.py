"""File to define Bear class."""
__author__ = "730463838"


class Bear:  
    """Class Bear."""
    age: int
    hunger_score: int

    def __init__(self):
        """Init."""
        self.age = 0
        self.hunger_score = 0 
        return None
     
    def one_day(self):
        """One day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Eat."""
        self.hunger_score += num_fish