from typing import Iterable, Any

# if function is None we return True values !
def ft_filter(regulator, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those item of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    # print(iterable, regulator)
    if iterable is None:
        raise TypeError("'NoneType' object is not iterable")
    elif regulator is None:
        yield from [elem for elem in iterable if elem]
    else:
        yield from [elem for elem in iterable if regulator(elem)]


def main():
    asciDict = {
        'z': 0,
        'a': 97,
        'b': 98,
        'c': 100,
        'd': 101,
        'e': 106,
        'i': 107,
        'o': 200
    }
    aniterable = ft_filter(lambda x: x < 150, asciDict.values())
    print(aniterable)
    # this value is printed before the NoneType exception
    [print(elem) for elem in aniterable]


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'{e}')