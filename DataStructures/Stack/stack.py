def new_stack():
    stack =  {'size': 0, 'first': None, 'last': None}
    return stack

def push(stack, object):
    dato = {'info': object, 'next': None}
    
    if stack["size"] == 0:
        stack["last"]=dato
    else: 
        dato['next'] = stack["first"]
        
    stack["size"]+=1
    stack["first"]=dato
    
    return stack

def pop(stack):
    assert stack["size"]==0, "EmptyStructureError: stack is empty"
    
    first = stack["first"]
    next = first["next"]

    stack["first"] = next
        
    stack["size"]-=1
    
    if stack["size"]==0:
        stack["last"]=None
        
    return first["info"]

def is_empty(stack):
    if stack["size"]==0:
        return True
    else:
        return False
    
def top(stack):
    assert stack["size"]==0, "EmptyStructureError: stack is empty"
    return stack["first"]["info"]

def size(stack):
    return stack["size"]

