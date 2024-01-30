
class Zero():
    name = "None"

class Player:
    #Stats
    kmh = 6
    level = 1
    attack = 1
    hp = 10
    maxhp = 10
    crit = 10

    #Equipment
    mainhand = Zero
    offhand = Zero
    head = Zero
    chest = Zero
    legs = Zero
    feet = Zero

    #general info
    location = 0
    money = 100

    def stats(self):
        print("""Du befindest dich in""", self.location,"""
[""",self.money,"""] münzen
Level: [""",self.level,"""]
Speed: [""",self.kmh,"""] kmh
Hp: [""",self.hp,"""/""",self.maxhp,"""]
Strength: [""",self.attack,"""]
Critchance: [""",self.crit,"""]
Waffe: [""",Player.waffe.name,"""]
zweite Hand: [""",Player.offhand.name,"""]
Helm: [""",Player.head.name,"""]
Brustplatte: [""",Player.chest.name,"""]
Hose: [""",Player.legs.name,"""]
Schuhe: [""",Player.feet.name,"""]""")

