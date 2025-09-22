import time


def time_it(f):
    time_it.active = 0

    def tt(*args, **kwargs):
        time_it.active += 1
        start_time = time.time()
        tabs = '\t'*(time_it.active - 1)
        name = f.__name__
        print(f"{tabs}Executing <{name}>")
        result = f(*args, **kwargs)
        print(f"{tabs}Function <{name}> execution time: {time.time() - start_time:.10f} seconds")
        time_it.active -= 1
        return result
    return tt