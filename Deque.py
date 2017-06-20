class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueueFront(self,item):
        self.items.insert(0,item)
        print("Item queued front")

     def enqueueEnd(self,item):
        self.items.insert(len(self.items)-1,item)
        print("Item queued back")

    def dequeueFront(self):
        return self.items.pop(0)

    def dequeueEnd(self):
        return self.items.pop(len(self.items)-1)

    def size(self):
        return self.items.len()