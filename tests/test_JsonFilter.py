import unittest
import sys
sys.path.insert(1, "..")
from jsonfilter.JsonFilter import JsonFilter
from tests.LongString import LongString


class test_JsonFilterString(unittest.TestCase):

    def setUp(self):
        self.jsonfilter = JsonFilter()

    def test_filter_simple(self):

        result = "my_value"
        mapstring = '["mykey"]'
        json_string = '{"mykey": "my_value"}'

        self.jsonfilter.set_mapstring(mapstring).set_contentstring(json_string)
        returned_result = self.jsonfilter.filter()

        self.assertEqual(returned_result, result)

    def test_filter_simple2(self):
        result = "2"
        mapstring = '["two"]'
        json_string = '{"one" : "1", "two" : "2", "three" : "3"}'

        self.jsonfilter.set_mapstring(mapstring).set_contentstring(json_string)
        returned_result = self.jsonfilter.filter()

        self.assertEqual(returned_result, result)

    def test_filter_bigresponse1(self):
        result = "Ssh from outside"
        mapstring = '["SecurityGroups"][1]["Description"]'
        json_string = LongString().get_string()

        self.jsonfilter.set_mapstring(mapstring).set_contentstring(json_string)

        returned_result = self.jsonfilter.filter()

        self.assertEqual(returned_result, result)

    def test_filter_exception_non_string(self):
        mapstring = '["SecurityGroups"]'
        json_string = LongString().get_string()

        self.jsonfilter.set_mapstring(mapstring).set_contentstring(json_string)

        with self.assertRaises(Exception):
            self.jsonfilter.filter()

    def test_filter_list(self):
        mapstring = '["SecurityGroups"]'
        json_string = LongString().get_string()
        self.jsonfilter.set_mapstring(mapstring).set_contentstring(json_string)
        returned_list = self.jsonfilter.filter_list()
        self.assertTrue(isinstance(returned_list, list))
