from character import Character
import random

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.type = "Normal"
        print(f"{self.type} Monster created (CS: {self.combat_strength}, HP: {self.health_points})")

    def monster_attacks(self, hero):
        damage = self.combat_strength
        print(f"    |    {self.type} Monster attacks with {damage} combat strength!")
        hero.health_points -= damage
        print(f"    |    Hero HP reduced to {hero.health_points}")

    def apply_environment_effect(self, environment):
        """Apply environment-specific bonuses"""
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
        self.combat_strength += 1
        print(f"    |    Fire Monster (CS: {self.combat_strength}, HP: {self.health_points})")

class IceMonster(Monster):
    def __init__(self):
        super().__init__()
        self.type = "Ice"
        self.health_points += 2
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
    """Create a random monster type"""
    monster_types = [Monster, FireMonster, IceMonster, BatMonster, CamouflagedMonster]
    return random.choice(monster_types)()