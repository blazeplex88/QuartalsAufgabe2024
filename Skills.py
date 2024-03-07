


class Skill():

    def __init__(self):
        super().__init__()
        self.name = 0
        self.mpcost = 0
        self.hpcost = 0
        self.damage = 0


class Cleave(Skill):
    def __init__(self):
        self.name = "Cleave"
        self.mpcost = 3
        self.damage = 10

    def Use(self,target,user):
        user.mp -= self.mpcost
        self.actdamage = (self.damage + user.attack)
        target.hp -= self.actdamage
        print("[",user.name," nutzt den Skill {Cleave}]")
        print("[Durch {Cleave} nimmt [",target.name,"]",self.actdamage,"Schaden. Es verbleiben",target.hp,"/",target.maxhp,"Hp")
        print("[",user.name," nutzt",self.mpcost,"MP. ",user.name,"hat noch",user.mp,"/",user.maxmp,"Mp verbleibend.")

cleave = Cleave()

usages = dict()
usages[cleave.name] = cleave
usages[cleave] = cleave.name
