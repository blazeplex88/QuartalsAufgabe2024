import Inventory
import Items
import Player
import ReisenTest
import Stadt
import traders


class Mydialog():
    def __init__(self):
        self.player = Player.Player()
        self.player.location = ReisenTest.hamilton

        Player.Player.waffe = Items.holzschwert

    def Dialog(self):
        print("""
-----------------------
du befindest dich hier:""",self.player.location.name,"""
Was willst du nun tuen?
du kannst:
""",self.player.location.options,"""""")
        chosen = input()
        if chosen in self.player.location.options:
            if chosen == "travel":
                print("Wo willst du hin reisen? Du kannst zu:",Stadt.orte,"")
                dest = input()
                self.player.location.travel(Stadt.welt[dest])
                self.player.location = Stadt.welt[dest]
            if chosen == "Inventory":
                Inventory.Inventory()
            if chosen == "trade":
                print("In dieser Stadt gibt es die Händler:", self.player.location.traders,"mit wem möchtest du handeln")
                self.choice = input()
                if self.choice in self.player.location.traders:
                    traders.trader[self.choice].trade()
                elif self.choice == "nein":
                    self.Dialog()
                else:
                    print("etwas ist fehlgeschlagen. Bitte probiere es erneut")
        self.Dialog()


dia = Mydialog()
dia.Dialog()

