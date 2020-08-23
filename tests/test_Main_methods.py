import json
import unittest
import sys
sys.path.insert(1, "..")
from jsonfilter.__main__ import \
    get_filtered_data_single,\
        get_filtered_data_list_property,\
        get_top
from jsonfilter.Translator import Translator
from tests.LongStringsSG import LongStringsSG


class test_Main_methods(unittest.TestCase):

    def test_get_filtered_data_single(self):
        data_from_outside = LongStringsSG().get_string_longer()
        string_map = "SecurityGroups.2.Description"
        data_to_print = get_filtered_data_single(string_map, data_from_outside, Translator())
        expected_data = "SecurityGroup for ElasticBeanstalk environment"
        self.assertEqual(expected_data, data_to_print)

    def test_get_filtered_data_single_2(self):
        data_from_outside = LongStringsSG().get_string_longer()
        string_map = "SecurityGroups.1.Description"
        data_to_print = get_filtered_data_single(string_map, data_from_outside, Translator())
        expected_data = "Ssh from outside"
        self.assertEqual(expected_data, data_to_print)

    def test_get_filtered_data_list_property(self):
        data_from_outside = LongStringsSG().get_string_longer()
        string_map = "SecurityGroups..Description"
        data_to_print = get_filtered_data_list_property(string_map, Translator(), data_from_outside)
        expected_data = " * santa-fe-mysql\n * Ssh from outside\n * SecurityGroup for ElasticBeanstalk environment\n"
        self.assertEqual(expected_data, data_to_print)

    def test_get_top(self):
        data_from_outside = LongStringsSG().get_string_longer()
        dict_resulting = json.loads(data_from_outside)
        returned_items = get_top(dict_resulting)
        expected_result = ["SecurityGroups"]
        self.assertListEqual(expected_result, returned_items)

    def test_get_top_multiple_keys(self):
        data_from_outside = LongStringsSG().get_multiple_root_key()
        dict_resulting = json.loads(data_from_outside)
        returned_items = get_top(dict_resulting)
        expected_result = ["DBInstances", "Images"]
        self.assertListEqual(expected_result, returned_items)

