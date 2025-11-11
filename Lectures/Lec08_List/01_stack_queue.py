
Stack = []
Queue = []

# Stack Operations
def push(stack, item):
    stack.append(item)
def pop(stack):
    if len(stack) == 0:
        return "Error!"
    return stack.pop()

# Queue Operations
def enqueue(queue, item):
    queue.append(item)
def dequeue(queue):
    if len(queue) == 0:
        return "Error!"
    return queue.pop(0)

################ 사용 ###############
enqueue(Queue, 1)
enqueue(Queue, 2)  
print(dequeue(Queue))  # 2
print(dequeue(Queue))  # 1  
print(dequeue(Queue))  # Error!
