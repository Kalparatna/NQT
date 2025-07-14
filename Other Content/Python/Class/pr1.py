class CustomQueue:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.rear = 0
        self.front = 0

    def enqueue(self, item):
        if self.size >= self.capacity:
            self.expand_array()
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        item = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def expand_array(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % len(self.array)]
        self.array = new_array
        self.front = 0
        self.rear = self.size

    def __str__(self):
        return str(self.array)

# Example usage
queue = CustomQueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
