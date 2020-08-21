import time
from functools import lru_cache, wraps


def squared(func):
    return lambda x: func(x) * func(x)


@squared
def x_plus_3(x):
    """
    Tổ hợp hàm với decorator
    Làm code sạch hơn
    Giúp DRY code - di chuyển code giống nhau vào decorator

    """
    return x + 3


def cached(tag_name):
    # func decorator cached init ONE time
    # where keep the result
    _cache = {}

    def decorated_function_param(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            start_time = time.time()
            print('Caching' + '=' * 80)
            print('_cache:', _cache)
            if args not in _cache:
                # Perform and store in cache
                _cache[args] = func(*args, **kwargs)
            print('Compute time: %ss' % round(time.time() - start_time))
            return _cache[args]
        return decorated_function
    return decorated_function_param


@lru_cache()
@cached("plus")
def complex_computation(x, y):
    """If function execute then time lazy 2 second"""
    time.sleep(2)
    return x + y


@cached("plus")
def other_complex_computation(x, y):
    """If function execute then time lazy 2 second"""
    time.sleep(2)
    return x * y


def main():
    """
    Open for Extension and Closed for Modification
    Có thể dùng nhiều decorator trong một hàm
    :return:
    """
    print(x_plus_3(2))
    assert x_plus_3(2) == 25

    print(complex_computation.__name__)
    print("Result computed: {}".format(complex_computation(1, 2)))
    print("Result computed: {}".format(complex_computation(2, 3)))
    # SKIP performance the expensive operation
    print("Result computed: {}".format(complex_computation(1, 2)))

    # Decorator can reuse
    print("Result computed other: {}".format(other_complex_computation(1, 2)))
    print("Result computed other: {}".format(other_complex_computation(1, 2)))

    # Hữu ích đến mức thành tiêu chuẩn với @lru_cache()
    # LRU = Least Recently Used


if __name__ == "__main__":
    main()