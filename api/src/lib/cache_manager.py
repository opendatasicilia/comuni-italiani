import json

from redis.asyncio import Redis


class CacheManager:
    def __init__(self, redis_host="redis", redis_port=6379):
        self.redis = self.connect(redis_host, redis_port)

    @staticmethod
    def connect(host, port):
        try:
            return Redis(host=host, port=port)
        except Exception as e:
            raise ConnectionError(f"Impossibile connettersi a Redis: {e}")

    async def store(self, key: str, data):
        await self.redis.set(key, json.dumps(data))

    async def read(self, key: str):
        raw = await self.redis.get(key)
        return json.loads(raw) if raw else None
