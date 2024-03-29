import random

import Skills


class Gegner():

    def __init__(self):
        self.lvl = 0
        self.name = "None"
        self.hp = 0
        self.maxhp = 0
        self.attack = 0
        self.ini = 0
        self.defense = 2
        self.truedefense = 0
        self.actions = ["attack", "defend"]
        self.skills = [Skills.cleave]
        self.dialog = list()
        self.endline = ""
        self.exp = 5
        self.wert = 5

    def fight(self, player):
        player.foodused = -0.2
        self.lvl = player.level
        if self.ini <= player.ini:
            self.pturn(player)
        elif self.ini > player.ini:
            self.eturn(player)
        player.food -= player.foodused

    def pturn(self, player):
        player.foodused += 0.2
        if self.hp < 1:
            self.hp = self.maxhp
            player.waves += 1
            if player.location.waves > player.waves:
                if player.waves == player.location.waves - 1:
                    player.location.boss.fight(player)
                else:
                    enemy = random.choice(player.location.gegner)
                    print("Der Gegner hatte Verstärkung. Herbeikommt", enemy.name, "Er/sie/es greift dich an")
                    enemy.fight(player)
            elif player.waves >= player.location.waves:
                player.waves = 1
                self.win(player)
        elif player.hp < 1:
            player.death(player)
        else:
            print("Du hast", player.hp, "/", player.maxhp, "hp")
            print("Du kannst", player.actions)
            self.choice = input()
            if self.choice in player.actions:
                if self.choice == "attack":
                    self.damage = (player.attack - self.truedefense)
                    a = random.randint(1, 100)
                    if a <= player.crit:
                        self.damage *= 2
                        print("Kritischer Treffer")
                    if self.damage < 0:
                        self.damage = 0
                    self.hp -= self.damage
                    print("Du hast dem", self.name, ",", self.damage, "Schaden zugefügt.", self.hp, "/", self.maxhp,
                          "übrig.")
                    self.truedefense = 0
                    self.eturn(player)
                elif self.choice == "defend":
                    player.truedefense = player.defense
                    print("Du verteidigst dich")
                    self.eturn(player)
                elif self.choice == "Skills":
                    print("Welchen Skill willst du nutzen? Du hast:", player.skills)
                    skill = input()
                    if skill in player.skills:
                        Skills.usages[skill].Use(self, player)
                        self.truedefense = 0
                        self.eturn(player)
            else:
                print("Das geht nicht")
                self.pturn(player)

    def pexturn(self, player):
        player.foodused += 0.2
        if self.hp < 1:
            self.win(player)
        elif player.hp < 1:
            player.death(player)
        else:
            print("Extra Zug")
            print("Du kannst", player.actions)
            self.choice = input()
            if self.choice in player.actions:
                if self.choice == "attack":
                    self.damage = (player.attack - self.truedefense)
                    a = random.randint(1, 100)
                    if a <= player.crit:
                        self.damage *= 2
                        print("Kritischer Treffer")
                    if self.damage < 0:
                        self.damage = 0
                    self.hp -= self.damage
                    print("Du hast dem", self.name, ",", self.damage, "Schaden zugefügt.", self.hp, "/", self.maxhp,
                          "übrig.")
                    self.truedefense = 0
                elif self.choice == "defend":
                    player.truedefense = player.defense
                    print("Du verteidigst dich")
                    self.eturn(player)
                elif self.choice == "Skills":
                    print("Welchen Skill willst du nutzen? Du hast:", player.skills)
                    skill = input()
                    if skill in player.skills:
                        Skills.usages[skill].Use(self, player)
                        self.truedefense = 0
                        self.eturn(player)
            else:
                print("Das geht nicht")
                self.pturn(player)

    def eturn(self, player):
        if self.hp < 1:
            player.waves += 1
            self.hp = self.maxhp
            if player.location.waves > player.waves:
                if player.waves == player.location.waves - 1:
                    print("Der Boss erscheint. ", player.location.boss.name, " schaut auf dich herab")
                    player.location.boss.fight(player)
                else:
                    enemy = random.choice(player.location.gegner)
                    print("Der Gegner hatte Verstärkung. Herbeikommt", enemy.name, "Er/sie/es greift dich an")
                    enemy.fight(player)
            elif player.waves >= player.location.waves:
                player.waves = 1
                self.win(player)
        elif player.hp < 1:
            player.death(player)
        else:
            self.act = random.choice(self.actions)
            if self.act == "attack":
                self.damage = (self.attack - player.truedefense)
                if self.damage <= 0:
                    self.damage = 0
                    print("Der Gegner greift dich an.")
                    print("Du hast den Angriff erfolgreich abgewehrt")
                    print("Der Gegner ist nun verwundbar")
                    player.truedefense = 0
                    self.pexturn(player)
                    player.foodused -= 0.2
                else:
                    player.hp -= self.damage
                    print("Der", self.name, "greift dich für", self.damage, "an. Dir verbleiben noch", player.hp, "/",
                          player.maxhp, "hp")
                self.truedefense = 0
                self.pturn(player)
            elif self.act == "defend":
                self.truedefense = self.defense
                print("Der gegner verteidigt sich")
                player.truedefense = 0
                self.pturn(player)
            elif self.act == "skill":
                random.choice(self.skills).Use(player, self)
                self.pturn(player)
            elif self.act == "talk":
                text = random.choice(self.dialog)
                print(text)
                self.actions.append("end")
            elif self.act == "end":
                print(self.endline)
                self.win(player)
        player.truedefense = 0

    def win(self, player):
        player.exp += self.exp
        player.money += self.wert
        print("Du hast gewonnen")
        print("[Du erhältst", self.exp, "Erfahrungspunkte]")
        print("[Du erhältst", self.wert, "Münzen]")
        player.enemiesKilled.append(self.name)
        self.hp = self.maxhp


