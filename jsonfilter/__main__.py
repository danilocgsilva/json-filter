import sys
import re
from jsonfilter.JsonFilter import JsonFilter
from jsonfilter.Translator import Translator

def main():
    data_from_outside = get_redirected_data()
    string_map = get_argument_provided_or_die()
    translator = Translator()

    if not re.search("\.\.", string_map):
        print(get_filtered_data_single(string_map, data_from_outside, translator))
    else:
        print("Still in development")

        two_parts_string_map = string_map.split("..")

        part_one = two_parts_string_map[0]
        part_two = two_parts_string_map[1]

        part_one_map = translator.set_humanterm(part_one).translate()
        json_filter = JsonFilter().set_mapstring(part_one_map).set_contentstring(data_from_outside)
        list_from_first_part = json_filter.filter_list()
        translated_second_part_filter = translator.set_humanterm(part_two).translate()
        for list_item in list_from_first_part:
            print(' * ' + eval("list_item" + translated_second_part_filter))


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
    json_filter = JsonFilter().set_mapstring(converted_string).set_contentstring(data_from_outside)
    return json_filter.filter()
