"""File to define Fish class"""

class Fish:

    age: int
    
    def __init__(self):
        self.age = 0 
        copy_fish: list = list[Fish]
        for fish in self.fish:
            if self.age > 3:
                copy_fish.pop(fish)
            else:
                copy_fish.append(fish)
        self.fish == copy_fish

        return None
    
    def one_day(self):
        self.one_day += 1
        return None