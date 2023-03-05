from functools import wraps
import time


def timer(func):
    @wraps(func)
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} for {len(*args)} records took {total_time} seconds')
        return result
    return timer_wrapper
