
class Weapons():

    def __init__(self):
        self.dmg = 0
        self.crit = 0


class Sword(Weapons):

    def __init__(self):
        super().__init__()
        self.dmg = 2
        self.crit = 5

class Holzschwert(Sword):

    def __init__(self):
        super().__init__()
        self.name = "Holzschwert"

holzschwert = Holzschwert()




items = dict()
items[holzschwert.name] = holzschwert