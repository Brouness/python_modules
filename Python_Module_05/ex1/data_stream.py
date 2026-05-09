from abc import ABC, abstractmethod
import typing
from typing import Any, List


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: List[str] = []
        self._counter = 0
        self._total_processed = 0

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
            raise ValueError("Improper numeric data")
        elif isinstance(data, list):
            for element in data:
                self._storage.append(str(element))
                self._total_processed += 1
        else:
            self._storage.append(str(data))
            self._total_processed += 1


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
                self._total_processed += 1
        else:
            self._storage.append(data)
            self._total_processed += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        def valid_dict(d: dict[str, str]) -> bool:
            return (
                isinstance(d, dict)
                and "log_level" in d
                and "log_message" in d
                and isinstance(d["log_level"], str)
                and isinstance(d["log_message"], str)
            )

        if isinstance(data, dict):
            return valid_dict(data)

        if isinstance(data, list):
            return all(valid_dict(d) for d in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, dict):
            self._storage.append(format_log(data))
        else:
            for d in data:
                self._storage.append(format_log(d))


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed: bool = False
            for process in self._processors:
                if process.validate(element):
                    process.ingest(element)
                    processed = True
            if processed is False:
                print(
                    f"DataStream error - Can't "
                    f"process element in stream: {element}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            name = processor.__class__.__name__.replace(
                "Processor",
                " Processor"
            )
            print(
                f"{name}: "
                f"total {processor._total_processed} items processed, "
                f"remaining {len(processor._storage)} on processor"
            )


def consume_processor(processor: DataProcessor, nb: int) -> None:
    for _ in range(nb):
        try:
            processor.output()
        except ValueError:
            print("processor empty")


def main() -> None:
    print("=== Code Nexus - Data Strean ===\n")
    process = DataStream()
    print("Initialize Data Stream...")
    process.print_processors_stats()
    numeric = NumericProcessor()
    log = LogProcessor()
    text = TextProcessor()
    process.register_processor(numeric)
    print("\nRegistering Numeric Processor\n")
    data: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
        ]
    print(f"Send first batch of data on stream: {data}")
    process.process_stream(data)
    process.print_processors_stats()
    process.register_processor(text)
    process.register_processor(log)
    process.process_stream(data)
    print("\nRegistering other data processors\n")
    print("Send the same batch again")
    process.print_processors_stats()
    print(
        "\nConsume some elements from the data processors: " +
        "Numeric 3, Text 2, Log 1")
    consume_processor(numeric, 3)
    consume_processor(text, 2)
    consume_processor(log, 1)
    process.print_processors_stats()


if __name__ == "__main__":
    main()
