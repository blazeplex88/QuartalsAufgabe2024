import Inventory
import Items
import Player


class Trader():

    def __init__(self):
        super().__init__()
        self.waren = list()
        self.name = "None"


    def trade(self):
        print("dies sind meine Waren:", self.waren,"möchten sie etwas kaufen?")
        object = input()
        if object in self.waren:
            print("Dieses Objekt kostet:",Items.items[object].wert,"Sie haben momentan:", Player.Player.money,"Wollen sie es kaufen? y/n")
            self.yn = input()
            if self.yn == "y":
                if Items.items[object].wert <= Player.Player.money:
                    self.waren.remove(object)
                    Player.Player.money -= Items.items[object].wert
                    Inventory.inv.append(object)
                    print("der Handel war erfolgreich")
                    print("[Geld-",Items.items[object].wert,"]")
                    print("[",object,"ins Inventar hinzugefügt]")
                else:
                    print("Du bist zu arm, komm wieder wenn du einen Job oder so was gefunden hast")
            else:
                print("schade. Vieleicht gefällt ihnen ja etwas anderes?")
                self.trade()
        if object == "n":
            print("Noch einen schönen Tag.")


class Otto(Trader):
    def __init__(self):
        super().__init__()
        self.waren = [Items.eisenschwert.name]
        self.name = "Otto"



otto = Otto()

trader = dict()
trader[otto.name] = otto