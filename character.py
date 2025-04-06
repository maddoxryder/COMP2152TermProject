import random  # We’ll use this to roll for random values

# This is the parent class that Hero and Monster will inherit from
class Character:
    def __init__(self):
        # These are private variables (note the double underscore)
        # They represent the character's base stats
        self.__combat_strength = random.randint(1, 6)  # Simulates a small dice roll
        self.__health_points = random.randint(10, 20)  # Simulates a bigger health roll
        print("Character created with Combat Strength:", self.__combat_strength, "and Health Points:", self.__health_points)

    # This method runs when the object is destroyed (usually when the program ends)
    def __del__(self):
        print("The Character object is being destroyed by the garbage collector")

    # Getter for combat_strength – lets us access the private variable
    @property
    def combat_strength(self):
        return self.__combat_strength

    # Setter for combat_strength – lets us safely change it
    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 0:
            self.__combat_strength = value  # We only allow non-negative values

    # Getter for health_points
    @property
    def health_points(self):
        return self.__health_points

    # Setter for health_points
    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self.__health_points = value