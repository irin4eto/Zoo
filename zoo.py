import animals
import sqlite3


conn = sqlite3.connect("animals.db")
cursor = conn.cursor()


class Zoo():
    """docstring for Zoo"""
    def __init__(self, name, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget
        self.name = name
        self.animals_in_zoo = []

    def accommodate(self, species, age, name, gender, weight):
        new_animal = animals.Animal(species, age, name, gender, weight)
        self.animals_in_zoo.append(new_animal)
        cursor.execute("INSERT INTO zoo_and_animals(species, name, zoo, gender, weight, age, status) VALUES(?, ?, ?, ?, ?, ?, 'Alive')", (species, name, self.name, gender, weight, age))

    def see_animals(self):
        return "\n".join("<{}> : <{}>, <{}>, <{}>".format(x.name, x.species,
               x.age, x.weight) for x in self.animals_in_zoo)

    def move_to_habitat(self, species, name):
        for x in self.animals_in_zoo:
            if x.name == name and x.species == species:
                self.animals_in_zoo.pop(x)
                cursor.execute("UPDATE zoo_and_animals SET status='moved' WHERE name = ?, species = ?", (name, species))
                break
    