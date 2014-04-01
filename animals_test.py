import animals
import unittest


class SpeciesTest(unittest.TestCase):
    def test_see_animals(self):
        frodo = animals('Frog', '5', 'Frodo', 'Male', '0.5')
        self.assertEqual("Frodo: Frog, 5, 0.5,", animals.see_animals())
