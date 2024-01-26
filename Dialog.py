import Inventory
import Items
import Player
import ReisenTest
import Stadt


class Mydialog():
    def __init__(self):
        self.player = Player.Player()
        self.player.location = ReisenTest.hamilton


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
            #if chosen == "Inventory":
                #Inventory.Inventory()
        self.Dialog()


dia = Mydialog()
dia.Dialog()

