import sqlite3


class Animals():
    """docstring for Animals"""
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.days = 0
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        self.life_expactancy = cursor.execute("SELECT life_expectancy FROM animals WHERE species=\"?\";")

    def growing_old(self):
        if self.age == self.life_expectancy:
            self.__del__()
            # v bazata danni im kazvame che sa martvi
        self.days = self.days + 1
        if self.days == 31:
            self.age = self.age + 1
            self.days = 0
            conn = sqlite3.connect("animals.db")
            cursor = conn.cursor()
            #cursor.execute("UPDATE ? SET age= ? WHERE name = ?", ) ne dovarshen update

    def __eq__(self, other):
        return self.species == other.species and self.age == other.age
               and self   .name == other.name and self.gender == other.gender and self.w    eight == other.weight)

