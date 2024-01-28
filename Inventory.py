import Items
from Player import Player

inv = ["holzschwert", "steinschwert"]






def Inventory():
    print("in deinem Inventar befindet sich:",inv,)
    print("mit was möchtest du Interagieren?")
    choice = input()
    if choice in inv:
        if Items.items[choice] == Player.waffe:
            print("Willst du es abrüsten oder untersuchen?")
            action = input()
            if action == "abrüsten":
                Items.items[choice].Unequip(Player.waffe)

            elif action == "untersuchen":
                Items.items[choice].Info()
            else:
                print("Etwas ist fehlgeschlagen probiere es erneut")
                Inventory()
        else:
            print("Willst du es ausrüsten oder untersuchen")
            action = input()
            if action == "ausrüsten":
                Items.items[choice].Equip()
            elif action == "untersuchen":
                Items.items[choice].Info()
            else:
                print("Etwas ist fehlgeschlagen probiere es erneut")
                Inventory()
    else:
        print("dieses Item ist entweder nicht im Inventar oder wurde falsch geschrieben")
        Inventory()

