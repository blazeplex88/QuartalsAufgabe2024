import Items

inv = [Items.holzschwert.name, Items.steinschwert.name]






def Inventory(self,player):
    print("in deinem Inventar befindet sich:",inv,)
    print("""Waffe: [""",self.mainhand.name,"""]
zweite Hand: [""",self.offhand.name,"""]
Helm: [""",self.head.name,"""]
Brustplatte: [""",self.chest.name,"""]
Hose: [""",self.legs.name,"""]
Schuhe: [""",self.feet.name,"""]
Geld: [""",self.money,"""]""")
    print("mit was möchtest du Interagieren?")
    choice = input()
    if choice in inv:
        if Items.items[choice] == self.mainhand or Items.items[choice] == self.head or Items.items[choice] == self.chest or Items.items[choice] == self.legs or Items.items[choice] == self.feet:
            print("Willst du es abrüsten oder untersuchen?")
            action = input()
            if action == "abrüsten":
                Items.items[choice].Unequip(self.mainhand, self)

            elif action == "untersuchen":
                Items.items[choice].Info()
            else:
                print("Etwas ist fehlgeschlagen probiere es erneut")
                Inventory()
        elif Items.items[choice].type == "Consumable":
            Items.items[choice].Using(player)
        else:
            print("Willst du es ausrüsten oder untersuchen")
            action = input()
            if action == "ausrüsten":
                Items.items[choice].Equip(self)
            elif action == "untersuchen":
                Items.items[choice].Info()
            else:
                print("Etwas ist fehlgeschlagen probiere es erneut")
                Inventory()
    else:
        print("dieses Item ist entweder nicht im Inventar oder wurde falsch geschrieben")

