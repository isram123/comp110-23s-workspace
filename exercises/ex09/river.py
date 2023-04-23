"""File to define River class."""
__author__ = "730463838"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check Age."""
        copy_fish: list = []
        for fish in self.fish:
            if fish.age <= 3:
                copy_fish.append(Fish())
        self.fish = copy_fish
        copy_bear: list = []
        for bear in self.bears:
            if bear.age <= 5:
                copy_bear.append(Bear())
        self.bears = copy_bear
        return None

    def bears_eating(self):
        """Bear Eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Check Hunger."""
        copy_bear: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                copy_bear.append(Bear())
        self.bears = copy_bear
        return None
        
    def repopulate_fish(self):
        """Repopulate Fish."""
        for x in range(0, len(self.fish) // 2):
            for x in range(0, 4):
                self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulate bear."""
        for x in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """View River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f'Fish Population: {len(self.fish)}')
        print(f'Bear Population: {len(self.bears)}')
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
   
    def one_river_week(self):
        """River."""
        for day in range(0, 7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int): 
        """Remove."""
        for fish in range(0, amount):
            self.fish.pop(0)