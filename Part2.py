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
    
def get_sub_split(list_op):
    bracket_counter = 1
    for i in range(1, len(list_op)):
        if list_op[i] == "(":
            bracket_counter += 1
        elif list_op[i] == ")":
            bracket_counter -= 1
            if bracket_counter == 0:
                return list_op[1:i], list_op[i+1:]
    
def compute(data):
    for i in range(len(data)):
        cur_op = get_op(data[i])
        if callable(cur_op):
            return cur_op(compute(data[:i]), compute(data[i+1:]))
        elif cur_op == '(':
            left, right = get_sub_split(data)
            if len(right) == 0:
                return compute(left)
            else:
                return get_op(right[0])(compute(left), compute(right[1:])) 
    return int(data[0])

if __name__=='__main__':      
    print("Input your space separated integers and operators:")
    data = input().split()
    print(compute(data))

