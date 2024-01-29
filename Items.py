import Player
Player.Player = Player.Player


class Weapons():

    def __init__(self):
        self.dmg = 0
        self.crit = 0


class Sword(Weapons):

    def __init__(self):
        super().__init__()
        self.dmg = 2
        self.crit = 5
        self.name = "None"
        self.wert = 0

    def Unequip(self, target):
        Player.Player.attack -= target.dmg
        Player.Player.crit -= target.crit
        Player.Player.waffe = 0
    def Equip(self):
        self.Unequip(Player.Player.waffe)
        Player.Player.waffe = self
        Player.Player.attack += self.dmg
        Player.Player.crit += self.crit

    def Info(self):
        print("""name = """,self.name,"""
atk = """,self.dmg,"""
crit =""",self.crit)


class Holzschwert(Sword):

    def __init__(self):
        super().__init__()
        self.name = "holzschwert"
        self.wert = 1


class Steinschwert(Sword):

    def __init__(self):
        super().__init__()
        self.name = "steinschwert"
        self.dmg = 3
        self.crit = 9
        self.wert = 10

class Eisenschwert(Sword):
    def __init__(self):
        super().__init__()
        self.name = "eisenschwert"
        self.dmg = 10
        self.crit = 10
        self.wert = 50


holzschwert = Holzschwert()
steinschwert = Steinschwert()
eisenschwert = Eisenschwert()



items = dict()
items[holzschwert.name] = holzschwert
items[steinschwert.name] = steinschwert
items[eisenschwert.name] = eisenschwert