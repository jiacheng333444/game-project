import character

class Enemy(character.Character):
    def __init__(self, name, monster_type):
        
        self.monster_type = monster_type
        
        if monster_type == "Goblin":
            super().__init__(name=name, hp=40, base_attack=6)
            self.equip_weapon("Rusty Dagger", weapon_damage=2)
            # No armor for the weak goblin!
            
        elif monster_type == "Ogre":
            super().__init__(name=name, hp=120, base_attack=12)
            self.equip_weapon("Giant Club", weapon_damage=8)
            self.equip_armor("Thick Hide", defense_power=4)
            
        else:
            # A default enemy just in case we misspell something
            super().__init__(name=name, hp=50, base_attack=5)