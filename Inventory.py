import Items

inv = list()






def Inventory(self, player):
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
        if Items.items[choice] == self.mainhand or Items.items[choice] == self.offhand or Items.items[choice] == self.head or Items.items[choice] == self.chest or Items.items[choice] == self.legs or Items.items[choice] == self.feet:
            print("Willst du es abrüsten oder untersuchen?")
            action = input()
            if action == "abrüsten":
                Items.items[choice].Unequip(self.mainhand, self)
            elif action == "untersuchen":
                Items.items[choice].Info()
            else:
                print("Etwas ist fehlgeschlagen probiere es erneut")
                Inventory(self, player)
        elif Items.items[choice].type == "Consumable":
            Items.items[choice].Using(player)
        elif Items.items[choice].type == "Useless":
            print("willst du es untersuchen?")
            yn = input()
            if yn == "y":
                Items.items[choice].Info()
        elif Items.items[choice].type == "weapon":
            print("Willst du es ausrüsten oder untersuchen")
            action = input()
            if action == "ausrüsten":
                Items.items[choice].Equip(self)
            elif action == "untersuchen":
                Items.items[choice].Info()
            else:
                print("Etwas ist fehlgeschlagen probiere es erneut")
                Inventory(self, player)
    else:
        print("dieses Item ist entweder nicht im Inventar oder wurde falsch geschrieben")

