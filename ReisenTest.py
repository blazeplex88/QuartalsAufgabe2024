from math import sqrt

import Inventory
import Items
# hier importieren wir die funktion des Wurzelziehens aus der Mathe datei die in pycharm mit installiert ist

import Player
import Quests
import Stadt
import gegner
import traders


# hier importieren wir alle KLassen, Funktionen und Variablen aus der datei Player welche ich erstellt habe


class Loc:
    # wir definieren die Klasse Loc(Location)
    def __init__(self):
        # durch def __init__(self) legen wir fest was in den Instanzen benutzt wird

        self.bandits = 0
        self.name = "None"
        self.x = 0
        self.y = 0
        self.z = 0
        self.options = [0]
        self.traders = list()
        self.gegner = list()
        self.npcs = list()
        self.discoveries = list()
        self.waves = 1
        self.boss = 0
        self.searchdict = dict()
        # die Variablen der Instanzen und dieser Klasse

    def travel(self, dest, player):

        # Eine Funktion namens travel wir erstellt mit der ausführenden Instanz als Self und eine andere Instans als dest(destination)
        dista = dest.x - self.x
        # die Differenz zwischen den X Wert der ausführenden Instanz und der dest Instanz

        distb = dest.y - self.y
        # die Differenz zwischen dem Y wert der ausführenden Instanz und der dest Instanz

        distc = dista * dista + distb * distb
        sdistc = sqrt(distc)
        # Satz des Pythagoras

        truedist = 0.2 * (dest.z - self.z) + sdistc
        # Meine eigene Formel für die Höhe

        if truedist == (0):
            truedist = sdistc
        # Wenn das Ergebnis von der vorherigen Gleichung 0 ist wird truedist zur wurzel von distc gesetzt

        if truedist < 0:
            truedist *= (-1)
        # wenn truedist negativ ist wird es positiv gemacht

        tspent = truedist / (player.kmh * 24)
        # die Entfernung wird durch die distanz die der Spieler an einem Tag zurücklegt geteilt

        if tspent < 1:
            # Sollte das ergenis von eben kleiner als 1 sein also braucht man weniger als einen Tag wird folgendes ausgeführt

            tspent = truedist / player.kmh
            # Die Entfernung wird durch die Distanz die der Spieler in einer Stunde zurücklegt geteilt

            tkind = "Stunden"
            # Diese Variable wird zu "STunden" gesetzt

            if tspent < 1:
                # Sollte der Spieler dafür weniger als eine Stunde brauchen machen wir das gleiche mit der Distanz für Minuten getan
                tspent = truedist / (player.kmh / 60)
                tkind = "Minuten"
                # und tkind wird zu Minuten gesetzt
        else:
            tkind = "Tage"
            # Sollte die erste der Beiden ifs nicht erfüllt sein wird tkind zu Tage gesetzt

        print("Du reist von", self.name, "nach", dest.name)
        # Die Namen der beiden Orte werden angezeigt in diesem Text

        print("Die Reise dauert etwa", round(tspent, 1), tkind)
        if tkind == "Stunden" and tspent >= 12:
            self.bandits = round((tspent - 12) / 24) + 1
        elif tkind == "Tage":
            self.bandits = round(tspent)
        if self.bandits > 0:
            print("Auf deiner Reise wirst du Nachts von Banditen überfallen")
        while self.bandits > 0:
            gegner.bandit.fight(player)
            player.food -= 6
            print("Am nächsten Morgen benötigst du Nahrung.")
            self.loop = True
            while self.loop:
                if player.food <= 10:
                    print("Du bist sehr hungrig")
                elif player.food <= 20:
                    print("Du hast Hunger")
                elif player.food <= 30:
                    print("Du bist satt")
                elif player.food > 30:
                    print("Du bist komplett voll")
                print("Was aus deinem Inventar möchtest du Essen? [option/n]")
                print(Inventory.inv)
                self.chosen = input()
                if self.chosen == "n":
                    self.loop = False
                elif Items.items[self.chosen].type == "Consumable":
                    print("""Dieses Objekt gibt dir:
""", Items.items[self.chosen].nahrung, """ Nahrung
""", Items.items[self.chosen].hp, """ Hp
""", Items.items[self.chosen].mp, """ Mp
willst du es verbrauchen? [y/n]""")
                    self.yesno = input()
                    if self.yesno == "y":
                        Items.items[self.chosen].Using(player)
                        self.loop = False
                    else:
                        self.loop = True
                else:
                    self.loop = True
            if self.bandits < 1:
                self.bandits -= self.bandits
            else:
                self.bandits -= 1

        # Wie lange die Reise dauert, wird durch ein gerundetes Ergebnis und das vorher bestimmte tkind dargestellt

    def Search(self, player):
        print("""Hier gibt es:
""", self.discoveries, """
Was möchtest du untersuchen?""")
        search = input()
        if search in self.discoveries:
            self.searchdict[search].searching(self)
        else:
            print("Das geht hier nicht")


