#Functions that you have implemented in the Queue section

def enqueue(queue, new_item):
	queue.append(new_item)

def dequeue(queue):
    #We have added return here, just to return the item that is being removed
	return queue.pop(0)
    
def is_empty(queue):
	return len(queue) == 0

def size(queue):
    return len(queue)


def hot_potato_simulator(players, turns):
    hot_potato_queue = [] 
    
    for player in players:
        enqueue(hot_potato_queue,player)
    #print ('Hot Potato Queue is ',hot_potato_queue)
    
    while size(hot_potato_queue)> 1:         
       for i in range(turns):
           x= dequeue(hot_potato_queue)
           #print ('potato is with ',x, end ='\n')
           enqueue(hot_potato_queue, x) 
           #print ('Now queue is ',hot_potato_queue)
            #Enqueue the next-to-last element from the queue to the end

       dequeue(hot_potato_queue)

    return dequeue(hot_potato_queue) #Dequeue last element from the queue (The winner)


## Do not change code below this line
players = ["Peter", "John", "Luka", "Maria", "Sophia", "Derek"]
turns = 10
print(hot_potato_simulator(players, turns))
