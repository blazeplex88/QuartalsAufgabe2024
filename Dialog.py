import random

import Inventory
import Items
import Player
import Quests
import ReisenTest
import Stadt
import testStory

import traders


class Mydialog():
    def __init__(self):
        self.player = Player.Player
        self.player.location = ReisenTest.hutte

    def Dialog(self):
        print("[Enter] um fortzufahren")
        enter = input()
        for x in Quests.quests:
            x.check_quest(self.player)
        self.player.enemiesKilled.clear()
        print("____________________________________________")
        testStory.Progress(self.player)
        print("""
du befindest dich hier:""",self.player.location.name,"""
Was willst du nun tun?
du kannst:
""",self.player.location.options,"""""")
        chosen = input()
        if chosen in self.player.location.options:
            if chosen == "travel":
                print("Du bist hier:",Stadt.orte.welt[self.player.location])
                print("Wo willst du hin reisen? Du kannst zu:",Stadt.orte.orte,"")
                dest = input()
                if dest in Stadt.orte.orte:
                    Stadt.orte.orte.append(self.player.location.name)
                    self.player.location.travel(Stadt.orte.welt[dest],self.player)
                    self.player.location = Stadt.orte.welt[dest]
                    Stadt.orte.orte.remove(self.player.location.name)
                else:
                    print("Da passt was nicht")
            if chosen == "Inventory":
                Inventory.Inventory(self.player, self.player)
            if chosen == "trade":
                print("In dieser Stadt gibt es die Händler:", self.player.location.traders,"mit wem möchtest du handeln")
                self.choice = input()
                if self.choice in self.player.location.traders:
                    traders.trader[self.choice].trade(self.player)
                elif self.choice == "nein":
                    self.Dialog()
                else:
                    print("etwas ist fehlgeschlagen. Bitte probiere es erneut")
            if chosen == "stats":
                self.player.stats(self.player)
                self.player.Equip(self.player)
            if chosen == "explore":
                enemy = random.choice(self.player.location.gegner)
                print("Während du erkundest findest du einen",enemy.name,"Er/sie/es greift dich an")
                enemy.fight(self.player)
            if chosen == "talk":
                print("Hier gibt es die Personen",self.player.location.npcs,". Mit wem möchtest du reden?")
                self.chosennpc = input()
                if self.chosennpc in self.player.location.npcs:
                    traders.npcs[self.chosennpc].talk(self.player)
            if chosen == "search":
                self.player.location.Search(self.player)
            if chosen == "rest":
                print("Du ruhst dich in einer Taverne aus. Deine Hp sind regeneriert, deine Mp sind regeneriert, du hast Stamina regeneriert")
                self.player.hp = self.player.maxhp
                self.player.mp = self.player.maxmp
                self.player.stamina = self.player.maxstamina


        else:
            print("Das kannst du hier nicht machen.")
        self.Dialog()


dia = Mydialog()
print("Bitte melde alle fehler auf github!!!")
print("Bevor es los geht:")
print("Wie heißt du?")
name = input()
dia.player.name = name
print("Hallo",name)
print("""
________________________________________________________________________________________
Du erwachst in einer nur leicht beleuchteten Hütte die du auf etwa 5 Quadratmeter schätzt.
Schnell schwingst du dich auf deine Beine und guckst dich um""")
dia.Dialog()


