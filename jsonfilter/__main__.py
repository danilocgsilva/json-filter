import sys
from jsonfilter.JsonFilter import JsonFilter

def main():
    data_from_outside = sys.stdin.read()
    string_map = sys.argv[1]
    json_filter = JsonFilter().set_mapstring(string_map).set_contentstring(data_from_outside)
    print(json_filter.filter())
