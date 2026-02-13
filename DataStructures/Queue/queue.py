def new_queue():
    queue = {
        "elements": all.new_list()
    }
    return queue
def enqueue(my_queue, element):
    all.add_last (my_queue["elements"], element)

def dequeue(my_queue):
    if my_queue["size"] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    else: 
       x = my_queue["first"]["element"]
    return x
    
    
