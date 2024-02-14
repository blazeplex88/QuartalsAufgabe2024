
import Inventory
import ReisenTest
import Stadt
import gegner
import traders
import Items

hamiltonfirst = True





def Progress(player):
    if player.level >= 2 and ReisenTest.george.name not in Stadt.orte.orte:
        Stadt.orte.orte.append(ReisenTest.george.name)
        print("Du kannst jetzt nach George Reisen")
        print("Die Goblins in den Höhlen haben sich Unterstützung geholt")
        ReisenTest.cave.gegner.append(gegner.goblin)
        ReisenTest.cave.gegner.append(gegner.goblin)
        ReisenTest.cave.gegner.append(gegner.orc)
    if player.location.name == "Hamilton":
        if hamiltonfirst:
            player.safespot = player.location
    if player.exp >= player.expneeded:
        player.level += 1
        player.exp -= player.expneeded
        player.expneeded *= 2
        print("Du bist ein Level aufgestiegen")
        print("öffne den Statscreen um deine Skillpunkte zu verteilen")
        player.skillpoints += 3
    if "Eisenschwert" in Inventory.inv and "Cave" not in Stadt.orte.orte:

        print("Du kannst jetzt zur Cave reisen")
        Stadt.orte.orte.append("Cave")
        loop = 5
        traders.otto.extramessage = ""
        print("Otto hat neue Waren")
        while loop > 0:
            traders.otto.waren.append(Items.kleineRation.name)
            loop -= 1
    if "Lederharnisch" in Inventory.inv and "Fort" not in Stadt.orte.orte:
        print("In der Lederrüstung findest du einen Schlüssel für eine Burg")
        print("Du kannst jetzt zu Fort reisen")
        Stadt.orte.orte.append("Fort")

