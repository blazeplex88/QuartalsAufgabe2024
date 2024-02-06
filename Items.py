import Inventory


class Weapons():

    def __init__(self):
        self.dmg = 0
        self.crit = 0
        self.infi = 0


class Items():

    def __init__(self):
        super().__init__()
        self.name = 0
        self.hp = 0
        self.mp = 0
        self.wert = 0
        self.nahrung = 0
        self.infi = 0
        self.type = "Consumable"

    def Using(self, player):
        player.hp += self.hp
        if player.hp > player.maxhp:
            player.hp = player.maxhp
        player.mp += self.mp
        if player.mp > player.maxmp:
            player.mp = player.maxmp
        player.food += self.nahrung
        if player.food > player.maxfood:
            player.food = player.maxfood
        print("Durch ", self.name, " regenerierst du", self.hp, "Leben und ", self.mp, "Mana")
        print("""Jetzt hast du 
HP: [""", player.hp, "/", player.maxhp, """]
MP: [""", player.mp, "/", player.maxmp, """]""")
        Inventory.inv.remove(self.name)


class Rüstung():

    def __init__(self):
        super().__init__()
        self.name = 0
        self.defense = 0
        self.hp = 0
        self.speed = 0
        self.wert = 0
        self.type = "Equip"
        self.infi = 0

    def Info(self):
        print("""name = """, self.name, """
Defense = """, self.defense, """
Hp Boost = """, self.hp, """
Speed Boost = """, self.speed)


class Helm(Rüstung):

    def __init__(self):
        super().__init__()

    def Unequip(self, target, player):
        player.defense -= target.defense
        player.hp -= target.hp
        player.maxhp -= target.hp
        player.speed -= target.speed
        player.head = 0

    def Equip(self, player):
        if player.head == 0:
            pass
        else:
            self.Unequip(player.head, player)
        player.head = self
        player.defense += self.defense
        player.hp += self.hp
        player.maxhp += self.hp
        player.kmh += self.speed


class Brustplatte(Rüstung):

    def __init__(self):
        super().__init__()

    def Unequip(self, target, player):
        player.defense -= target.defense
        player.hp -= target.hp
        player.maxhp -= target.hp
        player.kmh -= target.speed
        player.chest = 0

    def Equip(self, player):
        if player.chest == 0:
            pass
        else:
            self.Unequip(player.chest, player)
        player.chest = self
        player.defense += self.defense
        player.hp += self.hp
        player.maxhp += self.hp
        player.kmh += self.speed


class Hose(Rüstung):

    def __init__(self):
        super().__init__()

    def Unequip(self, target, player):
        player.defense -= target.defense
        player.hp -= target.hp
        player.maxhp -= target.hp
        player.speed -= target.speed
        player.legs = 0

    def Equip(self, player):
        if player.legs == 0:
            pass
        else:
            self.Unequip(player.legs, player)
        player.legs = self
        player.defense += self.defense
        player.hp += self.hp
        player.maxhp += self.hp
        player.kmh += self.speed


class Schuhe(Rüstung):

    def __init__(self):
        super().__init__()

    def Unequip(self, target, player):
        player.defense -= target.defense
        player.hp -= target.hp
        player.maxhp -= target.hp
        player.speed -= target.speed
        player.feet = 0

    def Equip(self, player):
        if player.feet == 0:
            pass
        else:
            self.Unequip(player.feet, player)
        player.feet = self
        player.defense += self.defense
        player.hp += self.hp
        player.maxhp += self.hp
        player.kmh += self.speed


class Sword(Weapons):

    def __init__(self):
        super().__init__()
        self.dmg = 2
        self.crit = 5
        self.name = "None"
        self.wert = 0
        self.type = "Equip"
        self.slot = "Mainhand"

    def Unequip(self, target, player):
        player.attack -= target.dmg
        player.crit -= target.crit
        player.mainhand = 0

    def Equip(self, player):
        if player.mainhand == 0:
            pass
        else:
            self.Unequip(player.mainhand, player)
        player.mainhand = self
        player.attack += self.dmg
        player.crit += self.crit

    def Info(self):
        print("""name = """, self.name, """
atk = """, self.dmg, """
crit =""", self.crit)


class Holzschwert(Sword):

    def __init__(self):
        super().__init__()
        self.name = "Holzschwert"
        self.wert = 1


class Steinschwert(Sword):

    def __init__(self):
        super().__init__()
        self.name = "Steinschwert"
        self.dmg = 3
        self.crit = 9
        self.wert = 10


class Eisenschwert(Sword):
    def __init__(self):
        super().__init__()
        self.name = "Eisenschwert"
        self.dmg = 10
        self.crit = 10
        self.wert = 50


class HealthPotion(Items):

    def __init__(self):
        super().__init__()
        self.name = "Health Potion"
        self.hp = 8
        self.mp = 1
        self.wert = 10
        self.infi = 7


class Lederharnisch(Brustplatte):

    def __init__(self):
        super().__init__()
        self.name = "Lederharnisch"
        self.defense = 4
        self.hp = 1
        self.speed = 0
        self.wert = 60


class KleineRation(Items):

    def __init__(self):
        super().__init__()
        self.name = "Kleine Ration"
        self.nahrung = 3
        self.wert = 5
        self.hp = 1


holzschwert = Holzschwert()
steinschwert = Steinschwert()
eisenschwert = Eisenschwert()
lederharnisch = Lederharnisch()
healthPotion = HealthPotion()
kleineRation = KleineRation()

items = dict()
items[holzschwert.name] = holzschwert
items[steinschwert.name] = steinschwert
items[eisenschwert.name] = eisenschwert
items[lederharnisch.name] = lederharnisch
items[healthPotion.name] = healthPotion
items[kleineRation.name] = kleineRation


