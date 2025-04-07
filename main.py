# Import the random library to use for the dice later
import random
import functions
from hero import Hero
from monster import create_random_monster  # Updated import
import platform
import os

print("Python Version:", platform.python_version())
print("Operating System:", os.name)

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

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

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Create hero and random monster objects
hero = Hero()
monster = create_random_monster()  # Now creates random monster type

# Roll for weapon
print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")
ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
"""
print(ascii_image5)
weapon_roll = random.choice(small_dice_options)

# Limit the combat strength to 6
hero.combat_strength = min(6, (hero.combat_strength + weapon_roll))
print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

# Weapon Roll Analysis
print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Analyze the Weapon roll (Press enter)")
print("    |", end="    ")
if weapon_roll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weapon_roll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

if weapons[weapon_roll - 1] != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

# Roll for player and monster health points
print("    |", end="    ")
input("Roll the dice for your health points (Press enter)")
hero.health_points = random.choice(big_dice_options)
print("    |    Player rolled " + str(hero.health_points) + " health points")

print("    |", end="    ")
input("Roll the dice for the monster's health points (Press enter)")
monster.health_points = random.choice(big_dice_options)
print("    |    Player rolled " + str(monster.health_points) + " health points for the monster")

# Collect Loot
print("    ------------------------------------------------------------------")
print("    |    !!You find a loot bag!! You look inside to find 2 items:")
print("    |", end="    ")
input("Roll for first item (enter)")
loot_options, belt = functions.collect_loot(loot_options, belt)

print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Roll for second item (Press enter)")
loot_options, belt = functions.collect_loot(loot_options, belt)

print("    |    You're super neat, so you organize your belt alphabetically:")
belt.sort()
print("    |    Your belt: ", belt)

belt, hero.health_points = functions.use_loot(belt, hero.health_points)

print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Analyze the roll (Press enter)")
print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.combat_strength))
print("    |    --- You have a strong player: " + str((hero.combat_strength + hero.health_points) >= 15))

print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                
"""
print(ascii_image4)
power_roll = random.choice(list(monster_powers.keys()))
monster.combat_strength = min(6, monster.combat_strength + monster_powers[power_roll])
print("    |    The monster's combat strength is now " + str(
    monster.combat_strength) + " using the " + power_roll + " magic power")

# Dream levels
num_dream_lvls = -1  # Initialize the number of dream levels
while num_dream_lvls < 0 or num_dream_lvls > 3:
    print("    |", end="    ")
    user_input = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
    try:
        num_dream_lvls = int(user_input)
        if num_dream_lvls < 0 or num_dream_lvls > 3:
            print("    |    Number entered must be between 0 and 3. Try again.")
        elif num_dream_lvls != 0:
            hero.health_points -= 1
            crazy_level = functions.inception_dream(num_dream_lvls)
            hero.combat_strength += crazy_level
            print("combat strength: " + str(hero.combat_strength))
            print("health points: " + str(hero.health_points))
    except ValueError:
        print("    |    That's not a number! Try again.")
        num_dream_lvls = -1

print("num_dream_lvls: ", num_dream_lvls)

# Fight Sequence
print("    ------------------------------------------------------------------")
print("    |    You meet the monster. FIGHT!!")
current_environment = random.choice(list(environments.keys()))
print(f"\n    |    BATTLEFIELD: {current_environment.upper()}!")
print(f"    |    {environments[current_environment]['description']}")
monster.apply_environment_effect(current_environment)  # Apply starting environment effects

