import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_single_char(self):
        self.assertEqual(reverse('a'), '')

    def test_common(self):
        self.assertEqual(reverse('123'), '321')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iterable(self):
        with self.assertRaises(TypeError):
            reverse(['a', '2', '3'])


if __name__ == "__main__":
    unittest.main()
