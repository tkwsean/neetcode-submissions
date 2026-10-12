class TimeMap:

    def __init__(self):
        self.kv_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_store:
            self.kv_store[key] = []
        self.kv_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.kv_store.get(key, [])
        l, r = 0, len(values)-1
        while l <= r:
            mid = l + (r-l) // 2
            if timestamp >= values[mid][1]:
                l = mid+1
                res = values[mid][0]
            else:
                r = mid-1
        return res

