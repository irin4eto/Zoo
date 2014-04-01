import animals
import unittest


class SpeciesTest(unittest.TestCase):
    # def test_see_animals(self):
    #     frodo = animals('Frog', '5', 'Frodo', 'Male', '0.5')
    #     self.assertEqual("Frodo: Frog, 5, 0.5,", animals.see_animals())

    def test_growing_old1(self):
        frodo = animals.Animals('Frog', 5, 'Frodo', 'Male', 0.5)
        frodo.growing_old()
        self.assertEqual(5, frodo.age)

    def test_growing_old2(self):
        frodo = animals.Animals('Frog', 5, 'Frodo', 'Male', 0.5)
        frodo.days = 30
        frodo.growing_old()
        self.assertEqual(6, frodo.age)

    def test_growing_old_and_dying(self):
        frodo = animals.Animals('Frog', 5, 'Frodo', 'Male', 0.5)
      
if __name__ == '__main__':
    unittest.main()
