'''QUEUE'''


class Queue:
    def __init__(self, capacity, process_rate):
        self.items = []
        self.capacity = capacity
        self.process_rate = process_rate
    def __str__(self):
        return str(self.items)
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []

    def is_full(self):
        return self.size() == self.capacity
    
    def enqueue(self, item):
        if not self.is_full():
            self.items.insert(0,item)
        else:
            drop_item = item
            return drop_item
    
    def dequeue(self):
        if not self.is_empty():
            self.items.pop()
        else:
            return None



'''LINKED LIST'''


'''class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return '{}'.format(self.cargo)'''


class Node:
    def __init__(self, cargo = None, last = None):
        self.cargo = cargo
        self.last = last 
    
    def __str__(self):
        return '{}'.format(self.cargo)


class NodeStack:
    def __init__(self):
        self.length = 0
        self.last = None
    
    def is_empty(self):
        return self.length == 0

    def insert(self,cargo):
        self.length += 1
        self.last = Node(cargo=cargo, last= self.last)

    def remove(self):
        if self.is_empty():
            return None
        else:
            self.length -= 1
            # self.last = Node(cargo = self.last.last.cargo, last = self.last.last.last)
            self.last = self.last.last
            



node_stack = NodeStack()
node_stack.insert('cargo_1')
node_stack.insert('cargo_2')
node_stack.insert('cargo_3')
print(node_stack.last)
node_stack.remove()
print(node_stack.last)    
node_stack.remove()
print(node_stack.last)    