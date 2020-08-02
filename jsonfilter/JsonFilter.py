import json

class JsonFilter:

    def filter(self, data_string: str, mapstring: str):
        dictResult = json.loads(data_string)
        return eval("dictResult" + mapstring)