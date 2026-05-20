#All tasks are written in one file
import random

class Creature:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.potion = None

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack(self):
        raise NotImplementedError("Subclass must implement attack method")

    def drink_potion(self, potion):
        self.potion = potion

        print(f"{self.name} drinks {potion.name} potion!")

        self.health += potion.use()

        print(f"{self.name}'s health is now {self.health}")

class Dragon(Creature):
    def __init__(self, name, fire_power):
        super().__init__(name)
        self.fire_power = fire_power

    def take_damage(self, damage):
        if self.fire_power > 30:
            damage -= 10

            if damage < 0:
                damage = 0

        super().take_damage(damage)

    def attack(self):
        damage = self.fire_power + random.randint(5, 15)
        return damage


class Unicorn(Creature):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def heal(self):
        self.health += self.heal_amount

        if self.health > 100:
            self.health = 100

        print(f"{self.name} heals for {self.heal_amount} HP!")

    def attack(self):
        return 15


class Phoenix(Creature):
    def __init__(self, name, flame_health):
        super().__init__(name)
        self.flame_health = flame_health
        self.revived = False

    def attack(self):
        damage = random.randint(10, 30) + self.flame_health
        return damage

    def take_damage(self, damage):
        super().take_damage(damage)

        if self.health == 0 and not self.revived:
            self.revived = True
            self.health = 50

            print(f"{self.name} rises from ashes and revives with 50 HP!")


class MagicPotion:
    def __init__(self, name, effect, potency):
        self.name = name
        self.effect = effect
        self.potency = potency

    def use(self):
        print(f"Potion effect: {self.effect}")
        return self.potency


class Battle:
    def __init__(self, creature1, creature2):
        self.creature1 = creature1
        self.creature2 = creature2

    def fight_rounds(self, num_rounds):

        potions = [
            MagicPotion("Healing", "Restores health", 20),
            MagicPotion("Mega Heal", "Big healing power", 35),
            MagicPotion("Magic Energy", "Boosts vitality", 25)
        ]

        potion1 = random.choice(potions)
        potion2 = random.choice(potions)

        self.creature1.drink_potion(potion1)
        self.creature2.drink_potion(potion2)

        print("\n===== BATTLE START =====\n")

        for round_num in range(1, num_rounds + 1):

            print(f"--- Round {round_num} ---")

            damage = self.creature1.attack()

            print(f"{self.creature1.name} attacks {self.creature2.name} for {damage} damage!")

            self.creature2.take_damage(damage)

            print(f"{self.creature2.name} health: {self.creature2.health}")

            if not self.creature2.is_alive():
                print(f"{self.creature2.name} has been defeated!")
                break

            damage = self.creature2.attack()

            print(f"{self.creature2.name} attacks {self.creature1.name} for {damage} damage!")

            self.creature1.take_damage(damage)

            print(f"{self.creature1.name} health: {self.creature1.health}")

            if not self.creature1.is_alive():
                print(f"{self.creature1.name} has been defeated!")
                break

            print()

        print("\n===== BATTLE END =====")



#TESTING


print("PROBLEM 1 TEST")
dragon = Dragon("Smaug", 40)
unicorn = Unicorn("Silver", 20)

dragon.take_damage(30)
print(dragon.name, "health:", dragon.health)

unicorn.heal()
print(unicorn.name, "health:", unicorn.health)

print("\nPROBLEM 2 TEST")

phoenix = Phoenix("Fawkes", 10)

creatures = [dragon, unicorn, phoenix]

for creature in creatures:
    print(creature.name, "attack damage:", creature.attack())

print("\nPROBLEM 3 TEST")

potion = MagicPotion("Healing Potion", "Restores HP", 25)

dragon.drink_potion(potion)

print("\nPROBLEM 4 TEST")

battle_dragon = Dragon("Inferno", 45)
battle_phoenix = Phoenix("Ashwing", 12)

battle = Battle(battle_dragon, battle_phoenix)

battle.fight_rounds(3)