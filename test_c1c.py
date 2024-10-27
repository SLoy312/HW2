import unittest
from c1c import FunRandomName

class TestFunRandomName(unittest.TestCase):

    def test_add_adjective(self):
        fun_name = FunRandomName()
        initial_count = fun_name.get_total_adjectives()
        fun_name.add_adjective("Новый")
        self.assertEqual(fun_name.get_total_adjectives(), initial_count + 1)

    def test_add_noun(self):
        fun_name = FunRandomName()
        initial_count = fun_name.get_total_nouns()
        fun_name.add_noun("Профессор")
        self.assertEqual(fun_name.get_total_nouns(), initial_count + 1)

    def test_get_name(self):
        fun_name = FunRandomName()
        name = fun_name.get_name()
        self.assertIsInstance(name, str)
        self.assertEqual(len(name.split()), 2)  # Проверка, что состоит из двух слов

    def test_get_all_names(self):
        fun_name = FunRandomName()
        all_names = fun_name.get_all_names()
        self.assertIsInstance(all_names, list)
        self.assertTrue(all(isinstance(name, str) for name in all_names))
        self.assertEqual(len(all_names), fun_name.get_total_adjectives() * fun_name.get_total_nouns())

if __name__ == "__main__":
    unittest.main()
