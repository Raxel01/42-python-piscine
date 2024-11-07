# from ft_filter import ft_filter
# import sys


data = 'Hello the World les enfant'


def check():
    pass


def main():
    """
this is The main Function where all the functions will be called
    """
    # asArr = data.split(' ')
    result = filter(lambda elem: len(elem) > 90, data)
    [print(elem) for elem in result]


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'{e}')
