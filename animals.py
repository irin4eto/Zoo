import sqlite3
import create_zoo
from random import randint


conn_animals = sqlite3.connect("animals.db")
cursor_animals = conn_animals.cursor()


class Animals():
    """docstring for Animals"""
    def __init__(self, species, age, name, gender, weight, cursor):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.days = 0
        self.month = 0
        self.cursor = cursor
        self.life_expectancy = cursor_animals.execute("SELECT " +
                                                      "life_expectancy FROM" +
                                                      " animals WHERE " +
                                                      "species=?",
                                                      (self.species, ))
        self.status = cursor_animals.execute("SELECT status FROM animals")
        self.was_beard = False

    def growing_old(self):
        if self.age == self.life_expectancy:
            self.__del__()
            self.cursor.execute("UPDATE zoo_and_animals SET status='Dead' " +
                                "WHERE name=? and species=?",
                                (self.name, self.species))
        self.days = self.days + 1
        if self.days == 31:
            self.age = self.age + 1
            self.days = 0
            conn = sqlite3.connect("animals.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE ? SET age=? WHERE name=? and species=?",
                          (self.age, self.name, self.species))

    def __eq__(self, other):
        return self.species == other.species and \
            self.age == other.age and \
            self.name == other.name and \
            self.gender == other.gender and \
            self.weight == other.weight

    def eat(self):
        food_weight_ratio = cursor_animals.execute("SELECT food_weight_ratio" +
                                                   " FROM animals WHERE " +
                                                   "species=?",
                                                   (self.species, )).fetchone()
        return food_weight_ratio[0] * self.weight

    def going_to_die(self):
        chance_of_dying = (self.age / self.life_expectancy) * 100
        random_number = randint(0, 101)
        return random_number > 0 and random_number < chance_of_dying

    def new_animal_is_born(self):
        zoo_animal = self.cursor("SELECT zoo FROM zoo_and_animals" +
                                 "WHERE name=? and species=? and status=?",
                                 (self.name, self.species, "Alive"))
        if self.gender == "female" and zoo_animal is not None:

            male_animal = self.cursor("SELECT zoo, gender, species FROM "
                                      "zoo_and_animals WHERE species=? and" +
                                      "gender=?", (self.species, "male"))
            if male_animal is not None:
                if not self.was_beard or \
                   (self.was_beard and self.month >= 6):
                    print("New animal is born")
                    self.was_beard = True
                    random_number = randint(0, 101)
                    gender_new_animal = "male"
                    if random_number >= 0 and random_number < 50:
                        gender_new_animal = "female"
                    name_new_animal = input("What is {}`s name, which is" +
                                            "just born and it is " +
                                            "{}".format(self.species,
                                                        self.gender))
                    weight_new_animal = input("How much kilo it is?")
                    new_animal = Animals(self.species, 0, name_new_animal,
                                         gender_new_animal, weight_new_animal,
                                         self.cursor)
                    create_zoo.insert_zoo_and_animals(zoo_animal, new_animal,
                                                      self.cursor)
                    return True
                return False
            return False

















