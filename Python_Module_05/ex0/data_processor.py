from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise ValueError("Empty Storage!")
        else:
            value = self._storage.pop(0)
            index = self._counter
            self._counter += 1
        return (index, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        elif isinstance(data, list):
            if all(isinstance(element, (int, float)) for element in data):
                return True
            else:
                return False
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data !")
        elif isinstance(data, list):
            for element in data:
                self._storage.append(str(element))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            if all(isinstance(element, str) for element in data):
                return True
            else:
                return False
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data!")
        elif isinstance(data, list):
            for element in data:
                self._storage.append(element)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            my_keys = data.keys()
            my_value = data.values()
            if all(isinstance(key, str) for key in my_keys) and all(isinstance(value, str) for value in my_value):
                    return True
            else:
                return False

        if isinstance(data, list):
            x = 0
            for singel_dic in data:
                if isinstance(singel_dic, dict):
                    my_keys = singel_dic.keys()
                    my_value = singel_dic.values()
                else:
                    return False
                if all(isinstance(key, str) for key in my_keys) and all(isinstance(value, str) for value in my_value):
                    continue
                else:
                    x += 1
            if x != 0:
                return False
            else:
                return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data!")
        elif isinstance(data, dict):
            for key, value in data.items():
                my_list = key, value
                self._storage.extend(my_list)
        elif isinstance(data, list):
            for element in data:
                for key, value in element.items():
                    my_list = key, value
                    self._storage.extend(my_list)


my_list = [{"amine": "bourajli", "hfdla": "fd"}, {"alo ": "fdjshf"}, {"fdf": "55"}]
younes = LogProcessor()
booll = younes.validate(my_list)
print(booll)
younes.ingest(my_list)
print(younes._storage)
