import unittest
from ..translation import french_to_english, english_to_french


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(french_to_english(None))  # test when input is null the output is None
        self.assertEqual(french_to_english('Bonjour'),'Hello') # test when input is 'Bonjour' the output is sample text



class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNone(english_to_french(None))  # test when input is null the output is None
        self.assertEqual(english_to_french('Hello'),'Bonjour') # test when input is 'Hello' the output is 'Bonjour'



unittest.main()