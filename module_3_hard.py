data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def summ_(*args):
    total = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            total += summ_(*arg)
        elif isinstance(arg, dict):
            total += summ_(*arg.items())
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, (int)):
            total += arg
    return total


print(summ_(data_structure))
