class Animals():
    """docstring for Animals"""
    animals_in_zoo = {}

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        animals_in_zoo[self.name] = self.species

    def see_animals(self):
        for animal in animals_in_zoo:
            print (animal + ' : ' + animals_in_zoo[animal] + ' ' + animal.age + ' ' + animal.weight)
