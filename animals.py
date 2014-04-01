import sqlite3
from random import randint


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
        self.life_expactancy = cursor.execute("SELECT life_expectancy FROM animals WHERE species=\"?\";", (species))


    def growing_old(self):
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        integer_for_dying = randint(1, 100)
        if integer_for_dying < self.age * 100 / self.life_expectancy:
            self.__del__()
            cursor.execute("UPDATE zoo_and_animals SET status='Dead' WHERE name=?, species=?", (self.name, self.species))
        else:
            self.days = self.days + 1
            if self.days == 31:
                self.age = self.age + 1
                self.days = 0
                conn = sqlite3.connect("animals.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE ? SET age=? WHERE name=?, species=?", (self.age, self.name, self.species))

    def __eq__(self, other):
        return self.species == other.species and self.age == other.age and self.name == other.name and self.gender == other.gender and self.weight == other.weight

    # def eat(self):
