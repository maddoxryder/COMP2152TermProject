from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        print(f"Hero created (CS: {self.combat_strength}, HP: {self.health_points})")

    def hero_attacks(self, monster):
        damage = self.combat_strength
        print(f"    |    Hero attacks with {damage} combat strength!")
        monster.health_points -= damage
        print(f"    |    Monster HP reduced to {monster.health_points}")