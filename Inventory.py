import Items

inv = list





def Inventory():
    print("in deinem Inventar befindet sich:",inv,)
    print("mit was möchtest du Interagieren?")
    choice = input()
    if choice in inv:
        pass
    else:
        print("dieses Item ist entweder nicht im Inventar oder wurde falsch geschrieben")
        Inventory()

