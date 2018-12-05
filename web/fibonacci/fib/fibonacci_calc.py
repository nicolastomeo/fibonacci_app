from typing import Optional
from flask_caching import Cache

def int_cache_get(cache: Cache, key: str) -> Optional[int]:
    """
    Parses the string from Redis cache
    :param cache: Redis cache
    :param key: key
    :return: Int parsed value
    """
    cached = cache.get(key)
    if cached is None:
        return cached
    else:
        return int(cached)
class CacheCorrupted(Exception):
    """
    Exception raised when cache gets corrupted
    """
    pass


def fibonacci_generator(start_index: int, end_index: int):
    """
    Fibonacci generator bottom up that yields only values from start_index to end_index

    :param start_index: Index to start generating Fibonacci sequence
    :param end_index:  Index to end generating Fibonacci sequence
    """
    n0, n1 = 0, 1
    for i in range(end_index + 1):
        if i >= start_index:
            yield n0
        n0, n1 = n1, n0 + n1


def fibonacci_generator_cache(start_index: int, end_index: int, cache: Cache):
    """
    Fibonacci generator bottom up that yields only values from start_index to end_index
    and uses a cache to start computing from possible biggest index

    :param start_index: Index to start generating Fibonacci sequence
    :param end_index: Index to end generating Fibonacci sequence
    :param cache: Redis cache
    """
    biggest_index = int_cache_get(cache, 'biggest_index')
    if biggest_index is None:
        biggest_index = 0
        cache.set('0', '0')
        cache.set('1', '1')
    if biggest_index >= start_index:
        start_calc = start_index
    else:
        start_calc = biggest_index
    i = 0
    for i in range(start_calc, end_index + 1):
        fibi = int_cache_get(cache, str(i))
        if fibi is None:
            try:
                fibi = int_cache_get(cache, str(i - 1)) + int_cache_get(cache, str(i - 2))
            except:
                #This may happens if some key before biggest_index is deleted
                raise CacheCorrupted()
            cache.set(str(i), str(fibi))
            cache.set('biggest_index', i)
        if i >= start_index:
            yield fibi