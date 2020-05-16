def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def iterative_fibonacci(n):
    base_1, base_2 = 0, 1
    for i in range(n):
        base_1, base_2 = base_2, base_1 + base_2
    return base_1

memory = {0:0, 1:1}
def recursive_memory(n):
    if not n in memory:
        memory[n] = recursive_memory(n-1) + recursive_memory(n-2)
    return memory[n]
