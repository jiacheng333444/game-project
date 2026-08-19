import character

class Tank(character.Character):
    def __init__(self, name):
        
        
        # 150 HP, but only 8 base attack
        super().__init__(name=name, hp=150, base_attack=8)
        
        print("\n--- Equipping Starting Gear ---")
        self.equip_weapon("Iron Warhammer", weapon_damage=6)
        self.equip_armor("Heavy Steel Plate", defense_power=10)
        
        self.learn_ability("Shield Bash")

    def shield_bash(self, target):
        
        print(f"\n{self.name} uses Shield Bash!")
        
        if "Shield Bash" in self.abilities:
            # Shield bash does a flat amount of bonus damage
            bash_damage = self.base_attack + 8 
            print(f"{self.name} slams {target.name} with their shield for {bash_damage} damage fr")
            target.take_damage(bash_damage)
        else:
            print(f"{self.name} doesn't know how to do that yet.")
    
