from character import Character  # Inherit from the base class

class Hero(Character):
    def __init__(self):
        # Call parent constructor to initialize combat_strength and health_points
        super().__init__()
        print("Hero object created.")

    def __del__(self):
        # Call parent destructor
        super().__del__()
        print("The Hero object is being destroyed by the garbage collector")

    # Hero’s custom attack method
    def hero_attacks(self, monster):
        print(f"    |    Hero attacks Monster with strength {self.combat_strength}")
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("    |    You have killed the monster!")
        else:
            monster.health_points -= self.combat_strength
            print(f"    |    You damaged the monster. Monster’s health is now {monster.health_points}")