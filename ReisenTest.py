from math import sqrt
# hier importieren wir die funktion des Wurzelziehens aus der Mathe datei die in pycharm mit installiert ist

import Player
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
            if self.bandits < 1:
                self.bandits -= self.bandits
            else:
                self.bandits -= 1
        # Wie lange die Reise dauert, wird durch ein gerundetes Ergebnis und das vorher bestimmte tkind dargestellt


class Hamilton(Loc):
    # Eine Instanz der Loc Klasse namens Hamilton wird erstellt

    def __init__(self):
        super().__init__()
        self.name = "Hamilton"
        self.options = ["stats", "travel", "Inventory", "trade"]
        self.traders = [traders.otto.name, traders.alchemist.name]

        # Variablen bearbeitet


class George(Loc):
    # Eine weitere Instanz erstellt

    def __init__(self):
        super().__init__()
        self.name = "George"
        self.x = 60
        self.y = 60
        self.options = ["travel", "Inventory", "talk", "trade"]
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


cave = Cave()
hamilton = Hamilton()
george = George()
# Instanzen der Beiden soeben erstellten Klassen


# hamilton.travel(george)
# Die Travel funktion wird im Namen von hamilton ausgeführt und als dest wird george festgelegt
