queue = []

# scheccules a function in n ticks
def schedcule(delay, func, *args):
    while len(queue) <= delay:
        queue.append([])
    queue[delay].append((func, args))

# executes a tick
def tick():
    if len(queue) == 0:
        return
    tasks = queue.pop(0)
    for task in tasks:
        task[0](*task[1])