round_number = 1
while monster.health_points > 0 and hero.health_points > 0:
    # --- Existing Environment Effects ---
    if current_environment == "Cave":
        hero.combat_strength = max(1, hero.combat_strength - 3)
        print("    |    Your visibility is reduced (-3 combat strength)")
    elif current_environment == "Icy":
        hero.combat_strength = max(1, hero.combat_strength - 2)
        print("    |    The icy terrain slows you (-2 combat strength)")
    elif current_environment == "Desert":
        hero.health_points -= 1
        print("    |    The desert heat drains your health (-1 HP)")

    # --- Monster Drop Check ---
    dropped_item = monster.drop_loot()
    if dropped_item:
        if dropped_item == "Health Potion":
            hero.health_points = min(20, hero.health_points + 5)
            print("    |    Hero gained +5 HP!")
        elif dropped_item == "Smoke Bomb":
            monster.health_points = max(0, monster.health_points - 2)
            print("    |    Smoke bomb confuses monster (-2 HP)!")
        elif dropped_item == "Mini Explosive":
            monster.health_points = 0
            print("    |    KABOOM! Monster obliterated!")
        elif dropped_item == "Shield":
            hero.combat_strength += 3
            print("    |    Shield equipped (+3 combat strength)!")

    # --- Original Action Selection ---
    health_potions = [item for item in belt if item == "Health Potion"]
    poison_potions = [item for item in belt if item == "Poison Potion"]
    print("\n    |    Available actions:")
    print("    |    1. Attack")
    if health_potions:
        print("    |    2. Use Health Potion ({} available)".format(len(health_potions)))
    if poison_potions:
        print("    |    3. Use Poison Potion ({} available)".format(len(poison_potions)))

    print("    |", end="    ")
    action = input("Choose your action (enter number): ")

    if action == "1":
        # Attack logic with environment awareness
        print("    |", end="    ")
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 != 0:  # Hero attacks first
            hero.hero_attacks(monster)
            if monster.health_points > 0:
                monster.monster_attacks(hero)
        else:  # Monster attacks first
            monster.monster_attacks(hero)
            if hero.health_points > 0:
                hero.hero_attacks(monster)

        # Determine stars based on outcome
        if monster.health_points <= 0:
            num_stars = 3
        elif hero.health_points <= 0:
            num_stars = 1
        else:
            num_stars = 2

    elif action == "2" and health_potions:
        if hero.use_potion("Health Potion"):
            belt.remove("Health Potion")
        # Monster gets a free attack
        print("    |", end="    ")
        input("The monster attacks while you're healing! (Press enter)")
        monster.monster_attacks(hero)
        if hero.health_points <= 0:
            num_stars = 1

    elif action == "3" and poison_potions:
        if hero.use_potion("Poison Potion", monster):
            belt.remove("Poison Potion")
        # Monster gets a free attack
        print("    |", end="    ")
        input("The monster attacks while you throw poison! (Press enter)")
        monster.monster_attacks(hero)
        if hero.health_points <= 0:
            num_stars = 1

    else:
        print("    |    Invalid choice or no potions available")
        continue

    # --- End of Round ---
    if monster.health_points > 0 and hero.health_points > 0:
        # 40% chance to change environment
        if random.random() < 0.4:
            current_environment = random.choice(list(environments.keys()))
            print(f"\n    |    ENVIRONMENT SHIFT! The battlefield becomes {current_environment.upper()}!")
            print(f"    |    {environments[current_environment]['description']}")
            monster.apply_environment_effect(current_environment)  # Apply new environment effects

        round_number += 1
        print("    ------------------------------------------------------------------")

if monster.health_points <= 0:
    winner = "Hero"
else:
    winner = "Monster"

# Final Score Display
tries = 0
input_invalid = True
while input_invalid and tries in range(5):
    print("    |", end="    ")
    hero_name = input("Enter your Hero's name (in two words)")
    name = hero_name.split()
    if len(name) != 2:
        print("    |    Please enter a name with two parts (separated by a space)")
        tries += 1
    elif not name[0].isalpha() or not name[1].isalpha():
        print("    |    Please enter an alphabetical name")
        tries += 1
    else:
        short_name = name[0][:2] + name[1][0]
        print("    |    I'm going to call you " + short_name + " for short")
        input_invalid = False

if not input_invalid:
    stars_display = "*" * num_stars
    print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
    functions.save_game(winner, hero_name=short_name, num_stars=num_stars)
    print("    |    Total monsters defeated across all games: " + str(functions.load_monster_kills()))

# item bag
bag = [
    "Health Potion",
    "Poison Potion",
    "Burn Potion",
    "Leather Boots",
    "Flimsy Gloves"
]

# Current statuses affecting the hero
statuses = ["Burned", "Poisoned"]

# Loop through each status the hero has
for status in statuses[:]:  # Loop over a copy of the list so we can safely modify the original
    # List comprehension: find appropriate item based on status
    matching_items = [item for item in belt if status.replace("ed", "") in item]

    # Nested conditional: check if we have the appropriate item
    if matching_items:
        print(f"You are {status}. You have a {matching_items[0]} — you recover!")
        statuses.remove(status)  # Remove the cured status
    else:
        print(f"CAUTION: You are {status} You don't have anything to help! Stay alert.")