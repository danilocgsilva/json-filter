import json


class JsonFilter:

    def __init__(self) -> None:
        self.mapstring = None

    def set_mapstring(self, mapstring: str):
        self.mapstring = mapstring
        return self

    def get_mapstring(self):
        return self.mapstring
