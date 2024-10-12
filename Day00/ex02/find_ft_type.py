def all_thing_is_obj(object:any) -> int:
    prefix =''
    if (object.__class__ == list):
        prefix = 'List : '
        print(prefix, object.__class__)
    elif (object.__class__ == tuple):
        prefix = 'Tuple : '
        print(prefix, object.__class__)
    elif (object.__class__ == set):
        prefix = 'Set : '
        print(prefix, object.__class__)
    elif (object.__class__ == dict):
        prefix = 'Dict : '
        print(prefix, object.__class__)
    elif (object.__class__ == str):
        prefix = f'{object} is in the kitchen :'
        print(prefix, object.__class__)
    else:
        print('Type not found')
    return 42
