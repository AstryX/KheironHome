from collections import deque

def multiplication(_left, _right):
    return _left * _right
    
def division(_left, _right):
    return _left / _right
    
def addition(_left, _right):
    return _left + _right
    
def subtraction(_left, _right):
    return _left - _right

def get_op(x):
    return {
        '*': multiplication,
        '/': division,
        '+': addition,
        '-': subtraction,   
    }.get(x, x)
    
def compute(data):
    cur_op = get_op(data.popleft())
    if callable(cur_op):
        return cur_op(compute(data), compute(data))
    else:
        return int(cur_op)

if __name__=='__main__':      
    print("Input your space separated integers and operators:")
    data = input().split()
    print(compute(deque(data)))

