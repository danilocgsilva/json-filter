import sys
import re
import json
from jsonfilter.JsonFilter import JsonFilter
from jsonfilter.Translator import Translator

def main():
    data_from_outside = get_redirected_data()
    string_map = get_argument_provided_or_empty()
    translator = Translator()

    if string_map == "":
        string_map_not_provided(data_from_outside, translator)
    else:
        string_map_provided(string_map, data_from_outside, translator)


def get_argument_provided_or_empty():
    try:
        return sys.argv[1]
    except IndexError:
        return ""


def get_redirected_data():
    return sys.stdin.read()


def get_filtered_data_single(string_map, data_from_outside, translator):
    converted_string = translator.set_humanterm(string_map).translate()
    json_filter = JsonFilter().set_mapstring(converted_string).set_contentstring(data_from_outside)
    if json_filter.filter_type().__name__ == str.__name__:
        return json_filter.filter()
    if json_filter.filter_type().__name__ == list.__name__:
        return json_filter.filter_list()


def get_filtered_data_list_property(string_map, translator, data_from_outside) -> str:
    two_parts_string_map = string_map.split("..")

    part_one = two_parts_string_map[0]
    part_two = two_parts_string_map[1]

    part_one_map = translator.set_humanterm(part_one).translate()
    json_filter = JsonFilter().set_mapstring(part_one_map).set_contentstring(data_from_outside)
    list_from_first_part = json_filter.filter_list()
    translated_second_part_filter = translator.set_humanterm(part_two).translate()
    strint_to_return = ""
    for list_item in list_from_first_part:
        strint_to_return += ' * ' + eval("list_item" + translated_second_part_filter) + "\n"
    return strint_to_return


def get_top(data_from_outside) -> list:
    list_to_return = []
    for k, v in data_from_outside.items():
        list_to_return.append(k)
    return list_to_return


def string_map_provided(string_map, data_from_outside, translator):
    if not re.search("\.\.", string_map):
        data_to_print = get_filtered_data_single(string_map, data_from_outside, translator)
    else:
        data_to_print = get_filtered_data_list_property(string_map, translator, data_from_outside)

    print(data_to_print)


def string_map_not_provided(data_from_outside, translator):
    results_mapped_top = get_top(json.loads(data_from_outside))

    print("You provided no mapping data, but here some hints:")
    for top_result in results_mapped_top:
        print(" * " + top_result)
    exit()