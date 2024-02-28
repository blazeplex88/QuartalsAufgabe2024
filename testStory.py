
import Inventory
import Quests
import ReisenTest
import Stadt
import gegner
import traders
import Items






def Progress(player):
    if ReisenTest.hutte.Doorunlock:
        player.location.options.append("travel")
        player.location.discoveries.remove("Tür")
        ReisenTest.hutte.Doorunlock = False
    if player.location.name == "Hamilton":
        if player.hamiltonfirst:
            player.safespot = player.location
            player.hamiltonfirst = False
    if player.exp >= player.expneeded:
        player.level += 1
        player.exp -= player.expneeded
        player.expneeded *= 2
        print("Du bist ein Level aufgestiegen")
        print("öffne den Statscreen um deine Skillpunkte zu verteilen")
        player.skillpoints += 3
    if "Eisenschwert" in Inventory.inv and player.ironswordgot:

        print("Du kannst jetzt zur Cave reisen")
        Stadt.orte.orte.append("Cave")
        loop = 5
        traders.otto.extramessage = ""
        print("Otto hat neue Waren")
        while loop > 0:
            traders.otto.waren.append(Items.kleineRation.name)
            loop -= 1
        player.ironswordgot = False

    if player.location.name == "Cave" and player.cavefirst:
        print("Als du die Höhle betritst siehst du wie ein anderer Abenteurer von einem Goblin angegriffen wird.")
        print("Der Abenteurer sieht dich und bietet dir eine Belohnung an wenn du ihn rettest.")
        print("Schnell schreitest du zur Tat")
        gegner.goblin.fight(player)
        player.cavefirst = False
        print("""Unbekannter Abenteurer: "Danke das du mich gerettet hast, im Moment kann ich dir leider nicht viel geben. Das einzige
das ich dir anbieten könnte wäre meine Quest." Er drückt dir eine Quest in die Hand und rennt dann weg.""")
        Quests.goblin1.accept_quest()
