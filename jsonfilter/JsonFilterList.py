from jsonfilter.JsonFilterInterface import FilterJsonInterface
from jsonfilter.JsonFilter import JsonFilter
import json


class JsonFilterList(FilterJsonInterface):


    def __init__(self) -> None:
        self.jsonFilter = JsonFilter()
        self.dictcontent = None

    def set_mapstring(self, mapstring: str):
        self.jsonFilter.set_mapstring(mapstring)
        return self

    def set_content(self, dictcontent: dict):
        if isinstance(dictcontent, dict):
            self.dictcontent = dictcontent
            return self
        raise Exception("The method set_content needs to receive only a dict content.")

    def filter(self) -> list:
        #dictResult = json.loads(self.jsonFilter.get_contentstring())
        returned_object = eval("self.dictcontent" + self.jsonFilter.get_mapstring())
        if isinstance(returned_object, list):
            return returned_object
        else:
            raise Exception('Must be a type of list.')
