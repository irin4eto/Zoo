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
        data_animal = cursor.execute("SELECT species, life_expectancy,food_type, gestation, newborn_weight, average_weight,weight_age_ratio, food_weight_ratio FROM animals WHERE species = ?",(species))
        cursor.execute("INSERT INTO animals(species, life_expectancy, food_type, gestation, newborn_weight, average_weight,weight_age_ratio, food_weight_ratio) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (data_animal[0], data_animal[1], data_animal[2], data_animal[3],data_animal[4], data_animal[5], data_animal[6], data_animal[7]))

    def see_animals(self):
        return "\n".join("<{}> : <{}>, <{}>, <{}>".format(x.name, x.species,
               x.age, x.weight) for x in self.animals_in_zoo)

    def move_to_habitat(self, species, name):
        for x in self.animals_in_zoo:
            if x.name == name and x.species == species:
                self.animals_in_zoo.pop(x)
                cursor.execute("UPDATE zoo_and_animals SET status='moved' WHERE name = ?, species = ?", (name, species))
                break

