#Robertas Dereskevicius 2021 Kheiron Take-home Exercise
#The logic for a basic prefix calculator

from collections import deque
from Helper import get_op
    
def compute(data):
    #Using deque to pop the leftmost value from the input
    cur_op = get_op(data.popleft())
    #Callable can be used to check if the object is a function
    if callable(cur_op):
        return cur_op(compute(data), compute(data))
    else:
        return int(cur_op)

if __name__=='__main__':      
    print("Input your space separated integers and operators:")
    data = input().split()
    print(compute(deque(data)))

