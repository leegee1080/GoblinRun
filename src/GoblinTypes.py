# __all__ = ['GlobalGoblinVars']

class Slimy:
    def __init__(self):
        self.name = "Slimy"
        self.statSpeed = 4
        self.statArmor = 6
        self.statHealth = 5
        self.statDamage = 3
        self.appliedEffect = "slow"


class Tough:
    def __init__(self):
        self.name = "Tough"
        self.statSpeed = 3
        self.statArmor = 8
        self.statHealth = 8
        self.statDamage = 8
        self.appliedEffect = "none"


class Fast:
    def __init__(self):
        self.name = "Fast"
        self.statSpeed = 8
        self.statArmor = 3
        self.statHealth = 3
        self.statDamage = 3
        self.appliedEffect = "none"


class Slow:
    def __init__(self):
        self.name = "Slow"
        self.statSpeed = 1
        self.statArmor = 5
        self.statHealth = 5
        self.statDamage = 5
        self.appliedEffect = "none"


class Dumb:
    def __init__(self):
        self.name = "Dumb"
        self.statSpeed = 2
        self.statArmor = 2
        self.statHealth = 2
        self.statDamage = 2
        self.appliedEffect = "none"


class Normal:
    def __init__(self):
        self.name = "Normal"
        self.statSpeed = 5
        self.statArmor = 5
        self.statHealth = 5
        self.statDamage = 5
        self.appliedEffect = "none"


#Global Vars including Typelist
class GlobalGoblinVars:
    GoblinBaseSpeed = 1
    GoblinBaseArmor = 0
    GoblinBaseHealth = 0
    GoblinBaseDamage = 0
    GlobalGoblinTypesList = {"Slimy": Slimy(), "Tough": Tough(), "Dumb": Dumb(), "Normal": Normal(), "Slow": Slow(), "Fast": Fast()}
    GlobalGoblinBaseStatsList = {"Spe": GoblinBaseSpeed, "Arm": GoblinBaseArmor, "Hea": GoblinBaseHealth, "Dam": GoblinBaseDamage}
