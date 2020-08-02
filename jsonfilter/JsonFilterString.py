from jsonfilter.JsonFilter import JsonFilter
from jsonfilter.JsonFilterInterface import FilterJsonInterface
import json


class JsonFilterString(FilterJsonInterface):

    def __init__(self) -> None:
        self.jsonFilter = JsonFilter()
        self.contentstring = None

    def set_mapstring(self, mapstring: str):
        self.jsonFilter.set_mapstring(mapstring)
        return self

    def set_contentstring(self, contentstring: str):
        self.contentstring = contentstring
        return self

    def filter(self) -> str:
        dictResult = json.loads(self.contentstring)
        returned_object = eval("dictResult" + self.jsonFilter.get_mapstring())
        if isinstance(returned_object, str):
            return returned_object
        else:
            raise Exception('Must be a type of string.')
