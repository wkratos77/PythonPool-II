from abc import abstractmethod, ABC
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.batches_processed = 0
        self.items_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id,
                "batches_processed": self.batches_processed,
                "items_processed": self.items_processed}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not all(isinstance(item, str) for item in data_batch):
                return "Invalid data batch. Only strings are allowed."
        except Exception:
            return "Invalid data batch. Only strings are allowed."
        temps = []
        for item in data_batch:
            parts = item.split(":")
            if len(parts) != 2:
                return "Invalid data format. Expected 'key:value'."
            if parts[0] == "temp":
                try:
                    temp_value = float(parts[1])
                    temps.append(temp_value)
                except ValueError:
                    return "Invalid temperature value. Must be a number."
        avg_tmp = sum(temps) / len(temps) if temps else 0
        self.items_processed += len(data_batch)
        self.batches_processed += 1

        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg_tmp:.1f}°C"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            filtered: List[Any] = []
            for item in data_batch:
                if not isinstance(item, str):
                    continue
                if not item.startswith("temp:"):
                    continue

                parts = item.split(":", 1)
                if len(parts) != 2:
                    continue

                try:
                    value = float(parts[1])
                except ValueError:
                    continue

                if value >= 30:
                    filtered.append(item)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "sensor"
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not all(isinstance(item, str) for item in data_batch):
                return "Invalid data batch. Only strings are allowed."
        except Exception:
            return "Invalid data batch. Only strings are allowed."
        self.items_processed += len(data_batch)
        self.batches_processed += 1

        buy = [int(item.split(":")[1])
               for item in data_batch if item.startswith("buy:")]
        sell = [int(item.split(":")[1])
                for item in data_batch if item.startswith("sell:")]

        net = sum(buy) - sum(sell)
        if net > 0:
            return (
                f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: +{net} units"
            )
        return (
            f"Transaction analysis: {len(data_batch)} "
            f"operations, net flow: {net} units"
            )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            filtered = []
            for item in data_batch:
                if not (item.startswith("buy:") or item.startswith("sell:")):
                    continue
                try:
                    amount = int(item.split(":", 1)[1])
                except ValueError:
                    continue
                if amount >= 100:
                    filtered.append(item)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "transaction"
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not all(isinstance(item, str) for item in data_batch):
                return "Invalid data batch. Only strings are allowed."
        except Exception:
            return "Invalid data batch. Only strings are allowed."

        error_count = sum(1 for item in data_batch if "error" in item.lower())
        self.items_processed += len(data_batch)
        self.batches_processed += 1
        if error_count == 1:
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{error_count} error detected"
            )
        else:
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{error_count} errors detected"
            )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [item for item in data_batch if "error" in item.lower()]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "event"
        return stats


# Polymorphic Stream Processor
class StreamProcessor():
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_batches: Dict[str, List[Any]]) -> List[str]:
        results = []
        stream_map = {s.stream_id: s for s in self.streams}
        for sid, batch in data_batches.items():
            stream = stream_map.get(sid)
            if stream is None:
                results.append(f"ERROR: Stream {sid} not found.")
                continue
            try:
                results.append(stream.process_batch(batch))
            except Exception:
                results.append(f"ERROR: Failed processing batch for {sid}.")
        return results

    def process_batch(self, stream_id: str,
                      data_batch: List[Any]) -> str:
        for stream in self.streams:
            if stream.stream_id == stream_id:
                try:
                    return stream.process_batch(data_batch)
                except Exception:
                    return f"ERROR: Failed processing batch for {stream_id}."
        return f"ERROR: Stream {stream_id} not found."


if __name__ == "__main__":
    def show_batch(items: List[str]) -> str:
        return "[" + ", ".join(items) + "]"

    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {show_batch(sensor_batch)}")
    print(sensor.process_batch(sensor_batch))
    print()

    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(f"Processing transaction batch: {show_batch(trans_batch)}")
    print(trans.process_batch(trans_batch))
    print()

    event_batch = ["login", "error", "logout"]
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: {show_batch(event_batch)}")
    print(event.process_batch(event_batch))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor([sensor, trans, event])
    batch1_sensor = ["temp:30.0", "humidity:50"]
    batch1_trans = ["buy:10", "sell:5", "buy:20", "sell:1"]
    batch1_event = ["login", "error", "logout"]

    batch1 = {
        "SENSOR_001": batch1_sensor,
        "TRANS_001": batch1_trans,
        "EVENT_001": batch1_event,
    }
    results = processor.process_all(batch1)

    print("Batch 1 Results:")

    print(f"- Sensor data: {len(batch1_sensor)} readings processed")
    print(f"- Transaction data: {len(batch1_trans)} operations processed")
    print(f"- Event data: {len(batch1_event)} events processed")
    print()

    print("Stream filtering active: High-priority data only")

    sensor_alert_batch = ["temp:31.0", "temp:30.2", "humidity:40"]
    critical_alerts = sensor.filter_data(sensor_alert_batch, "high")

    trans_alert_batch = ["buy:75", "sell:150", "buy:25"]
    large_tx = trans.filter_data(trans_alert_batch, "high")

    print(
        f"Filtered results: {len(critical_alerts)} critical sensor alerts, "
        f"{len(large_tx)} large transaction"
    )
    print("\nAll streams processed successfully. Nexus throughput optimal.")
