import ReisenTest



class Orte():

    def __init__(self):
        super().__init__()

        self.welt = dict()
        self.orte = list()

        self.welt[ReisenTest.hamilton.name] = ReisenTest.hamilton
        self.welt[ReisenTest.hamilton] = ReisenTest.hamilton.name
        self.orte.append("Hamilton")

        self.welt[ReisenTest.george.name] = ReisenTest.george
        self.welt[ReisenTest.george] = ReisenTest.george.name

        self.welt[ReisenTest.cave.name] = ReisenTest.cave
        self.welt[ReisenTest.cave] = ReisenTest.cave.name

orte = Orte()