class Goblin(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.lvl = 1
        self.hp = 15 + self.lvl * 2
        self.maxhp = 15 + self.lvl * 2
        self.attack = 1 + self.lvl * 2
        self.exp = 4 + self.lvl
        self.wert = 4 + self.lvl


class Orc(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.lvl = 1
        self.hp = 100 + self.lvl * 2
        self.maxhp = 100 + self.lvl * 2
        self.attack = 5 + self.lvl * 2
        self.exp = 40 + self.lvl
        self.wert = 50 + self.lvl


class Bandit(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Bandit"
        self.hp = 40 + self.lvl * 2
        self.maxhp = 40 + self.lvl * 2
        self.attack = 5 + self.lvl * 2
        self.exp = 20 + self.lvl
        self.wert = 40 + self.lvl


class Ratte(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Ratte"
        self.hp = 5 + self.lvl * 2
        self.maxhp = 5 + self.lvl * 2
        self.attack = 2 + self.lvl * 2
        self.exp = 2 + self.lvl
        self.wert = 3 + self.lvl


class Ritter(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Ritter"
        self.hp = 45 + self.lvl * 2
        self.defense = 15 + self.lvl * 2
        self.maxhp = 45 + self.lvl * 2
        self.attack = 7 + self.lvl * 2
        self.exp = 25 + self.lvl
        self.wert = 50 + self.lvl


class King(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "König"
        self.hp = 70 + self.lvl * 2
        self.defense = 17 + self.lvl * 2
        self.maxhp = 70 + self.lvl * 2
        self.attack = 9 + self.lvl * 2
        self.exp = 25 + self.lvl
        self.wert = 50 + self.lvl


class RitterRekrut(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Rekrut"
        self.maxhp = random.randint(30, 50) + self.lvl * 2
        self.hp = self.maxhp
        self.defense = random.randint(3, 17) + self.lvl * 2
        self.attack = random.randint(5, 9) + self.lvl * 2
        self.ini = random.randint(0, 6)
        self.maxmp = random.randint(10, 20) + self.lvl
        self.mp = self.maxmp
        self.exp = 50 + self.lvl
        self.wert = 5 + self.lvl
        self.actions = ["skill", "attack", "defense", "attack", "defense"]


class UnbeatableTrainer(Gegner):

    def __init__(self):
        super().__init__()
        self.name = "Trainer Micheal"
        self.maxhp = 200
        self.hp = self.maxhp
        self.truedefense = 99999
        self.actions = ["talk"]
        self.dialog = ["Das sieht doch schon gut aus", "Immer weiter so", "Guter Versuch"]
        self.endline = "Du bist perfekt geeignet für unsere Truppe, du bist dabei."


goblin = Goblin()
orc = Orc()
bandit = Bandit()
ritter = Ritter()
king = King()
ratte = Ratte()
ritterRekrut = RitterRekrut()
unbeatableTrainer = UnbeatableTrainer()
