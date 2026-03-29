class TimeMap:

    def __init__(self):
        self.Map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Map[key][timestamp] = value
        print(self.Map)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.Map:
            for t in sorted(self.Map[key].keys(), reverse=True):
                if t <= timestamp:
                    return self.Map[key][t]
        return ""