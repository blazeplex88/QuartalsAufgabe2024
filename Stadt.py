import ReisenTest


welt = dict()
orte = list()

welt[ReisenTest.hamilton.name] = ReisenTest.hamilton
welt[ReisenTest.hamilton] = ReisenTest.hamilton.name
orte.append("Hamilton")

welt[ReisenTest.george.name] = ReisenTest.george
welt[ReisenTest.george] = ReisenTest.george.name
orte.append("George")

print(welt[ReisenTest.hamilton])


