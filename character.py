
class Character:
    def __init__(self, name, hp, base_attack):
        # Sets up the basic stats, plus empty slots for gear and abilities.
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.base_attack = base_attack
        
        # New inventory and ability trackers and stuff
        self.weapon = None  # No weapon equipped yet
        self.armor = None   # No armor equipped yet
        self.abilities = [] # Empty list of abilities

    def equip_weapon(self, weapon_name, weapon_damage):
        # Equips a weapon and stores its name and damage bonus.
        self.weapon = {"name": weapon_name, "damage": weapon_damage}
        print(f"{self.name} equipped the {weapon_name} (+{weapon_damage} Attack)!")

    def equip_armor(self, armor_name, defense_power):
        # Equips armor and stores its name and defense bonus.
        self.armor = {"name": armor_name, "defense": defense_power}
        print(f"{self.name} equipped the {armor_name} (+{defense_power} Defense)!")

    def learn_ability(self, ability_name):
        # Adds a new special move to the character's list 
        self.abilities.append(ability_name)
        print(f"{self.name} learned a new ability: {ability_name}!")

    def take_damage(self, damage_amount):
        # Subtracts health, but armor blocks some of the damage first!"""
        actual_damage = damage_amount
        
        # If the character has armor, reduce the incoming damage
        if self.armor is not None:
            actual_damage -= self.armor["defense"]
            
        # Armor shouldn't heal you so if damage goes below 0, set it to 0.
        if actual_damage < 0:
            actual_damage = 0
            
        self.hp -= actual_damage
        
        if self.hp < 0:
            self.hp = 0
            
        print(f"{self.name} takes {actual_damage} damage! ({self.hp}/{self.max_hp} HP remaining)")

    def is_alive(self):
        # Returns True if the character still has health."""
        return self.hp > 0

    def attack(self, target):
        # Attacks the target using base attack PLUS weapon damage."""
        total_attack = self.base_attack
        
        # Add weapon damage if they are holding one
        if self.weapon is not None:
            total_attack += self.weapon["damage"]
            
        print(f"{self.name} strikes {target.name} for {total_attack} damage!")
        target.take_damage(total_attack)
    