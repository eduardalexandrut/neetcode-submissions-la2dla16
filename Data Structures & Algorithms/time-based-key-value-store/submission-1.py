class TimeMap:

    def __init__(self):
        self.Map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Map[key].append((timestamp, value))
        print(self.Map)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.Map:
            for entry in sorted(self.Map[key], reverse = True):
                if entry[0] <= timestamp:
                    return entry[1]
        return ""