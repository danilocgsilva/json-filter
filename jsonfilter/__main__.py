import sys
from jsonfilter.JsonFilter import JsonFilter

def main():
    data_from_outside = sys.stdin.read()
    string_map = sys.argv[1]
    json_filter = JsonFilter()
    print(json_filter.filter(data_from_outside, string_map))
