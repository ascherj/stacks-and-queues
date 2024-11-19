from collections import deque

# Initialize an empty queue using deque
queue = deque()

# Enqueue elements to the queue
queue.append(1)  # Add 1 to the right end
queue.append(2)  # Add 2 to the right end
queue.append(3)  # Add 3 to the right end

print("Queue after enqueuing elements:", queue)

# Dequeue elements from the queue
dequeued_item = queue.popleft()  # Remove and return leftmost element
print("Dequeued item:", dequeued_item)
print("Queue after dequeuing:", queue)

# Peek at the front element without removing it
if queue:
    front_item = queue[0]
    print("Front element:", front_item)

# Check if queue is empty
is_empty = len(queue) == 0
print("Is queue empty?", is_empty)

# Get queue size
queue_size = len(queue)
print("Queue size:", queue_size)
