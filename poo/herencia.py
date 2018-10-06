class Human:
    def attack(self):
        print('Lanza una patada')

class Cyborg(Human):
    def attack(self):
        print('Lanza un láser')

class Ninja(Human):
    def attack(self):
        print('Lanza una estrella')

class NinjaDesterrado(Human):
    pass

class Area51(Cyborg, Ninja):
    pass

class Area51v2(NinjaDesterrado, Cyborg):
    pass

Human().attack()
Cyborg().attack()
Ninja().attack()

Area51().attack()
Area51v2().attack()
