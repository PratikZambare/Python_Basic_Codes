import time
from functools import lru_cache

@lru_cache(3) # save upto 3 number of values that pass when calling a some work function
def some_work(n):\
    # some task taking n numbers of seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print('Running now')
    some_work(3)
    print('calling...again')
    some_work(2)
    print('called again')
    some_work(1)
    print('called again')
    some_work(3)
    print('called again')
    some_work(3)
    print('called again')