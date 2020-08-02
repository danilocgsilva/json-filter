import unittest
import sys
sys.path.insert(1, "..")
from jsonfilter.Translator import Translator

class test_JsonFilter(unittest.TestCase):

    def setUp(self):
        self.translator = Translator()

    def test_translate_simple_word(self):
        simple_word = "SecurityGroups"
        machine_translation = '["SecurityGroups"]'
        self.translator.set_humanterm(simple_word)
        returned_term = self.translator.translate()
        self.assertEqual(returned_term, machine_translation)

    def test_translate_two_terms(self):
        terms_to_translate = "SecurityGroups.Name"
        machine_translation = '["SecurityGroups"]["Name"]'
        self.translator.set_humanterm(terms_to_translate)
        returned_term = self.translator.translate()
        self.assertEqual(returned_term, machine_translation)

    def test_translate_with_number(self):
        terms_to_translate = "SecurityGroups.0.GroupName"
        machine_translation = '["SecurityGroups"][0]["GroupName"]'
        self.translator.set_humanterm(terms_to_translate)
        returned_term = self.translator.translate()
        self.assertEqual(returned_term, machine_translation)