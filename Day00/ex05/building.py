import sys


def get_input() -> str:
    """ + when None arg is provided
                    or
        arg is empty argv[1] == ""
        I ask user for his input
    """
    _user_input = ''
    while 1:
        line = input('what\'s the text to count : \n')
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
    _data_to_process_ = ''
    match len(argv):
        case 2:
            match len(argv[1]):
                case 0:
                    _data_to_process_ = get_input()
                case _:
                    _data_to_process_ = argv[1]
            # two cases maybe string have varacteres or "\0"
        case 1:
            _data_to_process_ = get_input()
        case _:
            raise AssertionError('AssertionError: Sequence args provided !')
    return _data_to_process_


def type_recognizer(input: str):
    """ + this function is maked to count
        + all occurent of every caractere type :
        + ['upper, lower', 'punct', 'digits',  'spaces']
    """
    pass


def main():
    """+ This is the main function that will contain
       + general steps that my program does so big
       + functionnalities will be called Here
    """
    provided_string = global_Validator(sys.argv)
    print(f'The text contain {len(provided_string)}') 


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'{e}')
