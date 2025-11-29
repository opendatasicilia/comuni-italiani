from typing import Dict, Any


class CacheManager:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def store(self, key: str, value: Any) -> None:
        self.data[key] = value

    def read(self, key: str) -> Any:
        return self.data.get(key)
