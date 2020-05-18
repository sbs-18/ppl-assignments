# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
class Animal:
    def __init__(self):
        pass
    def create(self):
        print("Animal Created!")


# %%
class Herbivore(Animal):
    def __init__(self):
        self.__species="mammal"
    def eats(self,typ):
        print(typ+" eats grass")
    


# %%
class Cow(Herbivore):
    def __init__(self):
        Herbivore.__init__(self)
        self.eats("Cow")
    def sound(self):
        print("Cow moos")
    


# %%
class Horse(Herbivore):
    def __init__(self):
        Herbivore.__init__(self)
        self.eats("Horse")
    def sound(self):
        print("Horse Neighs")


# %%
class Goat(Herbivore):
    def __init__(self):
        Herbivore.__init__(self)
        self.eats("Goat")
    def sound(self):
        print("Goat bleats")


# %%
class Donkey(Herbivore):
    def __init__(self):
        Herbivore.__init__(self)
        self.eats("Donkey")
    def sound(self):
        print("Donkey Hee-Haws")


# %%
class Carnivore(Animal):
    def __init__(self):
        self.__species="mammal"
    def eats(self,typ):
        print(typ+" eats meat")
    


# %%
class Lion(Carnivore):
    def __init__(self):
        Carnivore.__init__(self)
        self.eats("Lion")
    def sound(self):
        print("Lion roars")


# %%
class Tiger(Carnivore):
    def __init__(self):
        Carnivore.__init__(self)
        self.eats("Tiger")
    def sound(self):
        print("Tiger roars")


# %%
class Leopard(Carnivore):
    def __init__(self):
        Carnivore.__init__(self)
        self.eats("Leopard")
    def sound(self):
        print("Leopard screeches")


# %%
class Hyena(Carnivore):
    def __init__(self):
        Carnivore.__init__(self)
        self.eats("Hyena")
    def sound(self):
        print("Hyena screeches")


# %%
l = Lion()


# %%
l.sound()


# %%



# %%


