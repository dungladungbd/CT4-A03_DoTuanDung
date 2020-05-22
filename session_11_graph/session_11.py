class Node:
    def __init__(self, cargo=None, nexts=None):
        self.cargo = cargo
        self.nexts = nexts

    def __str__(self):
        return '{}'.format(self.cargo)


class NodeQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.capacity

    def enqueue(self, cargo):
        if self.is_full():
            return cargo
        elif self.is_empty():
            self.head = Node(cargo)
            self.length += 1
        else:
            loop = True
            last = self.head
            while loop:
                if last.nexts == None:
                    last.nexts = Node(cargo)
                    loop = False
                else:
                    last = last.nexts
            self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            del_items = self.head.cargo
            self.head = self.head.nexts
            self.length -= 1
            return del_items

queue = NodeQueue(5)
queue.enqueue('haha')
print(queue.head)
queue.enqueue('haha2')
print(queue.head.nexts)
queue.enqueue('hahaiuweifiayfia')
queue.enqueue('ajdfha')
queue.dequeue()
print(queue.head)
queue.dequeue()
print(queue.head)