class Hamilton(Loc):
    # Eine Instanz der Loc Klasse namens Hamilton wird erstellt
    class Gilde:

        def searching(self):
            print("""Du stehst vor einem großen Gebäude das in einem wesentlich besseren Zustand ist als der Rest der "
Stadt zu sein scheint.
Um dieses Gebäude versammeln sich viele verschiedene Personen.
Möchtest du es betreten? [y/n]""")
            yn = input()
            if yn == "y":
                print("""Du betrittst die Gilde
Innerhalb befinden sich noch mehr Menschen von denen viele Waffen besitzen, welche um einiges 
wertvoller aussehen als deine eigene.
Eine Große Menschenmenge hat sich um eine Art tafel gebildet. Du drängst dich durch die menge 
und siehst das eine große Anzahl an zu erledigenden Aufgaben an der Tafel hängen. Du überlegst
das die meisten vermutlich zu schwer für dein momentanes können ist und wählst die am 
einfachsten aussehende Aufgabe""")
                print(Quests.ratten.name)
                Quests.ratten.accept_quest()
                print("Auf der Rückseite findest du eine Karte zum Jagdort")
                print("Du kannst jetzt zur Verseuchten Wiese reisen")
                Stadt.orte.orte.append("Wiese")
                hamilton.discoveries.remove("Gilde")

    def __init__(self):
        super().__init__()
        self.name = "Hamilton"
        self.options = ["stats", "travel", "Inventory", "trade", "search", "rest"]
        self.traders = [traders.otto.name, traders.alchemist.name]
        self.discoveries = ["Gilde"]
        self.searchdict["Gilde"] = self.Gilde

        # Variablen bearbeitet


class George(Loc):
    # Eine weitere Instanz erstellt

    def __init__(self):
        super().__init__()
        self.name = "George"
        self.x = 60
        self.y = 60
        self.options = ["stats", "travel", "Inventory", "talk", "trade"]
        self.npcs = [traders.eric.name]
        self.traders = [traders.marlon.name]


class Cave(Loc):
    def __init__(self):
        super().__init__()
        self.name = "Cave"
        self.x = 3
        self.y = -1
        self.z = -0.5
        self.options = ["travel", "Inventory", "explore"]
        self.gegner = [gegner.goblin]


class Fort(Loc):

    def __init__(self):
        super().__init__()
        self.name = "Fort"
        self.x = 70
        self.y = 74
        self.z = 2
        self.boss = gegner.king
        self.waves = 4
        self.options = ["travel", "Inventory", "explore"]
        self.gegner = [gegner.ritter]


class Hutte(Loc):
    class Tisch:

        def searching(self):
            if "Hamilton" not in Stadt.orte.orte:
                print("Auf dem Tisch liegt eine Karte. Möchtest du sie aufheben?")
                yn = input()
                if yn == "y":
                    print(
                        "Die Karte zeigt die Nahe umgebung und du bemerkst das es wohl eine Stadt in deiner Nähe gibt.")
                    Stadt.orte.orte.append("Hamilton")

    class Truhe:
        def searching(self):
            if "Schlüssel" in Inventory.inv:
                print("Du hast diese Truhe bereits komplett geleert.")
            else:
                print("In einer Ecke der Hütte findest du eine Truhe. Möchtest du versuchen sie zu öffnen?")
                yn = input()
                if yn == "y":
                    print("In der Truhe liegt ein altes rostiges Schwert und ein Schlüssel. Du hebst beides auf.")
                    Inventory.inv.append("Altes Schwert")
                    Inventory.inv.append("Schlüssel")


    class Door:
        def __init__(self):
            self.Doorunlock = None

        def searching(self):
            if "Schlüssel" in Inventory.inv:
                print("Möchtest du die Tür aufschließen? [y/n]")
                yn = input()
                if yn == "y":
                    self.Doorunlock = True
            else:
                print("Die Tür ist abgeschlossen.")

    def __init__(self):
        super().__init__()
        self.name = "Hütte"
        self.x = -20
        self.y = -30
        self.z = 1
        self.Doorunlock = False
        self.waves = 0
        self.options = ["Inventory", "search"]
        self.discoveries = ["Tisch", "Truhe", "Tür"]
        self.searchdict["Tür"] = self.Door
        self.searchdict["Truhe"] = self.Truhe
        self.searchdict["Tisch"] = self.Tisch

class Wiese(Loc):

    def __init__(self):
        super().__init__()
        self.name = "Wiese"
        self.x = 3
        self.y = -2
        self.z = 0
        self.options = ["travel", "Inventory", "explore"]
        self.gegner = [gegner.ratte]


cave = Cave()
hamilton = Hamilton()
george = George()
fort = Fort()
hutte = Hutte()
wiese = Wiese()
# Instanzen der beiden soeben erstellten Klassen


# hamilton.travel(george)
# Die Travel funktion wird im Namen von hamilton ausgeführt und als dest wird george festgelegt
