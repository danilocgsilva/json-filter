import sys
import re
from jsonfilter.JsonFilterString import JsonFilterString
from jsonfilter.JsonFilterList import JsonFilterList
from jsonfilter.Translator import Translator

def main():
    data_from_outside = get_redirected_data()
    string_map = get_argument_provided_or_die()
    translator = Translator()

    if not re.search("\.\.", string_map):
        print(get_filtered_data_single(string_map, data_from_outside, translator))
    else:
        two_parts = string_map.split('..')

        part_one = two_parts[0]
        part_two = two_parts[1]

        converted_string = translator.set_humanterm(part_one).translate()
        json_filter_list = JsonFilterList().set_mapstring(converted_string).set_contentstring(data_from_outside)
        list_entities = json_filter_list.filter()
        for entities in list_entities:
            converted_second_part = translator.set_humanterm(part_two).translate()
            json_filter_loop = JsonFilterString().set_mapstring(converted_second_part).set_contentstring(entities)
            print(json_filter_loop.filter())


def get_argument_provided_or_die():
    try:
        return sys.argv[1]
    except IndexError:
        print("Sorry, but you need a map to provide as first argument.")
        exit()


def get_redirected_data():
    return sys.stdin.read()


def get_filtered_data_single(string_map, data_from_outside, translator):
    converted_string = translator.set_humanterm(string_map).translate()
    json_filter = JsonFilterString().set_mapstring(converted_string).set_contentstring(data_from_outside)
    return json_filter.filter()
