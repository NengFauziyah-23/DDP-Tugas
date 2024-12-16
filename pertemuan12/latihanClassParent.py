class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender=gender

    def berjalan(self):
        print(f"{self.name} sedang berjalan")

    def berkendara(self):
        print(f"{self.name} sedang berkendara")

    def ngomong(self):
        if self.gender == 'pria':
            print(f"{self.name} tidak bercerita karena dia {self.gender}")
        else:
            print(f"{self.name} senang bercerita karena dia {self.gender}")

class Supir(Person):
    def __init__(self, name, age, gender,sim):
        super().__init__(name, age, gender)
        self.sim = sim




def berkendara(self):
    Supir().berkendara()
    print(f"{self.name} sedang berkendara dengan SIM {self.sim}")

budi = Person('budi', 20, 'pria')
budi.ngomong()
budi.berkendara()

agus = Supir('agus', 20, 'wanita', 'A')
agus.ngomong()
print (agus.sim)
agus.berkendara()

