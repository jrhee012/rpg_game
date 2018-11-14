from Items import item


class Weapon(item.Item):
    def __init__(self, name, desc, specials, dmg):
        super().__init__(name, "weapon", desc, specials)
        self.dmg = dmg
