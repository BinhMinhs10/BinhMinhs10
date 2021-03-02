from icecream import ic


def foo(i):
    return i + 10


# print both its own arg and values of those arg
ic(foo(12))
d = {'love': {1: 'Hong Viet'}}
ic(d['love'][1])


# determine which parts of your program executed
def check(arg):
    i = 10
    if arg == 'first':
        ic()
    else:
        ic()


check('first')
