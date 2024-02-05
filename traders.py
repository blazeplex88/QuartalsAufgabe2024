import Inventory
import Items
import Player
import Skills


class Npcs():
    def __init__(self):
        super().__init__()
        self.name = 0


class Trader():

    def __init__(self):
        super().__init__()
        self.waren = list()
        self.name = "None"
        self.extramessage = ""

    def trade(self, player):
        print("dies sind meine Waren:", self.waren, "möchten sie etwas kaufen?")
        object = input()
        if object in self.waren:
            print("Dieses Objekt kostet:", Items.items[object].wert, "Silber. Sie haben momentan:", player.money, "Silber"
                  "Wollen sie es kaufen? y/n")
            self.yn = input()
            if self.yn == "y":
                if Items.items[object].wert <= player.money:
                    self.waren.remove(object)
                    player.money -= Items.items[object].wert
                    Inventory.inv.append(object)
                    print("der Handel war erfolgreich")
                    print("[Geld-", Items.items[object].wert, "]")
                    print("[", object, "ins Inventar hinzugefügt]")
                    print(self.extramessage)
                    if Items.items[object].type == "Equip":
                        print("[Möchtest du", object, "ausrüsten?]")
                        print("[y/n]")
                        self.yesno = input()
                        if self.yesno == "y":
                            Items.items[object].Equip(player)
                else:
                    print("Du bist zu arm, komm wieder wenn du einen Job oder so was gefunden hast")
            else:
                print("schade. Vieleicht gefällt ihnen ja etwas anderes?")
                self.trade(player)
            if len(self.waren) > 0:
                print("Möchten sie vlt noch etwas weiteres kaufen? [y/n]")
                self.yesno = input()
                if self.yesno == "y":
                    self.trade(player)
                else:
                    print("Och schade.")
        if object == "n":
            print("Noch einen schönen Tag.")

class Otto(Trader):
    def __init__(self):
        super().__init__()
        self.waren = [Items.eisenschwert.name]
        self.name = "Otto"
        self.extramessage = "Ich habe noch eine Karte für dich, damit du dein neues Schwert testen kannst."

class Alchemist(Trader):

    def __init__(self):
        super().__init__()
        self.waren = [Items.healthPotion.name, Items.healthPotion.name, Items.healthPotion.name, Items.healthPotion.name]
        self.name = "Alchemist"
        self.extramessage = ""

class Eric(Npcs):

    def __init__(self):
        super().__init__()
        self.name = "Eric"

    def talk(self, player):
        print("""Hallo, ich bin Eric.
Für den Preis von 60 Münzen kann ich dir eine besondere Schnittechnik für dein Schwert beibringen. Haben wir einen Deal?
[y/n]""")
        yesno = input()
        if yesno == "y":
            if player.money >= 60:
                print("Super also der Schnitt funktioniert indem du........")
                print("[Du hast den Skill {Cleave} gelernt]")
                player.skills.append(Skills.cleave.name)
                player.actions.append("Skills")
                print("Guter Deal. Tschüss")
                player.money -= 60
            else:
                print("Ich gebe dir keine Skills kostenlos. Zisch ab")
        elif yesno == "n":
            print("): warum nicht? dann halt net. Zisch ab")
        else:
            print("wie bitte?")
            self.talk(player)

class Marlon(Trader):

    def __init__(self):
        super().__init__()
        self.waren = [Items.lederharnisch.name]
        self.name = "Marlon"
        self.extramessage = "Ich geh was essen."


otto = Otto()
eric = Eric()
marlon = Marlon()
alchemist = Alchemist()

trader = dict()
trader[otto.name] = otto
trader[otto] = otto.name

trader[marlon.name] = marlon
trader[marlon] = marlon.name

trader[alchemist.name] = alchemist
trader[alchemist] = alchemist.name

npcs = dict()
npcs[eric.name] = eric
npcs[eric] = eric.name
