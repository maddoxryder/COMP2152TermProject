import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.type = "Normal"
        self.loot_table = ["Health Potion", "Smoke Bomb", "Mini Explosive", "Shield"]
        print(f"{self.type} Monster created (CS: {self.combat_strength}, HP: {self.health_points})")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")

    def monster_attacks(self, hero):
        print(f"    |    {self.type} Monster attacks with strength {self.combat_strength}")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            hero.health_points -= self.combat_strength
            print(f"    |    The monster has reduced Player's health to: {hero.health_points}")

    def drop_loot(self):
        """50% chance to drop a random item from loot_table"""
        if random.random() < 0.5:
            item = random.choice(self.loot_table)
            print(f"    |    !! Monster dropped {item} !!")
            return item
        return None

    def apply_environment_effect(self, environment):
        """Apply environment-specific bonuses to this monster"""
        if environment == "Cave" and self.type == "Bat":
            self.combat_strength += 2
            print("    |    Bat gains +2 Combat Strength in caves!")
        elif environment == "Forest" and self.type == "Camouflaged":
            print("    |    Camouflaged monster gains stealth in forest!")
        elif environment == "Icy" and self.type == "Ice":
            self.health_points += 3
            print("    |    Ice monster gains +3 HP in icy terrain!")
        elif environment == "Desert" and self.type == "Fire":
            self.combat_strength += 1
            print("    |    Fire monster gains +1 Combat Strength in desert!")

class FireMonster(Monster):
    def __init__(self):
        super().__init__()
        self.type = "Fire"
        self.combat_strength += 1  # Fire monsters start slightly stronger
        print(f"    |    Fire Monster (CS: {self.combat_strength}, HP: {self.health_points})")

class IceMonster(Monster):
    def __init__(self):
        super().__init__()
        self.type = "Ice"
        self.health_points += 2  # Ice monsters start with more HP
        print(f"    |    Ice Monster (CS: {self.combat_strength}, HP: {self.health_points})")

class BatMonster(Monster):
    def __init__(self):
        super().__init__()
        self.type = "Bat"
        print(f"    |    Bat Monster (CS: {self.combat_strength}, HP: {self.health_points})")

class CamouflagedMonster(Monster):
    def __init__(self):
        super().__init__()
        self.type = "Camouflaged"
        print(f"    |    Camouflaged Monster (CS: {self.combat_strength}, HP: {self.health_points})")

def create_random_monster():
    """Factory method to create a random monster type"""
    monster_types = [Monster, FireMonster, IceMonster, BatMonster, CamouflagedMonster]
    return random.choice(monster_types)()