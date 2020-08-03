import json


class JsonFilter:

    def __init__(self) -> None:
        self.mapstring = None
        self.contentstring = None

    def set_mapstring(self, mapstring: str):
        self.mapstring = mapstring
        return self

    def set_contentstring(self, contentstring: str):
        self.contentstring = contentstring
        return self

    def filter_any(self):
        dictResult = json.loads(self.contentstring)
        return eval("dictResult" + self.mapstring)

    def filter(self) -> str:
        returned_object = self.filter_any()
        if isinstance(returned_object, str):
            return returned_object
        raise Exception('Must be a type of string.')

    def filter_list(self) -> list:
        returned_object = self.filter_any()
        if isinstance(returned_object, list):
            return returned_object
        raise Exception('Must be a type of list.')
