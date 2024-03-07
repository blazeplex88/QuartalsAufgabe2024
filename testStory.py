import Inventory
import Quests
import ReisenTest
import Stadt
import gegner
import traders
import Items


def Progress(player):
    if ReisenTest.hutte.door.Doorunlock:
        player.location.options.append("travel")
        player.location.discoveries.remove("Tür")
        ReisenTest.hutte.door.Doorunlock = False
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
        print("")
        gegner.goblin.fight(player)
        player.cavefirst = False
        print("""
Unbekannter Abenteurer: "Danke das du mich gerettet hast, im Moment kann ich dir leider nicht viel geben. Das einzige
das ich dir anbieten könnte wäre meine Quest." Er drückt dir eine Quest in die Hand und rennt dann weg.""")
        Quests.goblin1.accept_quest()
    if Quests.goblin1.targethave == Quests.goblin1.targetneed:
        ReisenTest.hamilton.Gilde.gobQuestComp = True
    if player.location.name == "George" and "Trainings Camp" not in Stadt.orte.orte and player.georgeKnightAccept:
        Stadt.orte.orte.append("Trainings Camp")
    else:
        if player.location.name == "Trainings Camp":
            pass
        else:
            if "Trainings Camp" in Stadt.orte.orte:
                Stadt.orte.orte.remove("Trainings Camp")
    if player.location.name == "George" and player.georgefirst:
        print("""Bevor du die Stadt betreten kannst wirst du von einer Wache aufgefordert ihr alle deine Sachen zu 
        überlassen, sonst würde sie dich töten. Da du zuvor gesehen hattest wie andere Personen von anderen Wachen 
        ohne solche Aufforderungen durchgelassen wurden, wehrst du dich gegen die Wache""")
        player.georgefirst = False
        gegner.ritter.fight(player)
        if player.location.name == "George":
            print("""Nachdem du die Wache besiegt hast, kommt ein Vorgesetzter der Wache dazu.
            General: "Danke das du diesen Verbrecher für uns ausgeschaltet hast, vielleicht möchtest du ja dem Heer
            beitreten?" [y/n]""")

            def ynloop():
                yn = input()
                if yn == "y":
                    print("""General: "Super, Leute wie dich können wir immer gebrauchen. Du musst allerdings zuvor durch das Trainingslager
                          Dort wissen aber alle wie man zu mindestens simple Skills nutzt. Damit du keinen Nachteil hast
                          werde ich dir auch einen beibringen". 
                          Der General bringt dir den Skill [Cleave] bei.""")
                    player.skills.append("Cleave")
                    player.actions.append("Skills")
                    player.exactions.append("Skills")
                    player.georgeKnightAccept = True
                    print("[Du kannst jetzt im Kampf aktive Skills nutzen]"
                          "[Der Skill Cleave wurde freigeschaltet]"
                          "[Du kannst jetzt in Trainingslager]")
                elif yn == "n":
                    print("""General: "Sehr Schade, ich hätte dich liebend gerne zu einem Großartigen Ritter ausgebildet."
                    [Weitere Teile dieser Storyline sind momentan in Arbeit]""")
                else:
                    ynloop()

            ynloop()
    if player.location.name == "Trainings Camp" and player.georgeTrainfirst:
        print("""Schon bevor du das Trainingscamp betrittst kannst du hören dass dort viele Soldaten dort trainieren.
        Kurz nachdem du durch das große eingangstor des Lagers trittst wirst du von einem der Trainer begrüßt:
        "Hi du musst der Rekrut sein von dem uns der General erzählt hat,""", player.name, """ richtig? Komm einfach rein
         wir sind immer froh neue Rekruten zu haben, wie wärs wenn du mir direkt einmal zeigst was du so kannst."""
              )
        gegner.unbeatableTrainer.fight(player)
        print("""Trainer: "Du bist hier definitiv richtig. Der General hat ein gutes Auge für sowas. Momentan gibt es Konflikt
        im Westen, sobald du stark genug bist wirst auch du dort hingeschickt werden. Aber erstmal müssen wir uns um deine
        Ausrüstung kümmern." 
        Der Trainer gibt dir ein Kurzschwert und ein Schild, sowie Rüstung""")
        Inventory.inv.append("Vergoldeter Schild", "Vergoldetes Schwert", "Vergoldete Brustplatte")
        print("[Wenn du Level 10 erreichst kannst du die Geschichte fortsetzen]")
