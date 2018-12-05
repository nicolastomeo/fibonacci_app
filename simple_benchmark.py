import time
import urllib.request
import redis


def benchmark(start_index, end_index, flask_host, flask_port, redis_host, redis_port):
    cache = redis.Redis(host=redis_host, port=redis_port)
    cache.flushall()
    print(f"Three times with no cache")
    mean_sum = 0
    for i in range(1, 4):
        start = time.time()
        urllib.request.urlopen(f'http://{flask_host}:{flask_port}/fib/{start_index}/{end_index}?nocache=1')
        end = time.time()
        dif = end - start
        mean_sum += dif
        print(f"{i} time last {dif} seconds")

    print(f'Nocache mean time: {mean_sum/3} seconds')

    print(f'First time with cache (but caching)')
    start = time.time()
    urllib.request.urlopen(f'http://{flask_host}:{flask_port}/fib/{start_index}/{end_index}')
    end = time.time()
    print(f"Last {end - start} seconds")
    mean_sum = 0
    print(f"Three times with cache")
    for i in range(1, 4):
        start = time.time()
        urllib.request.urlopen(f'http://{flask_host}:{flask_port}/fib/{start_index}/{end_index}')
        end = time.time()
        dif = end - start
        mean_sum += dif
        print(f"{i} time last {dif} seconds")

    print(f'Cache mean time: {mean_sum/3} seconds')


if __name__ == '__main__':
    print(f'Testing with start_index: 5000 and end_index: 5010')
    benchmark(8000, 8010, 'localhost', 8000, 'localhost', 6378)
    print(f'Testing with start_index: 1000 and end_index: 10000')
    benchmark(1000, 10000, 'localhost', 8000, 'localhost', 6378)

"""
From these benchmarks I can conclude that the caching version is faster when the start_index is far away from 0 and
not so far from the end_index, otherwise the non-caching version is faster.
This is because i am using a bottom up strategy to calculate the Fibonacci sequence and therefore, the 0 to start_index
calculations can be skipped if they are cached but then the operations are so simple (a sum and a couple of assignments)
 than they are probably faster than getting the values from Redis.
"""
