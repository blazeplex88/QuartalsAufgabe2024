import ReisenTest


class Quest:

    def __init__(self):
        self.name = 0
        self.rewardmon = 0
        self.rewardexp = 0

    def accept_quest(self):
        quests.append(self)
        print("Die Quest", self.name, " wurde angenommen")

    def finish_quest(self, player):
        quests.remove(self)
        print("Die Quest", self.name, "wurde abgeschlossen."
                                      "Du erhältst:", self.rewardmon, "Münzen und", self.rewardexp, " Exp")
        player.money += self.rewardmon
        player.exp += self.rewardexp


class KillQuest(Quest):

    def __init__(self):
        super().__init__()
        self.target = 0
        self.targetneed = 0
        self.targethave = 0

    def check_quest(self, player):
        killed = player.enemiesKilled.count(self.target)
        self.targethave += killed
        for x in range(killed):
            player.enemiesKilled.remove(self.target)
        if self.targethave >= self.targetneed:
            self.finish_quest(player)
        else:
            print(self.name, ": [", self.targethave, "/", self.targetneed, "]")


class Ratten(KillQuest):

    def __init__(self):
        super().__init__()
        self.name = "Töte 5 Ratten"
        self.rewardexp = 20
        self.rewardmon = 40
        self.target = "Ratte"
        self.targetneed = 5


class Goblin1(KillQuest):

    def __init__(self):
        super().__init__()
        self.name = "Töte 5 Goblins"
        self.rewardexp = 40
        self.rewardmon = 45
        self.target = "Goblin"
        self.targetneed = 5




ratten = Ratten()
goblin1 = Goblin1()
quests = list()
