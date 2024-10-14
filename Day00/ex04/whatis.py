import sys

def global_Checker(sys) -> int:
    if len (sys.argv) == 1:
        exit()
    status = 'continue'
    to_int = ''
    try :
        if len(sys.argv) == 2:
            
            to_int = int(sys.argv[1])
        else:
            raise AssertionError('more than one argument is provided')
    except Exception as e:
        prefix = 'AssertionError: '
        e = 'argument is not an integer' if type(e) == ValueError else e 
        print(f'{prefix}{e}')
        status = 'stop'
    return {'To_int' : to_int,
            'Status' : status
        }

def main(number):
    print(number)
    result = {True:'I\'m Even.' , False: 'I\'m Odd.'} [number % 2 == 0]
    print(result)

if __name__ == "__main__":
    # check for overflow so ! 
    print(int('89987897654613124567897456324134678956487456489456489'))
    # data = global_Checker(sys)
    # if ( data.get('Status') == 'continue'):
    #     main(data.get('To_int'))

    