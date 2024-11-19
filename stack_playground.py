# Initialize an empty stack using a list
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after pushing elements:", stack)

# Pop elements from the stack
popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack)

# Peek at the top element without removing it
if stack:
    top_item = stack[-1]
    print("Top element:", top_item)

# Check if stack is empty
is_empty = len(stack) == 0
print("Is stack empty?", is_empty)

# Get stack size
stack_size = len(stack)
print("Stack size:", stack_size)
