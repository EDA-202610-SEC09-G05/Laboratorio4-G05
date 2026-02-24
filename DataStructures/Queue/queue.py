def new_queue():
    return {
        "elements": all.new_list()
    }
    
def enqueue(my_queue, element):
    all.add_last(my_queue["elements"], element)
    return my_queue

def dequeue(my_queue):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')

    element = all.get_element(my_queue["elements"], 1)
    all.delete_element(my_queue["elements"], 1)
    return element

def peek(my_queue):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')

    return all.get_element(my_queue["elements"], 1)

def is_empty(my_queue):
    return size(my_queue) == 0

def size(my_queue):
    return all.size(my_queue["elements"])
    
    
