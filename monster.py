from character import Character  # Inherit from Character base class

class Monster(Character):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        print("Monster object created.")

    def __del__(self):
        # Call parent destructor
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector")

    # Monster’s custom attack method
    def monster_attacks(self, hero):
        print(f"    |    Monster attacks Hero with strength {self.combat_strength}")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("    |    The monster has defeated the hero!")
        else:
            hero.health_points -= self.combat_strength
            print(f"    |    The monster damaged the hero. Hero’s health is now {hero.health_points}")