import math

def NULL_not_found(object: any) -> int:
    funcReturn = 1
    data_type = {
        None     : 'Nothing',
        math.nan : 'Cheese',
        0        : 'Zero',
        ''       : 'Empty',
        False    : 'Fake'
    }
    
    params_type = data_type.get(object, "Type not Found")

    if object is None and isinstance(object, type(None)):
        print(f'{params_type} : {object} {object.__class__}')
        funcReturn = 0
    
    elif  object.__class__ == float and math.isnan(object):
        params_type = 'Cheese'
        print(f'{params_type} : {object} {object.__class__}')
        funcReturn = 0
    
    elif object == 0 and object.__class__ == int:
        params_type = 'Zero'
        print(f'{params_type} : {object} {object.__class__}')
        funcReturn = 0
    elif object == '' and isinstance(object, str):
        print(f'{params_type} : {object} {object.__class__}')
        funcReturn = 0
    elif object == False and object.__class__ == bool:
        print(f'{params_type} : {object} {object.__class__}')
        funcReturn = 0
    else:
        print(params_type)
    return funcReturn