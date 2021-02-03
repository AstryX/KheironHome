#Robertas Dereskevicius 2021 Kheiron Take-home Exercise
#The logic for a basic infix calculator

from Helper import get_op
    
#Have to handle the extra bracket operations (in this case we are looking for the end of
#the current bracket and splitting the tasks to be computed in a binary tree-style)
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
    #If no split point is found in the data then just return the remaining int (out of the loop)
    for i in range(len(data)):
        #Data stored as a list in this case that is split multiple times recursively
        cur_op = get_op(data[i])
        #Callable can be used to check if the object is a function
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

