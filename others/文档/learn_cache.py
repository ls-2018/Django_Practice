import functools
from .my_lrucache import LRUCacheDict


def cache_it(max_size=1024, expiration=60):
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result

        return inner

    return wrapper


@cache_it(max_size=1024, expiration=3)
def query(sql):
    import time
    time.sleep(1)
    result = 'execute %s' % sql
    return result


# python3自带
from functools import lru_cache
