
def apply_async(func, args, *, a):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    a(result)
def print_result(result):
    print('Got:', result)
def add(x, y):
    return x + y
    
apply_async(add,(2, 3), a=print_result)
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
