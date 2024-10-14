def all_thing_is_obj(object: any) -> int:
    prefix = ''

    match object:
        case list():
            prefix = 'List : '
            print(prefix, object.__class__)
        case tuple():
            prefix = 'Tuple : '
            print(prefix, object.__class__)
        case  set():
            prefix = 'Set : '
            print(prefix, object.__class__)
        case dict():
            prefix = 'Dict : '
            print(prefix, object.__class__)
        case str():
            prefix = f'{object} is in the kitchen :'
            print(prefix, object.__class__)
        case _:
            print('Type not found')
    return 42
