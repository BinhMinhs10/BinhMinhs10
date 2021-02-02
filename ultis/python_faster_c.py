# START: pip install numba

import math
from time import perf_counter
from numba import njit, prange


class GilCompiler:
    def __init__(self, N):
        self.N = N

    def is_prime(self, num):
        if num == 2:
            return True
        if num <= 1 or not num % 2:
            return False
        for div in range(3, int(math.sqrt(num) + 1), 2):
            if not num % div:
                return False
        return True

    def run_program(self):
        for i in range(self.N):
            self.is_prime(i)


@njit(fastmath=True, cache=True)
def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
    return True


@njit(fastmath=True, cache=True, parallel=True)
def run_program(N):
    for i in prange(N):
        is_prime(i)


if __name__ == '__main__':
    N = 10000000
    start = perf_counter()
    run_program(N)
    end = perf_counter()
    print(end - start)
    #################
    start = perf_counter()
    gil = GilCompiler(N)
    gil.run_program()
    end = perf_counter()
    print(end - start)
