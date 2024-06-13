# from abc import ABC, abstractmethod



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species 

    # @abstractmethod
    def speak(self):
        return f"Animal sound"

    def __repr__(self):
        return f"Name of animal: {self.name} , Type of species: {self.species}"
    
class Mammal(Animal):
    def __init__(self, name, species):  #dont need __init__ if not changing parent attribute
        super().__init__()
        
    def give_birth(self):
        return f"{self.name} has given birth"
    
class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__()

    def climbs_trees(self):
        return f"{self.name} is climbing trees"
    
class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__()

    def carry_baby(self):
        return f"{self.name} is carrying its baby"

    
class Bird (Animal):
    def __init__(self, name, species, wingspan, speech):
        super().__init__(name, species)
        self.wingspan = wingspan
        self.speech = speech

    def speak(self):
        return f"{self.name} speaks {self.speech}"

    def __repr__(self):
        return f"Name of animal: {self.name} , Type of species: {self.species} , wingspan length: {self.wingspan}, speaks {self.speech}"

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__()

    def bask_in_sun(self):
        return f"{self.name} basking in the sun"
    

#------PART 3------

class Aviary:
    def __init__(self, birds):  #list of birds
        self.birds = birds

class ReptileEnclosure:
    def __init__(self, reptiles): #list of reptiles
        self.reptiles = reptiles

# elephant = Mammal("elephant", "animal")
# print(elephant)
# falcon = Bird("falcon", "bird", "6ft", "spanish")
# print(falcon.speak())

# animal = Animal("Lion", "Felis leo")
# print(animal.name)
# print(animal.species)
# print(animal.speak())

        
