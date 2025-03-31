import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.loot_table = ["Health Potion", "Smoke Bomb", "Mini Explosive", "Shield"]

    def monster_attacks(self, hero):
        damage = self.combat_strength
        hero.health_points -= damage
        print(f"Monster attacks! Hero loses {damage} health points.")

    def drop_loot(self):
        """Drops a random item with a 50% chance."""
        if random.random() < 0.5:
            return random.choice(self.loot_table)
        return None