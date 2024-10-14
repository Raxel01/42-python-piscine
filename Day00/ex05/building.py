import sys
from string import ascii_lowercase, ascii_uppercase
from string import digits, whitespace, punctuation


def get_input() -> str:
    """ + when None arg is provided
                    or
        arg is empty argv[1] == ""
        I ask user for his input
    """
    _user_input = ''
    while 1:
        line = input('what\'s the text to count : \n')
        print('Your line : |', line, "|")
        if line:
            _user_input = line
            break
    return _user_input


def global_Validator(argv) -> str:
    """ + check for argv len
     + if it  len == 2 that mean I have enought args
     + else either there is no args else there is more args > 2, 3 ,4,5!
     + so return the  string : given one or readed from input !
    """
    _user_input = ''
    match len(argv):
        case 2:
            match len(argv[1]):
                case 0:
                    _user_input = get_input()
                case _:
                    _user_input = argv[1]
            # two cases maybe string have varacteres or "\0"
        case 1:
            _user_input = get_input()
        case _:
            raise AssertionError('AssertionError: Sequence args provided !')
    return _user_input


def type_recognizer(_user_input: str):
    """ + this function is maked to count
        + all occurent of every caractere type :
        + [lower' ,'upper' , 'punct', 'digits',  'spaces']
    """
    print(f'The text contain {len(_user_input)}')
    # declaration
    upper, lower, puncts, Digits, spaces = 0, 0, 0, 0, 0

    for char in _user_input:
        if char in ascii_lowercase:
            lower += 1
        elif char in ascii_uppercase:
            upper += 1
        elif char in punctuation:
            puncts += 1
        elif char in digits:
            Digits += 1
        elif char in whitespace:
            spaces += 1
    counter_dic = {
        'upper': f'{upper} upper letters',
        'lower': f'{lower} lower letters',
        'puncts': f'{puncts} punctuation marks',
        'spaces': f'{spaces} spaces',
        'Digits': f'{Digits} digits'
    }
    return counter_dic


def main():
    """+ This is the main function that will contain
       + general steps that my program does so big
       + functionnalities will be called Here
    """
    _user_input = global_Validator(sys.argv)
    counter_dict = type_recognizer(_user_input)
    for key, value in counter_dict.items():
        print(f'{key} {value}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'{e}')
