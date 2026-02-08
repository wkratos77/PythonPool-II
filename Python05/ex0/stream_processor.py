from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional # noqa


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            total = sum(data)
            length = len(data)
            return (
                f"Processed {length} numeric values, "
                f"sum={total}, avg={total/length:.1f}"
            )
        else:
            return "Invalid numeric data."

    def validate(self, data: Any) -> bool:
        if type(data) is not list or len(data) == 0:
            return False
        for num in data:
            if type(num) is not int:
                return False
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            characters = len(data)
            words = len(data.split())
            return (
                f"Processed text: {characters} characters, "
                f"{words} words"
            )
        else:
            return "Invalid text data."

    def validate(self, data: Any) -> bool:
        if type(data) is str and len(data) > 0:
            return True
        else:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            level, message = data.split(":", 1)
            level = level.strip()
            message = message.strip()
            if level == "ERROR":
                return f"[ALERT] ERROR level detected: {message}"
            elif level == "INFO":
                return f"[INFO] INFO level detected: {message}"
            else:
                return "Unknown log level."

    def validate(self, data: Any) -> bool:
        if type(data) is not str or ":" not in data:
            return False
        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()
        if level not in ["ERROR", "INFO"] or message == "":
            return False
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    print("Validation: Numeric data verified")
    numeric_result = processors[0].process(numeric_data)
    print(
        f"{processors[0].format_output(numeric_result)}\n"
    )

    print("Initializing Text Processor...")
    print(f'Processing data: "{text_data}"')
    print("Validation: Text data verified")
    text_result = processors[1].process(text_data)
    print(
        f"{processors[1].format_output(text_result)}\n"
    )

    print("Initializing Log Processor...")
    print(f'Processing data: "{log_data}"')
    print("Validation: Log entry verified")
    log_result = processors[2].process(log_data)
    print(
        f"{processors[2].format_output(log_result)}\n"
    )

    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    numeric = [2, 1, 3]
    text = "Polymorphism"
    log = "INFO: System ready"
    samples = [numeric, text, log]
    i = 1
    for processor, sample in zip(processors, samples):
        if processor.validate(sample):
            result = processor.process(sample)
            print(f"Result {i}: {result}")
            i += 1
        else:
            print("Validation failed for sample.")
    print("\nFoundation systems online. Nexus ready for advanced streams.")
