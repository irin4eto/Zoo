import unittest
import zoo
import animals
import create_zoo
import os


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.cursor_zoo = create_zoo.create_cursor_and_table("test_zoo.db")
        self.animal1 = animals.Animals("lion", 5, "Jack", "male", 30,
                                       self.cursor_zoo)
        self.animal2 = animals.Animals("koala", 3, "Mimi", "female", 10,
                                       self.cursor_zoo)
        self.all_animal = []
        self.all_animal.append(self.animal1)
        self.all_animal.append(self.animal2)
        self.zoo = zoo.Zoo("The_Best_Zoo", self.all_animal, 10, 5000,
                           self.cursor_zoo)

        create_zoo.insert_zoo(self.zoo, self.cursor_zoo)
        create_zoo.insert_zoo_and_animals(self.zoo, self.animal1,
                                          self.cursor_zoo)
        create_zoo.insert_zoo_and_animals(self.zoo, self.animal2,
                                          self.cursor_zoo)

    def test_accommodate_in_refference(self):
        animal3 = animals.Animals("tiger", 2, "Koko", "male", 5,
                                  self.cursor_zoo)
        self.zoo.accommodate("tiger", 2, "Koko", "male", 5)
        self.assertEqual(animal3, self.zoo.animals_in_zoo[2])

    def test_accommodate_in_table(self):
        self.zoo.accommodate("tiger", 2, "Koko", "male", 5)
        animal = self.cursor_zoo.execute("SELECT species " +
                                         "FROM " +
                                         "zoo_and_animals").fetchall()
        self.assertEqual([('lion',), ('koala',), ('tiger',)], animal)

    def test_see_animals(self):
        self.assertEqual("<Jack> : <lion>, <5>, <30>\n" +
                         "<Mimi> : <koala>, <3>, <10>", self.zoo.see_animals())

    def test_move_habitat(self):
        self.zoo.move_to_habitat("lion", "Jack")
        is_moved = self.cursor_zoo.execute("SELECT status FROM" +
                                           " zoo_and_animals WHERE species=?"
                                           " and name =?",
                                           ("lion", "Jack")).fetchone()
        self.assertEqual(is_moved, ('moved', ))

    def test_daily_incomes(self):
        self.assertEqual(120, self.zoo.daily_incomes())

    def test_daily_outcomes(self):
        self.assertEqual(3.1, self.zoo.daily_outcomes())

    def test_daily_can_feed_all_animals(self):
        self.assertEqual(True, self.zoo.daily_can_feed_all_animals())

    def tearDown(self):
        os.remove("test_zoo.db")


if __name__ == '__main__':
    unittest.main()
