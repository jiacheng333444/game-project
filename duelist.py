import character

class Duelist(character.Character):
    def __init__(self, name):

        super().__init__(name=name, hp=80, base_attack=15)

        print("\n--- Equipping Starting Gear ---")
        self.equip_weapon("Silver Rapier", weapon_damage=12)
        self.equip_armor("Leather Cloak", defense_power=4)
        self.learn_ability("Precise Strike")

    def precise_strike(self, target):
        print(f"\n{self.name} uses Precise Strike fr")

        if "Precise Strike" in self.abilites:
            special_damage = self.base_attack * 2
            print(f"A flawless hit! {self.name} strikes {target.name} for {special_damage} damage fr")
            target.take_damage(special_damage)
        else:
            print(f"{self.name} doesn't know how to do that yet.")