class Animals():
    """docstring for Animals"""

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def __eq__(self, other):
        return self.species == other.species and self.age == other.age
               and self   .name == other.name and self.gender == other.gender and self.w    eight == other.weight)

