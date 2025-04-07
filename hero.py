from character import Character  # Inherit from the base class

class Hero(Character):
    def __init__(self):
        # Call parent constructor to initialize combat_strength and health_points
        super().__init__()
        print("Hero object created.")

    def use_potion(self, potion, monster=None):
        if potion == "Health Potion":
            if self.health_points < 20:
                new_health = self.health_points + 5
                self.health_points = min(20, new_health)  # Cap at 20
                print(f"Health restored from {self.health_points - 5} to {self.health_points}")
                return True
            else:
                print("Hero's health is already full")
                return False
        elif potion == "Poison Potion" and monster:
            if monster.health_points > 0:
                monster.health_points = max(0, monster.health_points - 3)
                print("Hero used a Poison Potion! Monster's health is now ", monster.health_points)
                return True
            else:
                print("Monster is already defeated.")
                return False



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
