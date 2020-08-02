import json

class JsonFilter:

    def __init__(self):
        self.mapstring = None
        self.contentstring = None

    def set_mapstring(self, mapstring: str):
        self.mapstring = mapstring
        return self

    def set_contentstring(self, contentstring: str):
        self.contentstring = contentstring
        return self

    def filter(self):
        dictResult = json.loads(self.contentstring)
        return eval("dictResult" + self.mapstring)
