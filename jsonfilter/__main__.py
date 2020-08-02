import sys
from jsonfilter.JsonFilter import JsonFilter
from jsonfilter.Translator import Translator

def main():
    data_from_outside = get_redirected_data()
    string_map = get_argument_provided_or_die()
    converted_string = Translator().set_humanterm(string_map).translate()
    json_filter = JsonFilter().set_mapstring(converted_string).set_contentstring(data_from_outside)
    print(json_filter.filter())


def get_argument_provided_or_die():
    try:
        return sys.argv[1]
    except IndexError:
        print("Sorry, but you need a map to provide as first argument.")
        exit()

def get_redirected_data():
    return sys.stdin.read()