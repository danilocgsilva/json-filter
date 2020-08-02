import unittest
import sys
sys.path.insert(1, "..")
from jsonfilter.JsonFilterList import JsonFilterList
from tests.LongString import LongString


class test_JsonFilterList(unittest.TestCase):

    def setUp(self) -> None:
        self.jsonFilterList = JsonFilterList()

    def test_simple_list_type_return(self):

        mapstring = '["SecurityGroups"]'
        json_string = LongString().get_string()
        self.jsonFilterList.set_mapstring(mapstring).set_content(json_string)

        returned_result = self.jsonFilterList.filter()

        self.assertTrue(isinstance(returned_result, list))

