import Stadt


class Zero():
    name = "None"
    dmg = 0
    crit = 0
    defense = 0
    hp = 0
    speed = 0

class Player:
    #Stats
    level = 1
    exp = 0
    expneeded = 10
    skillpoints = 0
    kmh = 6
    attack = 1
    hp = 10
    maxhp = 10
    mp = 10
    maxmp = 10
    defense = 5
    truedefense = 0
    crit = 10
    food = 30
    maxfood = 30
    foodused = 0
    ini = 5
    actions = ["attack", "defend"]
    exactions = ["attack"]
    skills = list()

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
    safespot = 0
    waves = 1

    def stats(self):
        print("""Du befindest dich in""",self.location.name,"""
[""",self.money,"""] münzen
Level: [""",self.level,"""]
Exp: [""",self.exp,"""/""",self.expneeded,"""
Defense: [""",self.defense,"""
___________________________________________
Speed: [""",self.kmh,"""] kmh
Hp: [""",self.hp,"""/""",self.maxhp,"""]
Mp: [""",self.mp,"""/""",self.maxmp,"""]
Strength: [""",self.attack,"""]
Critchance: [""",self.crit,"""]""")
        if self.food <= 10:
            print("Du bist sehr hungrig")
        elif self.food <= 20:
            print("Du hast Hunger")
        elif self.food <= 30:
            print("Ich bin satt")
        elif self.food > 30:
            print("Du bist komplett voll")
        if self.skillpoints > 0:
            print("Welchen Stat möchtest du verbessern?")
            skill = input()
            if skill == "Speed":
                self.kmh += 1
                self.skillpoints -= 1
            elif skill == "Hp":
                self.maxhp += 1
                self.hp += 1
                self.skillpoints -= 1
            elif skill == "Mp":
                self.maxmp += 1
                self.mp += 1
                self.skillpoints -= 1
            elif skill == "Strength":
                self.attack += 1
                self.skillpoints -= 1
            elif skill == "Crit":
                self.crit += 1
                self.skillpoints -= 1
            self.stats()


    def Equip(self):
        print("""
Waffe: [""",self.mainhand.name,"""]
zweite Hand: [""",self.offhand.name,"""]
Helm: [""",self.head.name,"""]
Brustplatte: [""",self.chest.name,"""]
Hose: [""",self.legs.name,"""]
Schuhe: [""",self.feet.name,"""]""")
    def death(self,player):
        print("Du bist gestorben. Loser")
        player.location = player.safespot
        print("Du hast 50% deiner Münzen verloren und bist wieder in deinem letzten besuchten Safespot aufgewacht.")
        player.money /= 2
        player.hp = player.maxhp
