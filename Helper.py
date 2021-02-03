#Common helper function that holds logic regarding the different calculator operations.

def multiplication(_left, _right):
    return _left * _right
    
def division(_left, _right):
    return _left / _right
    
def addition(_left, _right):
    return _left + _right
    
def subtraction(_left, _right):
    return _left - _right

#Using a more readable structure for defining the action of each individual operator rather than a bunch of if/elif statements.
def get_op(x):
    return {
        '*': multiplication,
        '/': division,
        '+': addition,
        '-': subtraction,   
    }.get(x, x)
    

