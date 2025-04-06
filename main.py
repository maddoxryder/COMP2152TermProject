import random
import platform
import os
from hero import Hero
from monster import create_random_monster

print("Python Version:", platform.python_version())
print("Operating System:", os.name)

# Define Battlefield Environments
environments = {
    "Cave": {
        "hero_penalty": "visibility -3",
        "monster_bonus": "Bats gain +2 Combat Strength",
        "description": "Dark caves reduce your combat effectiveness (-3 strength)"
    },
    "Forest": {
        "hero_bonus": "+30% loot chance",
        "monster_bonus": "Camouflaged monsters gain stealth",
        "description": "Dense vegetation hides secrets (+30% loot chance)"
    },
    "Icy": {
        "hero_penalty": "speed -2",
        "monster_bonus": "Ice monsters +3 HP",
        "description": "Frozen terrain slows your movements (-2 strength)"
    },
    "Desert": {
        "hero_penalty": "-1 HP per turn",
        "monster_bonus": "Fire monsters +1 Combat Strength",
        "description": "Scorching heat drains your vitality (-1 HP/round)"
    }
}

# Create hero and random monster
hero = Hero()
monster = create_random_monster()

# Initial environment
current_environment = random.choice(list(environments.keys()))
print(f"\nStarting Environment: {current_environment.upper()}!")
print(f"Effect: {environments[current_environment]['description']}")
monster.apply_environment_effect(current_environment)

# Combat loop
round_number = 1
while monster.health_points > 0 and hero.health_points > 0:
    print(f"\n--- Round {round_number} ---")
    print(f"Hero: {hero.combat_strength} CS | {hero.health_points} HP")
    print(f"Monster: {monster.combat_strength} CS | {monster.health_points} HP")

    # Apply environment effects to hero
    if current_environment == "Cave":
        hero.combat_strength = max(1, hero.combat_strength - 3)
        print("    |    Cave darkness reduces your combat strength (-3)")
    elif current_environment == "Icy":
        hero.combat_strength = max(1, hero.combat_strength - 2)
        print("    |    Icy terrain slows your movements (-2 strength)")
    elif current_environment == "Desert":
        hero.health_points -= 1
        print("    |    Desert heat drains your health (-1 HP)")

    # Hero attacks
    input("\nPress Enter to attack...")
    hero.hero_attacks(monster)
    if monster.health_points <= 0:
        break

    # Monster attacks
    input("\nPress Enter for monster's turn...")
    monster.monster_attacks(hero)
    if hero.health_points <= 0:
        break

    # 40% chance to change environment
    if random.random() < 0.4:
        current_environment = random.choice(list(environments.keys()))
        print(f"\nEnvironment changed to {current_environment.upper()}!")
        print(f"New effect: {environments[current_environment]['description']}")
        monster.apply_environment_effect(current_environment)

    round_number += 1

# Game over
if monster.health_points <= 0:
    print("\nYou defeated the monster!")
else:
    print("\nThe monster defeated you!")