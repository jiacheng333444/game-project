import character

class Healer(character.Character):
    def __init__(self, name):
        
        
        # Only 60 HP and 4 base attack
        super().__init__(name=name, hp=60, base_attack=4)
        
        print("\n--- Equipping Starting Gear ---")
        self.equip_weapon("Oak Staff", weapon_damage=3)
        self.equip_armor("Cloth Robes", defense_power=2)
        
        self.learn_ability("Healing Light")

    def heal(self, target):
        
        print(f"\n{self.name} casts Healing Light on {target.name}!")
        
        if "Healing Light" in self.abilities:
            heal_amount = 25
            target.hp += heal_amount
            
            # Prevent healing beyond the max HP
            if target.hp > target.max_hp:
                target.hp = target.max_hp
                
            print(f"{target.name} recovers health fr fr!! ({target.hp}/{target.max_hp} HP remaining)")
        else:
            print(f"{self.name} doesn't know how to do that yet.")