# __all__ = ['GlobalGoblinVars']

class Slimy:
    def __init__(self):
        self.name = "Slimy"
        self.statSpeed = 4
        self.statArmor = 0.7
        self.statHealth = 5
        self.statDamage = 3
        self.appliedEffect = "slow"


class Tough:
    def __init__(self):
        self.name = "Tough"
        self.statSpeed = 3
        self.statArmor = 0.5
        self.statHealth = 8
        self.statDamage = 8
        self.appliedEffect = "none"


class Fast:
    def __init__(self):
        self.name = "Fast"
        self.statSpeed = 8
        self.statArmor = 1.2
        self.statHealth = 3
        self.statDamage = 1
        self.appliedEffect = "none"


class Slow:
    def __init__(self):
        self.name = "Slow"
        self.statSpeed = 0
        self.statArmor = 0.8
        self.statHealth = 5
        self.statDamage = 5
        self.appliedEffect = "none"


class Dumb:
    def __init__(self):
        self.name = "Dumb"
        self.statSpeed = 1
        self.statArmor = 1
        self.statHealth = 1
        self.statDamage = 1
        self.appliedEffect = "none"


class Normal:
    def __init__(self):
        self.name = "Normal"
        self.statSpeed = 5
        self.statArmor = 1
        self.statHealth = 5
        self.statDamage = 5
        self.appliedEffect = "none"


#Global Vars including Typelist
class GlobalGoblinVars:
    GoblinBaseSpeed = 5
    GoblinBaseArmor = 0
    GoblinBaseHealth = 5
    GoblinBaseDamage = 0
    GlobalGoblinTypesList = [Slimy(), Tough(), Dumb(), Normal(), Slow(), Fast()]
    GlobalGoblinTypesDict = {"Slimy": Slimy(), "Tough": Tough(), "Dumb": Dumb(), "Normal": Normal(), "Slow": Slow(), "Fast": Fast()}
    GlobalGoblinBaseStatsList = {"Spe": GoblinBaseSpeed, "Arm": GoblinBaseArmor, "Hea": GoblinBaseHealth, "Dam": GoblinBaseDamage}
