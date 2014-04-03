import animals
import sqlite3
import create_zoo


conn_animals = sqlite3.connect("animals.db")
cursor_animals = conn_animals.cursor()


class Zoo():
    """docstring for Zoo"""
    def __init__(self, name, animals, capacity, budget, cursor):
        self.animals_in_zoo = animals
        self.capacity = capacity
        self.budget = budget
        self.name = name
        self.cursor = cursor

    def accommodate(self, species, age, name, gender, weight):
        new_animal = animals.Animals(species, age, name, gender, weight,
                                     self.cursor)
        self.animals_in_zoo.append(new_animal)
        create_zoo.insert_zoo_and_animals(self, new_animal, self.cursor)

    def see_animals(self):
        return "\n".join("<{}> : <{}>, <{}>, <{}>".format(x.name, x.species,
               x.age, x.weight) for x in self.animals_in_zoo)

    def move_to_habitat(self, species, name):
        for i in range(len(self.animals_in_zoo)):
            if self.animals_in_zoo[i].name == name and \
               self.animals_in_zoo[i].species == species:
                self.animals_in_zoo.pop(i)
                self.cursor.execute("UPDATE zoo_and_animals SET status=? " +
                                    "WHERE name=? and species=?",
                                    ("moved", name, species))
                break

    def daily_incomes(self):
        return len(self.animals_in_zoo) * 60

    def daily_outcomes(self):
        outcomes = 0
        for animal in self.animals_in_zoo:
            food_type = cursor_animals.execute("SELECT food_type FROM" +
                                               " animals WHERE species=?",
                                              (animal.species, ))
            daily_eat = animal.eat()
            if food_type == "carnivore":
                outcomes += daily_eat * 4
            else:
                outcomes += daily_eat * 2
        return outcomes

    def daily_can_feed_all_animals(self):
        return (self.budget + self.daily_incomes()) > self.daily_outcomes()





