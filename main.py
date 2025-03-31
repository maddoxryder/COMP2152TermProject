import monster

while monster.health_points > 0 and hero.health_points > 0:
    print("-----------------------------------------------------------")

    # Hero Attacks
    print("The hero strikes!")
    monster.health_points = functions.hero_attacks(hero, monster)

    # Check if the monster drops an item
    dropped_item = monster.drop_loot()
    if dropped_item:
        print(f"Monster dropped {dropped_item}")

        # Hero picks up item and uses it
        if dropped_item == "Health Potion":
            hero.health_points = min(100, hero.health_points + 5)
            print("Hero uses Health Potion and gained 5 HP!")
        elif dropped_item == "Smoke Bomb":
            monster.health_points -= 2
            print("Hero uses Smoke Bomb and confuses the Monster")
        elif dropped_item == "Mini Explosive":
            monster.health_points -= monster.health_points
            print("Hero uses Mini Explosive and Blows up the Monster!")
            print("The Monster has been destroyed!")
        elif dropped_item == "Shield":
            hero.combat_strength += 3
            print("Hero picks up shield and gains 3+ Combat Strength!")

        #If monster is still alive it attacks
        if monster.health_points > 0:
            print("The Monster Strikes!")
            hero.health_points = functions.monster_attacks(monster, hero)
