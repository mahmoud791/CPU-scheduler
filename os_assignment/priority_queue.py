from process import*


# A simple implementation of Priority Queue
# using Queue.
class TimeQueue(object):
    def __init__(self):
        self.queue = []
  
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def put(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def get(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].time_remaining < self.queue[min].time_remaining:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print('index out of boundries ya 3ashry')
            exit()



class SimpleQueue(object):
    def __init__(self):
        self.queue = []
  
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def put(self, data):
        self.queue.append(data)
  
    # for popping an element 
    def get(self):
        if self.isEmpty():
            print('queue is empty')

        else:
            item = self.queue[0]
            del self.queue[0]
            return item



class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def put(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def get(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].priority < self.queue[min].priority:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print('index out of boundries ya 3ashry')
            exit()