import abc


class FilterJsonInterface(abc.ABC):

    @abc.abstractmethod
    def set_mapstring(self, mapstring: str):
        pass
