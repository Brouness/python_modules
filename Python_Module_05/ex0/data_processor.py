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
        try:
            if not self.validate(data):
                raise ValueError
            elif isinstance(data, list):
                for element in data:
                    self._storage.append(str(element))
            else:
                self._storage.append(str(data))
        except ValueError:
            raise ValueError("Improper numeric data")


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
        try:
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
        except ValueError:
            raise ValueError("Improper numeric data")


def Testing_Numeric_data() -> None:
    print("Testing Numeric Processor...")
    Numeric = NumericProcessor()
    print(f" Trying to validate input '42': {Numeric.validate(42)}")
    hello = "Hello"
    print(f" Trying to validate input {hello}: {Numeric.validate(hello)}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        Numeric.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    my_list = [1, 2, 3, 4, 5]
    Numeric.ingest(my_list)
    print(f" Processing data: {my_list}")
    print(" Extracting 3 values...")
    index, value = Numeric.output()
    print(f" Numeric value {index}: {value}")
    index, value = Numeric.output()
    print(f" Numeric value {index}: {value}")
    index, value = Numeric.output()
    print(f" Numeric value {index}: {value}")
    print()


def Testing_Text_Processor() -> None:
    print("Testing Text Processor...")
    Text = TextProcessor()
    print(f" Trying to validate input '42': {Text.validate(42)}")
    hello = ["Hello", "Nexus", "World"]
    Text.ingest(hello)
    print(f" Processing data: {hello}")
    print(" Extracting 1 value...")
    index, value = Text.output()
    print(f" Numeric value {index}: {value}")
    print()


def Testing_Log_Processor() -> None:
    print("Tesring Log Processor...")
    Log = LogProcessor()
    hello = "Hello"
    print(f" Trying to validatr input {hello}: {Log.validate(hello)}")
    my_list = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
        ]
    Log.ingest(my_list)
    print(f" Processing data: {my_list}")
    print("Extracting 2 values...")
    x, y = Log.output()
    print(f"Log entry {x}: {y}")
    x, y = Log.output()
    print(f"Log entry {x}: {y}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    Testing_Numeric_data()
    Testing_Text_Processor()
    Testing_Log_Processor()

if __name__ == "__main__":
    main()
